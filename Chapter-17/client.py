"""__author__ = 余婷"""
import socket

client = socket.socket()
client.connect(('10.7.187.149', 9000))
while True:
    message = input('自己:')
    client.send(message.encode('utf-8'))