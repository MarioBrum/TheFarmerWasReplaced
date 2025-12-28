#import moduleIsEven
#import Math
import mv #move

def firstFree(dick):
	for i in range(get_world_size()): 
		for j in range(get_world_size()): 
			if(not ((i,j) in dick)):
				return (i,j)
	return (0,0)
	
def contains(dick,x,y):
	if ((x,y) in dick):
		return True
	return False
	
#	if(matriz[get_pos_x][get_pos_y] == True):
#		return True
#	else:
#		return False
		
#	for i in range(get_world_size()): 
#		for j in range(get_world_size()): 
#			if(matriz[i][j] == True):
#				return True
#	return False
		
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
	if get_water() <= 0.9:
		use_item(Items.Water)
	use_item(Items.Fertilizer)
		
def colheita():
	mv.moveMap(harvestTill)
	semeia() #planta random no inicio
	dickMapa = {(0,0):True}

	while(True):
		#quick_print(dictMapa)
		companhia = get_companion()
		planta = companhia[0]
		planta_x = companhia[1][0]
		planta_y = companhia[1][1]
		if(contains(dickMapa,planta_x,planta_y)):
			firstFreeRetorno = firstFree(dickMapa)
			if(firstFreeRetorno == (0,0)):
				mv.moveTo(0,0)
				mv.moveMap(harvest,harvest)
				break
			planta_x = firstFreeRetorno[0]
			planta_y = firstFreeRetorno[1]
			mv.moveTo(planta_x,planta_y)
			semeia()
			dickMapa[(planta_x,planta_y)] = True
		#quick_print("PLANTA:",planta," X:",planta_x," Y:",planta_y)
		#quick_print("Tamanho dict: ",len(dictMapa))
			#quick_print("MAH DICK: ",dickMapa)
		elif(companhia == None):
			mv.moveTo(planta_x,planta_y)
			semeia()
			dickMapa[(planta_x,planta_y)] = True
		else:
			mv.moveTo(planta_x,planta_y)
			dickMapa[(planta_x,planta_y)] = True
			if(get_ground_type() == Grounds.Grassland and planta == Entities.Carrot):
				#harvest()
				till()
				#do_a_flip()
			plant(planta)
		if(firstFree(dickMapa) == (0,0)):
			mv.moveTo(0,0)
			mv.moveMap(harvest)
			break
	