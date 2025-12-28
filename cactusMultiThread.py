import lib
import mv #move

def canCatch():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			mv.moveTo(i,j)
			if(not(can_harvest())):
				return False
	return True

def seedCactus():
	if(can_harvest()):
		harvest()
	#lib.delay(3000)
	lib.fertilWater()
	if(get_ground_type() != Grounds.Soil):
		till()
	#lib.delay(3000)
	plant(Entities.Cactus)
def seedCactusUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		seedCactus()

def sortingInX():
	x = get_pos_x()
	###FOR DEGUG
	#l =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#mv.moveTo(0,0)
	#for i in range(get_world_size()):
	#	mv.moveTo(i,0)
	#	l[i] = measure()
	bool = True
	allGrow = True
	while(bool):
		for i in range(0,get_world_size()):
			if(not can_harvest()):
				allGrow = False
			mv.moveTo(x,i)
		
		if(allGrow):
			bool = False
		allGrow = True
	#retorno = False
	haveChange = True
	tam = get_world_size()
	j=0
	while(haveChange):
		change = False
		i = 0 
		count = 1 + j
		##MUDAR LAÇO? ANTES ERA  while(i < tam-count
		##
		while(i < tam-count and haveChange): 
			#quick_print("Lista: ", l)
			mv.moveTo(x,i)
			if not(measure() <= measure(North)):
				swap(North)
				#aux = l[i+1]
				#l[i+1] = l[i]
				#l[i] = aux
				change = True
				#haveChange = True
			i+=1
		j+=1
		if(not(change)):
			haveChange = not haveChange
	
def sortingInY():
	###FOR DEGUG
	#l =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#mv.moveTo(0,0)
	#for i in range(get_world_size()):
	#	mv.moveTo(i,0)
	#	l[i] = measure()
	y = get_pos_y()
	bool = True
	allGrow = True
	while(bool):
		for i in range(0,get_world_size()):
			if(not can_harvest()):
				allGrow = False
			mv.moveTo(i,y)
		
		if(allGrow):
			bool = False
		allGrow = True
	#retorno = False
	haveChange = True
	tam = get_world_size()
	j = 0
	while(haveChange):
		change = False
		#i = 0
		i = 0 
		count = 1 +j
		while(i < tam-count and haveChange):
			#quick_print("Lista: ", l)
			mv.moveTo(i,y)
			#quick_print(i,y)
			if not(measure() <= measure(East)):
				swap(East)
				#aux = l[i+1]
				#l[i+1] = l[i]
				#l[i] = aux
				change = True
				#haveChange = True
			i+=1
		j+=1	
		if(not(change)):
			haveChange = not haveChange		

def colheita():
	#mv.moveMap(seedCactus,seedCactus)
	#mv.droneInLine(seedCactus)
	mv.droneInLine(seedCactusUp)
	#while(num_drones() >= 1):
	#	continue
	mv.moveTo(0,0)
	mv.droneInLine(sortingInX)
	quick_print("All X sorted")
	mv.droneInColumn(sortingInY)
	quick_print("All Y sorted")
	
	#for i in range(get_world_size()):
	#	mv.moveTo(0,i)
	#	harvest()
	while(num_drones() > 1):
		continue
	mv.moveTo(get_world_size()-1,get_world_size()-1)	
	harvest()

#colheita()