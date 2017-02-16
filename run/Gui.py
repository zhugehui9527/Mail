# -*- coding:utf-8 -*-
import wx

class MyPanel(wx.Panel):
	def __init__(self, parent):
		super(MyPanel, self).__init__(parent)
		
		b = wx.Button(self, label=u'发送', pos=(100, 100))
		b.Bind(wx.EVT_BUTTON, self.btnclk)
		
		b = wx.Button(self, label=u'接收', pos=(100, 200))
		b.Bind(wx.EVT_BUTTON, self.btnclk)
		self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
	
	def OnButtonClicked(self, e):
		print 'Panel received click event. propagated to Frame class'
		e.Skip()
	
	def btnclk(self, e):
		print "Button received click event. propagated to Panel class"
		e.Skip()


class Example(wx.Frame):
	def __init__(self, parent):
		super(Example, self).__init__(parent)
		
		self.InitUI()
	
	def InitUI(self):
		mpnl = MyPanel(self)
		self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
		
		self.SetTitle(u'邮件发送')
		self.Centre()
		self.Show(True)
	
	def OnButtonClicked(self, e):
		print 'click event received by frame class'
		e.Skip()

ex = wx.App()
Example(None)
ex.MainLoop()