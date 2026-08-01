#import moduleIsEven
#import Math
import mv #move
import lib

##########################
#TODO: IN PROGRESSSSS
##########################

#global var
visitedSet = set()
find = False

def seedMaze():
	harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	
def harvestTill():
	harvest()
	till()
		
def harvestUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		harvestTill()

#TODO: Method to find a new not visited position	
#In case have more options and have drones, put more drones to move
#around all options
def goToFree(conj):
	global visitedSet
	global find
	x = get_pos_x()
	y = get_pos_y()
	if(find):
		return True
	if(get_entity_type() == Entities.Treasure):
		quick_print("achei")
		harvest()
		find = True
		return True
	canNorth = False #x+1,j
	canSouth = False #x-1,j
	canWest = False #x,j-1
	canEast = False #x,j+1
	lName = [North,South,West,East]
	l = [False,False,False,False]
	moves = 0
	if(can_move(North) and (not ((x+1,y) in conj))):
		#canNorth = True
		l[0] = True
		moves+= 1
	if(can_move(South) and (not ((x-1,y) in conj))):
		#canSouth = True
		l[1] = True
		moves+= 1
	if(can_move(West) and (not ((x,y-1) in conj))):
		#canWest = True
		l[2] = True
		moves+= 1
	if(can_move(East) and (not ((x,y+1) in conj))):
		#canSouth = True
		l[3] = True
		moves+= 1
	if(moves == 0 or (len(visitedSet) == get_world_size()**2)):
		return False
	elif(moves >= 2):
		i = 0
		while(moves >=2 and i <= 3):
			if(l[i]):
				#move(lName[i])
				if(i == 0):
					visitedSet.add(((x+1,y)))
					move(North)
				if(i == 1):
					visitedSet.add(((x-1,y)))
					move(South)
				if(i == 2):
					visitedSet.add(((x,y+1)))
					move(West)
				if(i == 3):
					visitedSet.add(((x,y-1)))
					move(East)
				spawn_drone(goToFreeRec)
				moves-=1
			i+=1
		return 
	elif(moves == 1):
		if(l[1]):
			move(North)
			visitedSet.add(((x+1,y)))
			goToFreeRec()
			return 
		elif(l[2]):
			move(South)
			visitedSet.add(((x-1,y)))
			goToFreeRec()
		elif(l[3]):
			move(West)
			visitedSet.add(((x,y-1)))
			goToFreeRec()
			return 
		else:
			move(East)
			visitedSet.add(((x,y+1)))
			goToFreeRec()
			return 
	else:
		return True#impossible?
	
def goToFreeRec():
	global visitedSet
	global find
	x = get_pos_x()
	y = get_pos_y()
	if(find):
		#break
		quick_print("Foundrec local")
		#clear()#
		return True
	if(get_entity_type() == Entities.Treasure or find):
		#quick_print("achei local")
		harvest()
		find = True
		#quick_print("FIND", find)
		#clear()
		return True
	canNorth = False #x,j+1
	canSouth = False #x,j-1
	canWest = False #x-1,j
	canEast = False #x+1,j
	lName = [North,South,West,East]
	l = [False,False,False,False]
	moves = 0
	quick_print("size dict: ",len(visitedSet))
	quick_print("did find?: ",find)
	if(can_move(North) and (not ((x,y+1) in visitedSet))):
		#canNorth = True
		l[0] = True
		moves+= 1
	if(can_move(South) and (not ((x,y-1) in visitedSet))):
		#canSouth = True
		l[1] = True
		moves+= 1
	if(can_move(West) and (not ((x-1,y) in visitedSet))):
		#canWest = True
		l[2] = True
		moves+= 1
	if(can_move(East) and (not ((x+1,y) in visitedSet))):
		#canSouth = True
		l[3] = True
		moves+= 1
	if(moves == 0 or (len(visitedSet) == get_world_size()**2) or find):
		if(find):
			find = true
		#find = True
		return False
	if(find): 
		return True
	elif(moves >= 2):
		i = 0
		while(moves >=2 and i <= 3):
			if(l[i]):
				#move(lName[i])
				if(i == 0):
					visitedSet.add((x,y+1))
					move(North)
					if(num_drones() >= 1 and (not find)):
						spawn_drone(goToFreeRec)
						move(South)
					else:
						goToFreeRec()
						return
				if(i == 1):
					visitedSet.add((x,y-1))
					move(South)
					if(num_drones() >= 1 and (not find)):
						spawn_drone(goToFreeRec)
						move(North)
					else:
						goToFreeRec()
						return
				if(i == 2):
					visitedSet.add((x-1,y))
					move(West)
					if(num_drones() >= 1 and (not find)):
						spawn_drone(goToFreeRec)
						move(East)
					else:
						goToFreeRec()
						return
				if(i == 3):
					visitedSet.add(((x+1,y)))
					move(East)
					if(num_drones() >= 1 and (not find)):
						spawn_drone(goToFreeRec)
						move(West)
					else:
						goToFreeRec()
						return

				#moves-=1
			i+=1
		return 
	elif(moves == 1):
		if(l[0]):
			visitedSet.add(((x,y+1)))
			move(North)
			goToFreeRec()
			return 
		elif(l[1]):
			visitedSet.add(((x,y-1)))
			move(South)
			goToFreeRec()
			return 
		elif(l[2]):
			visitedSet.add(((x-1,y)))
			move(West)
			goToFreeRec()
		else:
			visitedSet.add(((x+1,y)))
			move(East)
			goToFreeRec()
			return 
	else:
		return True#impossible?

#Use if elem in set: para verificar se o conjunto contém um elemento.

#Use for elem in set: para iterar todos os elementos no conjunto.
#Para conjuntos maiores, o operador in funciona muito mais rápido do que em uma lista.
		
def colheita():
	mv.droneInLine(harvestUp)
	mv.moveTo(0,0)
	
	seedMaze()
	global visitedSet
	global find
	#visitedSet = {(0,0):True}
	#visitedSet = set()
	visitedSet.add((0,0))
	
	#global setPositionsOk
	#setPositionsOk = set()
	#quick_print(visitedSet)
	#quick_print("Length",len(visitedSet))
	#quick_print("firstFree",firstFree(visitedSet))
	
	while(len(visitedSet) < get_world_size()**2):
		if(not find):
			goToFreeRec()
		else: 
			return
	clear()#
#
#clear()
#colheita()

