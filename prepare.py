from random import shuffle
from socket import *
import time 

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST,PORT)

all_cards = [1,2,3,5,7,11,13,17,19,23\
			,29,31,37,41,43,'a','a','a','b','b'\
			,'b','c','c','c','d','d','d','e','e','e']

def get_players_number(HOST, PORT, BUFSIZ, ADDR): #获取玩家的总数
	#return gamer_number 
	# s= socket(AF_INET, SOCK_STREAM)
	# s.bind(ADDR)
	# s.listen(5) #暂时先让5个人玩
	# while True:
	# 	print('waiting for connection...')
	# 	client, addr = s.accept() #s先阻塞
	# 	print('got a connect from:', str(addr))
	pass

gamers_number = 7 #开始的玩家总数 （这里作为测试使用）

round_in = 0 #回合数

big_treasures = ['hat','hand','sheild','sword','axe'] #5个宝物的大列表

#gaming_list = [] #游戏回合中的牌列表

#gamer_backhome = 0

#gamer_ingame = gamer_number_start - gamer_backhome

def shuffle_all_cards():
	'''洗基础牌 '''  
	return shuffle(all_cards)

def shuffle_big_treasures():
	'''洗宝藏牌 ''' 
	return shuffle(big_treasures)

def put_treasure_in():
	global all_cards
	all_cards.append(big_treasures[0]) #将宝藏第一张塞入基础牌库
	del big_treasures[0] #移除大宝藏排列

def remove_cards(all_cards, trap):
	all_cards.remove(trap)
	all_cards.remove(trap)
	return None

def judge_the_money(i):
	print('你们发现了%d块钱'%i)
	everyone_get = i//gamers_number #每个人分到的钱
	print("每个人分到的钱为：%d"%everyone_get)
	rest_money = i%gamers_number #地板除剩下来的钱
	current_prize_pool[0] += rest_money #默认奖金池列表第一位为钱总数，及剩下的余钱
	print("这一步剩下的钱：%d"%rest_money)
	print('奖金池现在省下的钱有：%d'%current_prize_pool[0])
	return None

def judge_the_traps(i):
	if i == 'a':
		print('你们遇到了眼睛蛇陷阱')
	elif i == 'b':
		print('你们遇到了火焰陷阱')
	elif i == 'c':
		print('你们遇到了蜘蛛陷阱')
	elif i == 'd':
		print('你们遇到了僵尸陷阱')
	elif i == 'e':
		print('你们遇到了坠石陷阱')
	return None

def judge_the_treasure(i):
	if i == 'hat':
		print('你们发现了巫师之帽')
	elif i == 'hand':
		print('你们发现了神王手套')
	elif i == 'sheild':
		print('你们发现了辉铜之盾')
	elif i == 'sword':
		print('你们发现了刺血弯刀')
	elif i == 'axe':
		print('你们发现了镶钻金斧')
	return None

def whether_continue(current_prize_pool,gamers_number):
	#get_rest_players_number 先获得玩家数量
	players_leave = get_leave_players_number() #先获取剩余继续玩家的数量
	gamers_number -= players_leave
	print('有%d位玩家离开了游戏'%players_leave)
	money_they_take_away = current_prize_pool[0]//players_leave
	print('%d位玩家分得了%d块钱'%(gamers_number, money_they_take_away))
	current_prize_pool[0] = current_prize_pool[0]%players_leave
	print('还有%d块钱没有被拿走'%current_prize_pool[0])
	return gamers_number


def who_owns_the_treasure():
	pass

def get_map():
	'''第一回合'''
	global gaming_list
	gaming_list = [] #游戏回合中的牌列表
	global all_cards
	shuffle_big_treasures() #洗宝藏牌
	put_treasure_in()#将宝藏牌洗入牌库
	#print(big_treasures)
	shuffle_all_cards() #加入一个宝藏后再洗基础牌库
	#print(all_cards)
	for i in all_cards: #将本局地图率先导出
		gaming_list.append(i)
		if gaming_list.count('a') == 2: #判定陷阱 眼镜蛇
			#print(gaming_list)
			remove_cards(all_cards, 'a')
			#print(all_cards)
			break
		elif gaming_list.count('b') == 2: #判定陷阱 火焰
			#print(gaming_list)
			remove_cards(all_cards, 'b')
			#print(all_cards)
			break
		elif gaming_list.count('c') == 2: #判定陷阱 蜘蛛
			#print(gaming_list)
			remove_cards(all_cards, 'c')
			#print(all_cards)
			break
		elif gaming_list.count('d') == 2: #判定陷阱 僵尸
			#print(gaming_list)
			remove_cards(all_cards, 'd')
			#print(all_cards)
			break
		elif gaming_list.count('e') == 2: #判定陷阱 坠石
			#print(gaming_list)
			remove_cards(all_cards, 'e')
			#print(all_cards)
			break

def get_leave_players_number():
	try:
		remain = input('请输入离开游戏的人的个数\n') #之后替换成别的
		return int(remain) #玩家数量 测试用
	except ValueError:
		print('输入错误，请输入恰当的整数！')
		return get_leave_players_number()
	
class Player(object):
	__slots__ = ['name','address','money_owned','temp_money']
	def __init__(self, name, address, money_owned, temp_money):
		self.name = name
		self.address = addresss
		self.money_owned = money_owned
		self.temp_money = temp_money

	def leave(money_owned):
		pass

	def go_on(tmp_money):
		pass

if __name__ == '__main__':
	
	for a in range(5):

		print('第%d回合开始'%(a+1))

		current_prize_pool = [0,] #申明奖金池列表
	
		one_turn_number = gamers_number

		get_map()
		#get_map()
		#get_map()
		#get_map()
		#get_map()
		print(all_cards)
		print(gaming_list)
		for i in gaming_list:
			if one_turn_number <= 0:
				break
			elif type(i) == type(1): #判断是否是钱
				judge_the_money(i)
				one_turn_number = whether_continue(current_prize_pool,one_turn_number) # 进行下去的方法
			elif len(i) == 1: #判断是否陷阱
				judge_the_traps(i) #判断陷阱种类
				one_turn_number = whether_continue(current_prize_pool,one_turn_number) # 进行下去的方法
			elif len(i) > 1: #判断是否宝物
				judge_the_treasure(i) #判断宝物种类
				one_turn_number = whether_continue(current_prize_pool,one_turn_number) # 进行下去的方法
				who_owns_the_treasure() # 判断宝物归谁
			
		print('第%d回合结束'%(a+1))
