import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("212.115.110.10", 7546))
print("YES")
client.close()
