import message as m

import wx

class Acceuil(wx.Frame):

	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(500, 600))

		panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.Colour('#00031A'))

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox0 = wx.BoxSizer(wx.HORIZONTAL)
		icon = wx.StaticBitmap(panel, -1, wx.Bitmap('img1.png'), size=(200, 200))
		hbox0.Add(icon, proportion=2)
		vbox.Add(hbox0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

		vbox.Add((-1, 20))

		hbox01 = wx.BoxSizer(wx.HORIZONTAL)
		tc01 = wx.StaticText(panel, -1, label='MESSAGERIE INSTANTANÉE')
		hbox01.Add(tc01, proportion=0, flag=wx.RIGHT | wx.TOP, border=8)
		vbox.Add(hbox01, flag=wx.ALIGN_CENTER, border=10)

		vbox.Add((-1, 30))


		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(panel, -1, label='User Name:', size=(125, -1))
		hbox1.Add(st1, proportion=0, flag=wx.RIGHT | wx.TOP, border=8)
		self.tc1 = wx.TextCtrl(panel, -1)
		hbox1.Add(self.tc1, proportion=1)
		vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

		vbox.Add((-1, 10))
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		st2 = wx.StaticText(panel, -1, label='Address Network:', size=(125, -1))
		hbox2.Add(st2, proportion=0, flag=wx.RIGHT | wx.TOP, border=8)
		self.tc2 = wx.TextCtrl(panel, -1)
		hbox2.Add(self.tc2, proportion=1)
		vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=8)

		vbox.Add((-1, 10))
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		st3 = wx.StaticText(panel, -1, label='Port:', size=(125, -1))
		hbox3.Add(st3, proportion=0, flag=wx.RIGHT | wx.TOP, border=8)
		self.tc3 = wx.TextCtrl(panel, -1)
		hbox3.Add(self.tc3, proportion=1)
		vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=8)

		vbox.Add((-1, 80))
		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		btn1 = wx.Button(panel, -1, label='OK', size=(70, 30))
		hbox4.Add(btn1, proportion=0)
		btn2 = wx.Button(panel, -1, label='Close', size=(70, 30))
		hbox4.Add(btn2, proportion=0, flag=wx.LEFT | wx.BOTTOM, border=5)
		vbox.Add(hbox4, proportion=0, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=10)

		panel.SetSizer(vbox)

		btn1.Bind(wx.EVT_BUTTON, self.valider)
		self.Bind(wx.EVT_CLOSE, self.OnClose)

		self.Centre()
		self.afficher()

	def valider(self, event):
		#self.afficher(False)

		a = self.tc1.GetValue()
		b = self.tc2.GetValue()
		c = self.tc3.GetValue()

		if a == '':
			a = 'Sans Nom'
		a = str(a)
		b = str(b)
		c = int(c)

		pan = m.Message(self, -1, a, b, c)
		pan.SetSize(500, 650)
		pan.SetBackgroundColour('#0F0136')

		
	
		pan.SetValeur(a, b, c)


		


	def afficher(self, val=True):
		if val == True:
			self.Show()
		else:
			self.Show(False)

	def OnClose(self, event):
		self.Destroy()

	





if __name__ == '__main__':
	app = wx.App()
	Acceuil(None, -1, 'Messagerie Instantanné')
	app.MainLoop()