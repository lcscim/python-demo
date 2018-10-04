import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
def tcplink(data,addr):
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
while True:
    data, addr = s.recvfrom(1024)
    t = threading.Thread(target=tcplink, args=(data, addr))
    t.start()
