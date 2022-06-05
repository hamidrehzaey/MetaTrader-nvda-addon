import appModuleHandler, ui, api, winUser, speech
from keyboardHandler import KeyboardInputGesture
from scriptHandler import script
from NVDAObjects.IAccessible import getNVDAObjectFromEvent
from windowUtils import findDescendantWindow

class AppModule(appModuleHandler.AppModule):
	scriptCategory = "MetaTrader"

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
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
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
	script_close.__doc__ = ('close action')

	def script_Navigator(self, gesture):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=10064),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
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
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
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
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
			return
		obj.setFocus()
		ui.message('MarketWatch window')
	script_MarketWatch.__doc__ = ('goes to MarketWatch')

	def trade(self):
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=10328),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
			return
		obj.setFocus()

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
		try:
			obj = getNVDAObjectFromEvent(
			findDescendantWindow(api.getForegroundObject().windowHandle, visible=True, className=None, controlID=10707),
			winUser.OBJID_CLIENT, 0)
		except LookupError:
			# Translators: Error when trying to move focus in message body
			ui.message(_("Not in a message window"))
			return
		obj.setFocus()

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
		"kb:control+5": "closeTrade",
		"kb:control+6": "openModify",
		"kb:control+7": "openModifyPendingOrder",
		"kb:control+8": "close",
		"kb:control+9": "history",
		"kb:control+0": "Toolbox",
		"kb:control+-": "report_xlsx",
		"kb:control+=": "report_html",
		"kb:alt+1": "buy",
		"kb:alt+2": "sell",
	}
