"""
tcp 服务端循环流程 2

重点代码!!!
"""

from socket import *

# 创建tcp套接字 其实使用默认值就是tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听,让tcp套接字可以被链接
tcp_socket.listen(5)

while True:
    print("等待客户消息：")
    connfd,addr=tcp_socket.accept()
    data=connfd.recv(1024)
    print("接收到：",data.decode())
    connfd.send(b"thank")
    connfd.close()
tcp_socket.close()
