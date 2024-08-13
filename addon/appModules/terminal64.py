import appModuleHandler, globalPluginHandler, ui, api, winUser, speech, review, mouseHandler, ctypes, threading, os, tones, scriptHandler, gui

from keyboardHandler import KeyboardInputGesture
from scriptHandler import script
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from windowUtils import findDescendantWindow
from functools import wraps, lru_cache

def finally_(func, final):
	"""Calls final after func, even if it fails."""
	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()
		return new
	return wrap(final)

class AppModule(appModuleHandler.AppModule):
	scriptCategory = "MetaTrader"
	timer = None
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.toggling = False
		new_lines = '''کندل	کَندِل	0	0
فارکس	فارِکس	0	0
'''
		appdata_folder = os.getenv('APPDATA')
		file_path = os.path.join(appdata_folder, 'nvda', 'speechDicts', 'default.dic')
		if os.path.exists(file_path):
			with open(file_path, 'r', encoding='utf-8') as file:
				content = file.read()
			if new_lines  not in content:
				content += f'{new_lines}'
				with open(file_path, 'a', encoding='utf-8') as file:
					file.write(content)
		else:
			with open(file_path, 'w', encoding='utf-8') as file:
				file.write(f'{new_lines}')

	def getScript(self, gesture):
		if not self.toggling:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script = finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def script_error(self, gesture):
		tones.beep(120, 100)

	def finish(self):
		self.toggling = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_csv_file(self, gestures):
		if self.toggling:
			self.script_error(gesture)
			return
		self.bindGestures(self.__csv_fileGestures)
		self.toggling = True
		tones.beep(100, 10)
		ui.message('1 for one hour, 2 for daily, 3 for monthly, 4 for four hours, 7 for weekly')
	script_csv_file.__doc__ = ('TA assistant csv files layer commands')

	def buy(self):
		self.trade()
		KeyboardInputGesture.fromName('home').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('space').send()
		ui.message('buy')

	def script_buy(self, gesture):
		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			self.buy()
			self.script_DataWindow(self)

		if obj == 10064:
			self.buy()
			self.script_Navigator(self)

		if obj == 10144:
			self.buy()
			self.script_MarketWatch(self)

		if obj == 10328:
			self.buy()
			self.script_trade(self)

		if obj == 10707:
			self.buy()
			self.script_history(self)
	script_buy.__doc__ = ('buy action')

	def sell(self):
		self.trade()
		KeyboardInputGesture.fromName('home').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('space').send()
		ui.message('sell')

	def script_sell(self, gesture):
		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			self.sell()
			self.script_DataWindow(self)

		if obj == 10064:
			self.sell()
			self.script_Navigator(self)

		if obj == 10144:
			self.sell()
			self.script_MarketWatch(self)

		if obj == 10328:
			self.sell()
			self.script_trade(self)

		if obj == 10707:
			self.sell()
			self.script_history(self)
	script_sell.__doc__ = ('sell action')

	def dataWindow(self):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=32844),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			ui.message(_("Not in a window"))
			return
		obj.setFocus()

	def script_DataWindow(self, gesture):
		self.dataWindow()
	script_DataWindow.__doc__ = ('goes to data window')

	def close(self):
		KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send()
		a = api.getClipData().split('\r\n')
		ui.message(f'{a[6]}')

	def script_close(self, gesture):
		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			self.close()
			self.script_DataWindow(self)

		if obj == 10064:
			self.close()
			self.script_Navigator(self)

		if obj == 10144:
			self.close()
			self.script_MarketWatch(self)

		if obj == 10328:
			self.close()
			self.script_trade(self)

		if obj == 10707:
			self.close()
			self.script_history(self)
	script_close.__doc__ = ('reads close in data window')

	def script_Navigator(self, gesture):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=10064),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			ui.message(_("Not in a window"))
			return
		obj.setFocus()
		ui.message('navigator window')
	script_Navigator.__doc__ = ('goes to Navigator')

	def script_Toolbox(self, gesture):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=10128),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			ui.message(_("Not in a window"))
			return
		obj.setFocus()
		ui.message('toolbox window')
	script_Toolbox.__doc__ = ('goes to tool box')

	def script_MarketWatch(self, gesture):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=10144),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			ui.message(_("Not in a window"))
			return
		obj.setFocus()
		ui.message('MarketWatch window')
	script_MarketWatch.__doc__ = ('goes to MarketWatch')

	def trade(self):
		self.history()
		winUser.setCursorPos(37, 703)
		mouseHandler.executeMouseMoveEvent(37, 703)
		mouseHandler.doPrimaryClick()

	def script_trade(self, gesture):
		self.trade()
		ui.message('trade window')
	script_trade.__doc__ = ('goes to trade')

	def script_closeTrade(self, gesture):
		tradeAndKeyboardVeriables = self.trade(), KeyboardInputGesture.fromName('home').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send(), ui.message('trade closed')

		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			tradeAndKeyboardVeriables 
			self.script_DataWindow(self)

		if obj == 10064:
			tradeAndKeyboardVeriables 
			self.script_Navigator(self)

		if obj == 10144:
			tradeAndKeyboardVeriables 
			self.script_MarketWatch(self)

		if obj == 10328:
			tradeAndKeyboardVeriables 
			self.script_trade(self)

		if obj == 10707:
			tradeAndKeyboardVeriables 
			self.script_history(self)
	script_closeTrade.__doc__ = ('goes to trade and closes it')

	def script_openModify(self, gesture):
		tradeAndKeyboardVeriables = self.trade(), KeyboardInputGesture.fromName('home').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send(), ui.message('Modify or Delete  window')

		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			tradeAndKeyboardVeriables 

		if obj == 10064:
			tradeAndKeyboardVeriables 

		if obj == 10144:
			tradeAndKeyboardVeriables 

		if obj == 10328:
			tradeAndKeyboardVeriables 

		if obj == 10707:
			tradeAndKeyboardVeriables 
	script_openModify.__doc__ = ('opens modify or delete ')

	def script_openModifyPendingOrder(self, gesture):
		tradeAndKeyboardVeriables = self.trade(), KeyboardInputGesture.fromName('end').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send(), ui.message('Modify or Delete  pending order window ')

		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			tradeAndKeyboardVeriables 

		if obj == 10064:
			tradeAndKeyboardVeriables 

		if obj == 10144:
			tradeAndKeyboardVeriables 

		if obj == 10328:
			tradeAndKeyboardVeriables 

		if obj == 10707:
			tradeAndKeyboardVeriables 
	script_openModifyPendingOrder.__doc__ = ('opens modify or delete pending order')

	def history(self):
		winUser.setCursorPos(162, 703)
		mouseHandler.executeMouseMoveEvent(162, 703)
		mouseHandler.doPrimaryClick()

	def script_history(self, gesture):
		self.history()
		ui.message('history window')
	script_history.__doc__ = ('goes to history')

	def script_report_xlsx(self, gesture):
		tradeAndKeyboardVeriables = self.history(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('alt+y').send(), ui.message('Open XML')

		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			tradeAndKeyboardVeriables 

		if obj == 10064:
			tradeAndKeyboardVeriables 

		if obj == 10144:
			tradeAndKeyboardVeriables 

		if obj == 10328:
			tradeAndKeyboardVeriables 

		if obj == 10707:
			tradeAndKeyboardVeriables 

	script_report_xlsx.__doc__ = ('opens xlsx file')

	def script_report_html(self, gesture):
		tradeAndKeyboardVeriables = self.history(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('uparrow').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('alt+y').send(), ui.message('html')

		obj = api.getNavigatorObject().windowControlID

		if obj == 32844:
			tradeAndKeyboardVeriables 

		if obj == 10064:
			tradeAndKeyboardVeriables 

		if obj == 10144:
			tradeAndKeyboardVeriables 

		if obj == 10328:
			tradeAndKeyboardVeriables 

		if obj == 10707:
			tradeAndKeyboardVeriables 

	script_report_html.__doc__ = ('opens html file')


	def symbol(self):
		self.dataWindow()
		KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send()
		clip = api.getClipData().split('\r\n')
		symbol_index = f'{clip[0]}'.index(',')
		symbol = f'{clip[0][:symbol_index]}'
		return f'{symbol}'

	def hourly(self):
		KeyboardInputGesture.fromName('enter').send()
		self.symbol()
		folder_path = f'C:\Program Files\MetaTrader 5\MQL5\Files\{self.symbol()}_H1.csv'
		if os.path.exists(folder_path):
			ctypes.windll.shell32.ShellExecuteW(None, "open", folder_path, None, None, 1)
		else:
			file_path = os.path.join(os.getenv('APPDATA'), 'MetaQuotes', 'Terminal', 'D0E8209F77C8CF37AD8BF550E51FF075/MQL5', 'Files', f'{self.symbol()}_H1.csv')
			ctypes.windll.shell32.ShellExecuteW(None, "open", file_path, None, None, 1)

	def script_hourly(self, gesture):
		self.symbol()
		ui.message('1 hour csv file')
		KeyboardInputGesture.fromName('alt+c').send(), KeyboardInputGesture.fromName('f').send(), KeyboardInputGesture.fromName('o').send()
		KeyboardInputGesture.fromName('alt+i').send(), KeyboardInputGesture.fromName('e').send(), KeyboardInputGesture.fromName('t').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('enter').send()
		if self.timer: self.timer.cancel()
		self.timer = threading.Timer(4, self.hourly)
		self.timer.start()
	script_hourly.__doc__ = ('changes time frame to 1 hour and creates hourly csv file with TAAssistant')

	def four_hours(self):
		KeyboardInputGesture.fromName('enter').send()
		self.symbol()
		folder_path = f'C:\Program Files\MetaTrader 5\MQL5\Files\{self.symbol()}_H4.csv'
		if os.path.exists(folder_path):
			ctypes.windll.shell32.ShellExecuteW(None, "open", folder_path, None, None, 1)
		else:
			file_path = os.path.join(os.getenv('APPDATA'), 'MetaQuotes', 'Terminal', 'D0E8209F77C8CF37AD8BF550E51FF075/MQL5', 'Files', f'{self.symbol()}_H4.csv')
			ctypes.windll.shell32.ShellExecuteW(None, "open", file_path, None, None, 1)

	def script_four_hours(self, gesture):
		self.symbol()
		ui.message('4 hours csv file')
		KeyboardInputGesture.fromName('alt+c').send(), KeyboardInputGesture.fromName('f').send(), KeyboardInputGesture.fromName('4').send()
		KeyboardInputGesture.fromName('alt+i').send(), KeyboardInputGesture.fromName('e').send(), KeyboardInputGesture.fromName('t').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('enter').send()

		if self.timer: self.timer.cancel()
		self.timer = threading.Timer(4, self.four_hours)
		self.timer.start()
	script_four_hours.__doc__ = ('changes time frame to 4 hours and creates 4 hours csv file with TAAssistant')

	def daily(self):
		KeyboardInputGesture.fromName('enter').send()
		self.symbol()
		folder_path = f'C:\Program Files\MetaTrader 5\MQL5\Files\{self.symbol()}_D1.csv'
		if os.path.exists(folder_path):
			ctypes.windll.shell32.ShellExecuteW(None, "open", folder_path, None, None, 1)
		else:
			file_path = os.path.join(os.getenv('APPDATA'), 'MetaQuotes', 'Terminal', 'D0E8209F77C8CF37AD8BF550E51FF075/MQL5', 'Files', f'{self.symbol()}_D1.csv')
			ctypes.windll.shell32.ShellExecuteW(None, "open", file_path, None, None, 1)

	def script_daily(self, gesture):
		self.symbol()
		ui.message('daily csv file')
		KeyboardInputGesture.fromName('alt+c').send(), KeyboardInputGesture.fromName('f').send(), KeyboardInputGesture.fromName('d').send()
		KeyboardInputGesture.fromName('alt+i').send(), KeyboardInputGesture.fromName('e').send(), KeyboardInputGesture.fromName('t').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('enter').send()

		if self.timer: self.timer.cancel()
		self.timer = threading.Timer(4, self.daily)
		self.timer.start()
	script_daily.__doc__ = ('changes time frame to daily and creates daily csv file with TAAssistant')

	def weekly(self):
		KeyboardInputGesture.fromName('enter').send()
		self.symbol()
		folder_path = f'C:\Program Files\MetaTrader 5\MQL5\Files\{self.symbol()}_W1.csv'
		if os.path.exists(folder_path):
			ctypes.windll.shell32.ShellExecuteW(None, "open", folder_path, None, None, 1)
		else:
			file_path = os.path.join(os.getenv('APPDATA'), 'MetaQuotes', 'Terminal', 'D0E8209F77C8CF37AD8BF550E51FF075/MQL5', 'Files', f'{self.symbol()}_W1.csv')
			ctypes.windll.shell32.ShellExecuteW(None, "open", file_path, None, None, 1)

	def script_weekly(self, gesture):
		self.symbol()
		ui.message('weekly csv file')
		KeyboardInputGesture.fromName('alt+c').send(), KeyboardInputGesture.fromName('f').send(), KeyboardInputGesture.fromName('w').send()
		KeyboardInputGesture.fromName('alt+i').send(), KeyboardInputGesture.fromName('e').send(), KeyboardInputGesture.fromName('t').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('enter').send()

		if self.timer: self.timer.cancel()
		self.timer = threading.Timer(4, self.weekly)
		self.timer.start()
	script_weekly.__doc__ = ('changes time frame to weekly and creates weekly csv file with TAAssistant')

	def monthly(self):
		KeyboardInputGesture.fromName('enter').send()
		self.symbol()
		folder_path = f'C:\Program Files\MetaTrader 5\MQL5\Files\{self.symbol()}_MN1.csv'
		if os.path.exists(folder_path):
			ctypes.windll.shell32.ShellExecuteW(None, "open", folder_path, None, None, 1)
		else:
			file_path = os.path.join(os.getenv('APPDATA'), 'MetaQuotes', 'Terminal', 'D0E8209F77C8CF37AD8BF550E51FF075/MQL5', 'Files', f'{self.symbol()}_MN1.csv')
			ctypes.windll.shell32.ShellExecuteW(None, "open", file_path, None, None, 1)

	def script_monthly(self, gesture):
		self.symbol()
		ui.message('monthly csv file')
		KeyboardInputGesture.fromName('alt+c').send(), KeyboardInputGesture.fromName('f').send(), KeyboardInputGesture.fromName('n').send()
		KeyboardInputGesture.fromName('alt+i').send(), KeyboardInputGesture.fromName('e').send(), KeyboardInputGesture.fromName('t').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('enter').send()
		if self.timer: self.timer.cancel()
		self.timer = threading.Timer(4, self.monthly)
		self.timer.start()
	script_monthly.__doc__ = ('changes time frame to monthly and creates monthly csv file with TAAssistant')

	__csv_fileGestures = {
		"kb:1": "hourly",
		"kb:4": "four_hours",
		"kb:2": "daily",
		"kb:7": "weekly",
		"kb:3": "monthly",
	}

	__gestures = {
		"kb:control+1": "DataWindow",
		"kb:control+2": "trade",
		"kb:control+3": "Navigator",
		"kb:control+4": "MarketWatch",
		"kb:control+5": "close",
		"kb:control+6": "history",
		"kb:control+7": "Toolbox",
		"kb:control+8": "report_xlsx",
		"kb:control+9": "report_html",

		"kb:control+shift+1": "buy",
		"kb:control+shift+2": "sell",
		"kb:control+shift+3": "closeTrade",
		"kb:control+shift+4": "openModify",
		"kb:control+shift+5": "openModifyPendingOrder",
		"kb:control+shift+t": "csv_file"
	}
