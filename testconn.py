import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("ip", 7546))
print("YES")
client.close()
