import socket
import re
import time
import threading


from logic.ftp import ftp_send

import socket
import re
import threading
import time


class Client:
	def __init__(self, server_ip: str, port: int, password: str) -> None:
		self.server_ip = server_ip
		self.port = port
		self.SUPER_PASSWORD = password
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((self.server_ip, self.port))
		self.admin_thread = threading.Thread(target=self.connection)
		self.admin_thread.daemon = True
		self.admin_thread.start()

	def connection(self) -> None:
		while True:
			try:
				req = self.client.recv(1024)
				print(req.decode())
			except:
				continue


	def send(self, text: str, encode="utf-8") -> None:
		# text = self.SUPER_PASSWORD+"|"+text
		if encode:
			self.client.send(text.encode(encode))
		else:
			self.client.send(text)
		

if __name__ == "__main__":
	# SERVER_HOST = "212.115.110.10"
	SERVER_HOST = "192.168.1.100"
	SERVER_PORT = 7546
	SUPER_PASSWORD = "jesus_134"
	# client = Client("26.35.239.192", SERVER_PORT, SUPER_PASSWORD)
	# client = Client("26.172.116.184", SERVER_PORT, SUPER_PASSWORD)
	client = Client(SERVER_HOST, SERVER_PORT, SUPER_PASSWORD)
	client.send(SUPER_PASSWORD)
	while True:
		time.sleep(0.01)
		data = input(f"[{SERVER_HOST}:{SERVER_PORT}]$ ")
		if data == "exit":
			del client.admin_thread
			exit()

		client.send(data)
