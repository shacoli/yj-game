from socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
#连接监听socket
s.connect(("localhost",8080))
#接受服务端socket发送的信息
tm = s.recv(1024)
msg = tm.decode('utf-8')
print(msg)
if msg == '啊哈！游戏开始！':
	s.close()
	break
s.close()