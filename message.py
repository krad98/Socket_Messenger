
import wx
import socket
import threading


class Message(wx.Panel):
	def __init__(self, parent, id, nom, address, port):
		wx.Panel.__init__(self, parent, id)

		self.nom = nom
		self.address = address
		self.port = port

		self.client = Client(self.address, self.port)

	

		vbox = wx.BoxSizer(wx.VERTICAL)

		self.listbox = wx.ListBox(self, -1, size=(500, 360))
		vbox.Add(self.listbox, 0.5, wx.EXPAND | wx.ALL, 5)

		panel1 = wx.Panel(self, -1)
		vbox1 = wx.BoxSizer(wx.VERTICAL)

		self.write = wx.TextCtrl(panel1, -1, style=wx.TE_MULTILINE, size=(500, 130))
		button_send = wx.Button(panel1, 1, 'Send')
	
		vbox1.Add(self.write, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.LEFT, 5)
		vbox1.Add(button_send, 0, wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, 5)

		panel1.SetSizer(vbox1)
		vbox.Add(panel1, 0, wx.EXPAND | wx.TOP, 5)
		self.SetSizer(vbox)

		self.Bind(wx.EVT_CLOSE, self.OnClose)
		button_send.Bind(wx.EVT_BUTTON, self.sendMessage)

		thread = threading.Thread(target=self.showMessage)
		thread.start()


		
		
	def SetValeur(self, nom, address, port):
		self.nom = nom
		self.address = address
		self.port = port


	
	def sendMessage(self, event):

		msg = self.write.GetValue()
		msg = f"({self.nom}): {msg}"
		self.client.sendMes(msg)
	
		self.write.Clear()


	def showMessage(self):
		etat = True
		while etat:
			response = self.client.receiveMes()
			self.listbox.Append(response)

			if response == '!fin':
				etat = False

		self.client.close()
		self.Destroy()



	def OnClose(self, event):
		self.client.close()
		self.Destroy()




class Client:

	def __init__(self, host, port):
		self.host = host
		self.port = port


		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_address = (self.host, self.port)
		self.sock.connect(server_address)


	def sendMes(self, message):
		self.sock.send(message.encode())


	def receiveMes(self):
		response = self.sock.recv(1024).decode()
		return response

	def close(self):
		self.sock.close()













