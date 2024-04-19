import re

def ftp_get(self, name: str) -> None:
		file_bytes = b''
		while True:
			self.s.listen(100)
			conn, addr = self.s.accept()
			msg = conn.recv(1024)
			try:
				if "END" in msg.decode("utf-8"):
					conn.close()
					break
			except:
				pass
			file_bytes += msg
		with open(f"files/{name}", "wb") as file:
			file.write(file_bytes)

		print(f"[{self.SERVER_IP}:{self.SERVER_PORT}]$ Saved file in directory: files/{name}")

def ftp_send(self, src) -> None:
	with open(src, "rb") as f:
		b_file = f.read()

	self.send("FILE|" + re.split(r'[/\\]', src)[-1])

	bytes_list = [b_file[i:i + 4096] for i in range(0, len(b_file), 4096)]
	[self.send(i, encode=None) for i in bytes_list]

	self.send("END")
