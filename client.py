import socket

client = socket.socket()

client.connect(('192.168.210.86', 3000))

data = client.recv(1024)
print('Сообщение в бинарном виде', data)
print('Сообщение в бинарном виде', data.decode())

client.close()