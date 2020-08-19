from socket import *
#创建套接字
s=socket()
s.bind(('0.0.0.0',8888))
s.listen(5)
#接收浏览器链接
connfd,addr=s.accept()
data=connfd.recv(1024*10)
print(data.decode())
#组织响应格式 http响应
html="HTTP/1.1 200 OK\r\n"
html+="Content-Type: text/html\r\n"
html+="\r\n"
with open("python.html") as f:
   html+=f.read()
connfd.send(html.encode())#发送响应给浏览器
connfd.close()
s.close()
