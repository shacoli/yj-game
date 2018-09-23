from socket import *
import time 

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST,PORT)

def get_players_number(BUFSIZ, ADDR): #获取玩家的总数
	#return gamer_number 
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	udpSocket.bind(ADDR)
	print('waiting for connection...')
	
	
	#s_Ser= socket(AF_INET, SOCK_STREAM)
	#s_Ser.bind(ADDR)
	#s_Ser.listen(5) #暂时先让5个人玩
	#pnum = 0
	#for i in range(5):
		#print('waiting for connection...')
		#s_Cli, addr = s_Ser.accept() #s先阻塞
		#print('got a connect from:', str(addr))
		#pnum += 1
		#restnum = 5 - pnum
		#for i in s_Cli_list:
			#i.send(("现在已有%d位玩家在房间中等待，还差\
#%d位玩家即可开始"%(pnum, restnum)).encode())
		#if pnum == 5:
			#for i in s_Cli_list:
				#i.send('啊哈！游戏开始！'.encode())
			#break
		#s_Cli.close()
	#s_Ser.close()




get_players_number(BUFSIZ, ADDR)

