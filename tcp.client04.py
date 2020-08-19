"""
tcp 客户端循环流程 2
重点代码 !!!
"""
from socket import *

#  服务端地址
ADDR = ("127.0.0.1",8888)
while True:
    msg=input(">>")
    if not msg:
     break

    tcp_socket=socket()
    tcp_socket.connect(ADDR)
    tcp_socket.send(msg.encode())
    data=tcp_socket.recv(1024)
    print("server:",data.decode())
    tcp_socket.close()