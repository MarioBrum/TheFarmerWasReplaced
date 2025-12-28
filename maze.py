import mv
import lib
import graphi

def seedMaze():
	harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def recursive(dickMapa,t_x,t_y):
	x = get_pos_x()
	y = get_pos_y()
	if(y > t_y and can_move(East)):
		pass
	elif(can_move(West)):
		pass
	elif(can_move(North)):
		pass
	elif(can_move(South)):
		pass

#def makeGraph():
	#dickMapa = {(0,0):True}
	#for i in range(0,max_drones()):
	#	i = i
	#return dickMapa

	
def colheita():
	dickMapa = {(0,0):True}
	#dickMapa = makeGraph()
	seedMaze()
	graphi.makeGraph()
	#TODO: Se nao tá no dicionario e nao é tesouro entao adiciona 
	# Se pode se mover e não tá no dicionario, move e add numa lista de caminho atual
	# essa lista tem que ter quais movimentos foram usados (?), prov nao posso usar mv.moveTo
	# nos mazes #backtrack??? THATS IT?
	# Se chega num ponto de "cant move", adiciona o caminho todo ao dicionario e volta ao
	# ponto inicial do caminho (?)
	##DICIONARIO VAI SER A MATRIZ DE CAMINHO, ONDE TIVER TRUE, PODE IR CAMINHAR
	
	#for i in range(get_world_size()):
		#for j in range(get_world_size()):
			#dickMapa(i,j) = False
			#pass
	treasure = False
	#while(len(dickMapa < get_world_size() or not(treasure)):
	#treasure x,y
	#t_x, t_y = measure()
	t_y = 0
	while(not(treasure)):
		x = get_pos_x()
		y = get_pos_y() 
		if(can_move(East) and y-t_y):
			pass
		elif(can_move(West)):
			pass
		elif(can_move(North)):
			pass
		elif(can_move(South)):
			pass
	seedMaze()
	#use_item(Items.Weird_Substance,32)
	#substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	#use_item(Items.Weird_Substance, substance)
	

#clear()
#colheita()

#treasure 4,4

#actual 0,0

#se y > t_y and can_move(East)
	#move(East)

#se y > t_y and can_move(East)
	#move(East)
#5,0 5,1 5,2 5,3 5,4 5,5
#4,0 4,1 4,2 4,3 4,4 4,5
#3,0 3,1 3,2 3,3 3,4 3,5
#2,0 2,1 2,2 2,3 2,4 2,5
#1,0 1,1 1,2 1,3 1,4 1,5
#0,0 0,1 0,2 0,3 0,4 0,5