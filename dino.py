import mv
import lib
global finish

def moveDino(x,y):
	while(not(get_pos_x()== x and get_pos_y() == y)):
		if(get_pos_x() < x):
			if(not move(East)):
				change_hat(Hats.Traffic_Cone)
				finish = True
			move(East)
		elif(get_pos_x() > x):
			if(not move(West)):
				change_hat(Hats.Traffic_Cone)
				finish = True
			move(West)
		elif(get_pos_y() < y):
			if(not move(North)):
				change_hat(Hats.Traffic_Cone)
				finish = True
			move(North)
		elif(get_pos_y() > y):
			if(not move(South)):
				change_hat(Hats.Traffic_Cone)
				finish = True
			move(South)
			
def moveLeft(size):
	
	pass
def moveRight(size):
	pass
	
##TODO: Pode ser um dicionario que toda vez que passa por um elemento
##bota no dicionario, ou uma lista de posicoes e nao pode passar pela 
##mesma posicao, parece melhor a lista tem que ter o tamanho da cauda
	
def colheita():
	clear()
	change_hat(Hats.Dinosaur_Hat)
	count = 0
	#nroCauda = (get_world_size()**2) -1 ##-2? sei la 1024 -1
	nroCauda = 1000
	tam = get_world_size()#32
	#dangerZone = tam
	finish = False
	while(count < nroCauda and not finish):
		x, y = measure()
		dangerZone = count//tam
		if(count > tam and y >= tam-dangerZone):
			#TODO RIGHT TURN
			#moveRight()
			pass
		elif(count > tam and y <= dangerZone):
			#TODO LEFT TURN
			#moveRight()
			pass
		if(count >= nroCauda):
			finish = True
		moveDino(x,y)
	change_hat(Hats.Traffic_Cone)

#colheita()
	