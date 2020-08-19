"""
poll方法  IO多路复用网络并发
"""
from socket import *
from select import *
#创建好监听套接字 ,他也是IO对象
sockfd=socket()
sockfd.bind(('0.0.0.0',8886))
sockfd.listen(5)
#与非阻塞联合使用
sockfd.setblocking(False)
#创建poll对象
p=epoll()
#准备io监控 map字典用于查找IO对象
map={sockfd.fileno():sockfd}
#事件改为EPOLLIN
p.register(sockfd,EPOLLIN)
#循环IO发生
while True:
    #开始监控IO 阻塞等待监控的IO事件发生
    events=p.poll()#还是poll
    #io逐渐增加，就绪io也会复杂
    # 需要分类讨论列表 分两类 监听套接字，和客户端链接套接字
    for fd,event in events:
        # 对象判断是 is 数值判断是==
        if fd== sockfd.fileno():
            connfd,addr=map[fd].accept()
            print("Connect from",addr)
            connfd.setblocking(False)
            #增加监控
            p.register(connfd,EPOLLIN)
            #加入字典，添加到IO里
            map[connfd.fileno()]=connfd
        elif event == EPOLLIN:
            #客户端发消息给我
            data=map[fd].recv(1024).decode()
            if not data:
                #客户端退出
                p.unregister(fd)
                map[fd].close()
                del map[fd]
                continue
            print("收到",data)
            map[fd].send(b'ok')


