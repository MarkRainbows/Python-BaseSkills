"""__author__ = 余婷"""
import socket
from threading import Thread


class ConversationThread(Thread):
    def __init__(self, conversation, addr):
        super().__init__()
        self.conversation = conversation
        self.addr = addr

    def run(self):
        while True:
            message = self.conversation.recv(1024).decode('utf-8')
            print(self.addr, ': ' + message, sep='')


server = socket.socket()
server.bind(('10.7.187.149', 9001))
server.listen(512)
while True:
    conversation, addr = server.accept()

    # 给服务器发送请求的客户端建立的连接创建一个子线程。在子线程中去处理每个请求
    t = ConversationThread(conversation, addr)
    t.start()
