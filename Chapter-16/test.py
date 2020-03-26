import socket

server = socket.socket() # 使用socket模块，创建server对象

server.bind(('192.168.1.102',8080)) # 绑定服务端的IP和端口 

server.listen(99) # 开始监听，最大监听数99个

print('start listen')

while True:
    conversation,ip_address = server.accept() #服务器接收请求，返回接收内容和客户端的IP
    print('show client ip',ip_address) # 打印客户端的IP
    recv_data = conversation.recv(1024) # 设置会话内容的缓存大小，而且内容是二进制
    print(recv_data.decode('utf-8')) # 将二进制的会话解码成utf-8格式

    message = input('>>>:')
    conversation.send(message.encode('utf-8')) # 将会话方式编码成二进制传给客户端
    conversation.close() # 关闭会话













