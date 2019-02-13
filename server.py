import socket
s=socket.socket()
s.bind(('169.254.118.241',1234))
s.listen(5)

while True:
    c,addr=s.accept()
    print('connected to',addr)
  
    c.close()
