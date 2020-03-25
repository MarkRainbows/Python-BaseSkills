import socket


# 1 创建套接字对象
# 这里的socket()  默认包含 ipv4  和 tcp协议
server = socket.socket()
# 绑定ip 端口
server.bind(('10.7.187.121', 8080))
# 开始监听
server.listen(100)


while True:

    conversation, addr = server.accept()
    print('已接收', addr)






