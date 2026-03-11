#import moduleIsEven
#import Math
import mv #move
import li


##########################
#TODO: IN PROGRESSSSS
##########################


#global var
visitedSet = set()

def seedMaze():
	harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def seedUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		semeia()
	
def harvestUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		harvestTill()

#def firstFree(conj):
	#for i in range(get_world_size()): 
	#	for j in range(get_world_size()): 
	#		if(not ((i,j) in conj)):
	#			return (i,j)
	#return (0,0)

	return (0,0)
	
def firstColumn(conj):
	i = get_pos_x()
	for j in range(get_world_size()): 
		if(not ((i,j) in conj)):
			return (i,j)
	return (0,0)
		
def harvestTill():
	harvest()
	till()
	
def plantaAplanta(planta):
	if get_water() <= 0.9:
		use_item(Items.Water)
	use_item(Items.Fertilizer)
	plant(planta)

def semeia():
	plantas = [Entities.Carrot,Entities.Tree,Entities.Bush,Entities.Grass]
	toPlant = plantas[random()*len(plantas)]
	#print(toPlant)
	#get_entity_type()
	if(toPlant == Entities.Carrot and get_ground_type() == Grounds.Grassland):
		harvest()
		till()
		do_a_flip()
	plant(toPlant)
	#do_a_flip()
	lib.fertilWater()
	
def colheitaRec():
	global visitedSet
	while(True):
		#quick_print(dictMapa)
		companhia = get_companion()
		if(not (companhia == None)):
			planta = companhia[0]  #companhia da planta i,j
			planta_x = companhia[1][0] #
			planta_y = companhia[1][1]
		else:
			planta_x = 0
			planta_y = 0
		#planta = companhia[0]  #companhia da planta i,j
		#planta_x = companhia[1][0] #
		#planta_y = companhia[1][1]
		#if(contains(dickMapa,planta_x,planta_y)):
		if((planta_x,planta_y) in visitedSet):  #CASO MEU TALE JA ESTEJA PLANTADO
			firstFreeRetorno = firstColumn(visitedSet)
			if(firstFreeRetorno == (0,0) or len(visitedSet) == 32*2):
				#mv.moveTo(0,0)
				#mv.moveMap(harvest,harvest)
				#mv.moveTo(0,0)
				#mv.droneInLine(harveste)
				#break
				return
			planta_x = firstFreeRetorno[0]
			planta_y = firstFreeRetorno[1]
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			semeia()
		#quick_print("PLANTA:",planta," X:",planta_x," Y:",planta_y)
		#quick_print("Tamanho dict: ",len(dictMapa))
		#quick_print("MAH DICK: ",dickMapa)
		elif(companhia == None): #CASO NAO TENHA COMPANHIA
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			semeia()
		else:
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			if(get_ground_type() == Grounds.Grassland and planta == Entities.Carrot):
				#harvest()
				till()
				#do_a_flip()
			plant(planta)
					#se tem drone deixa ele colher dali
			if(num_drones() < max_drones()):
				spawn_drone(colheitaRec)
		if(firstColumn(visitedSet) == (0,0) or len(visitedSet) == 32**2):
			#mv.moveTo(0,0)
			#mv.moveMap(harvest)
			#mv.droneInLine(harvestUp)
			#break
			return
	
def colheitaTest():
	mv.droneInLine(harvestUp)
	mv.moveTo(0,0)
	semeia() #planta random no inicio
	global visitedSet
	visitedSet.add((0,0))
	mv.droneInLine(colheitaRec)
	mv.moveTo(0,0)
	mv.droneInLine(harvestUp)

#Use if elem in set: para verificar se o conjunto contém um elemento.

#Use for elem in set: para iterar todos os elementos no conjunto.
#Para conjuntos maiores, o operador in funciona muito mais rápido do que em uma lista.
		
def colheita():
	#mv.moveMap(harvestTill)
	#clear()
	mv.droneInLine(harvestUp)
	mv.moveTo(0,0)
	
	seedMaze()
	#TODO: Change logic to multithread
	
	
	#semeia() #planta random no inicio
	global visitedSet
	#visitedSet = {(0,0):True}

	#visitedSet = set()
	visitedSet.add((0,0))
	
	#global setPositionsOk
	#setPositionsOk = set()
	quick_print(visitedSet)
	quick_print("Length",len(visitedSet))
	quick_print("firstFree",firstFree(visitedSet))


	while(True):
		#quick_print(dictMapa)
		companhia = get_companion()
		if(not (companhia == None)):
			planta = companhia[0]  #companhia da planta i,j
			planta_x = companhia[1][0] #
			planta_y = companhia[1][1]
		else:
			planta_x = 0
			planta_y = 0
		#if(contains(dickMapa,planta_x,planta_y)):
		if((planta_x,planta_y) in visitedSet):  #CASO MEU TALE JA ESTEJA PLANTADO
			firstFreeRetorno = firstFree(visitedSet)
			if(firstFreeRetorno == (0,0) or len(visitedSet) == get_world_size()**2):
				#mv.moveTo(0,0)
				#mv.moveMap(harvest,harvest)
				mv.moveTo(0,0)
				mv.droneInLine(harvestUp)
				return
				#break
			planta_x = firstFreeRetorno[0]
			planta_y = firstFreeRetorno[1]
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			semeia()
			
		#quick_print("PLANTA:",planta," X:",planta_x," Y:",planta_y)
		#quick_print("Tamanho dict: ",len(dictMapa))
		#quick_print("MAH DICK: ",dickMapa)
		elif(companhia == None): #CASO NAO TENHA COMPANHIA
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			semeia()
		else:
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			if(get_ground_type() == Grounds.Grassland and planta == Entities.Carrot):
				#harvest()
				till()
				#do_a_flip()
			plant(planta)
			#se tem drone deixa ele colher dali
			if(num_drones() < max_drones()-3):
				spawn_drone(colheitaRec)
				spawn_drone(colheitaRec)
				spawn_drone(colheitaRec)
			#redirect main drone
			firstFreeRetorno = firstFree(visitedSet)
			mv.moveTo(firstFreeRetorno[0],firstFreeRetorno[1])
			#spawn_drone(plantaUp)
		if(firstFree(visitedSet) == (0,0) or len(visitedSet) == 32**2):
			mv.moveTo(0,0)
			#mv.moveMap(harvest)
			mv.droneInLine(harvestUp)
			#break
			return
clear()
colheita()