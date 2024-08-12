import appModuleHandler, ui, api, winUser, mouseHandler, os
from keyboardHandler import KeyboardInputGesture
from scriptHandler import script
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from windowUtils import findDescendantWindow

class AppModule(appModuleHandler.AppModule):
	scriptCategory = "MetaTrader"
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

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

	def buy(self):
		self.trade()
		KeyboardInputGesture.fromName('home').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('space').send()
		ui.message('buy')

	def script_buy(self, gesture):
		obj = api.getNavigatorObject().windowControlID

		if obj == 35443:
			self.buy()
			self.script_DataWindow(self)

		if obj == 35439:
			self.buy()
			self.script_Navigator(self)

		if obj == 35441:
			self.buy()
			self.script_MarketWatch(self)

		if obj == 33217:
			self.buy()
			self.script_trade(self)

		if obj == 33208:
			self.buy()
			self.script_history(self)
	script_buy.__doc__ = ('buy action')

	def sell(self):
		self.trade()
		KeyboardInputGesture.fromName('home').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('shift+tab').send(), KeyboardInputGesture.fromName('space').send()
		ui.message('sell')

	def script_sell(self, gesture):
		obj = api.getNavigatorObject().windowControlID

		if obj == 35443:
			self.sell()
			self.script_DataWindow(self)

		if obj == 35439:
			self.sell()
			self.script_Navigator(self)

		if obj == 35441:
			self.sell()
			self.script_MarketWatch(self)

		if obj == 33217:
			self.sell()
			self.script_trade(self)

		if obj == 33208:
			self.sell()
			self.script_history(self)
	script_sell.__doc__ = ('sell action')

	def dataWindow(self):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=35443),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			ui.message(_("Not in a window"))
			return
		obj.setFocus()

	def script_DataWindow(self, gesture):
		self.dataWindow()
		ui.message('data window')
	script_DataWindow.__doc__ = ('goes to data window')

	def close(self):
		KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('applications').send(), KeyboardInputGesture.fromName('downarrow').send(), KeyboardInputGesture.fromName('enter').send()
		a = api.getClipData().split('\r\n')
		ui.message(f'{a[6]}')

	def script_close(self, gesture):
		obj = api.getNavigatorObject().windowControlID

		if obj == 35443:
			self.close()
			self.script_DataWindow(self)

		if obj == 35439:
			self.close()
			self.script_Navigator(self)

		if obj == 35441:
			self.close()
			self.script_MarketWatch(self)

		if obj == 33217:
			self.close()
			self.script_trade(self)

		if obj == 33208:
			self.close()
			self.script_history(self)
	script_close.__doc__ = ('close action')

	def script_Navigator(self, gesture):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=35439),
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
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=33212),
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
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=35441),
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
		winUser.setCursorPos(210, 703)
		mouseHandler.executeMouseMoveEvent(210, 703)
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
	}
