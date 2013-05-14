#!/usr/bin/python
# -*- coding: <encoding name> -*-
from threading import Thread
import socket
class ClientThread(Thread):
	def __init__(self, client,server, nick):
		super(ClientThread,self).__init__()
		self.nick = nick
		self.client = client
		self.server = server
	def __del__(self):
		print 'object deleted'
	def run(self):
		try:
			while 1:
				msg = self.client.recv(1024)
				if not msg:
					break
				messages = msg[:-1].split(';') #User may get many messages at the same time
				for m in messages:
					#splitting message to type and message
					print m
					tmp = m.split(':')
					type = tmp[0]
					if type == 'msg': #Message to another client
						self.server.sendMessage(tmp[1],self.nick,u'{0}'.format(tmp[2]))
			self.server.deleteUser(self.nick)
		except socket.error as mesg:
			print mesg
