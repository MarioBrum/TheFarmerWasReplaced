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
	harvest()
	till()
	plant(Entities.Cactus)

def sortingInX(x):
	###FOR DEGUG
	#l =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#mv.moveTo(0,0)
	#for i in range(get_world_size()):
	#	mv.moveTo(i,0)
	#	l[i] = measure()
	
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
	
def sortingInY(y):
	###FOR DEGUG
	#l =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	#mv.moveTo(0,0)
	#for i in range(get_world_size()):
	#	mv.moveTo(i,0)
	#	l[i] = measure()
	
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
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			mv.moveTo(i,j)
			seedCactus()
	for i in range(get_world_size()):
		sortingInY(i)
		#quick_print("Sorting OK in y: ", i)
	quick_print("All Y sorted")
	
	for i in range(get_world_size()):
		sortingInX(i)
		#quick_print("Sorting OK in y: ", i)
	quick_print("All X sorted")
	
	#for i in range(get_world_size()):
	#	mv.moveTo(0,i)
	#	harvest()
	
	mv.moveTo(get_world_size()-1,get_world_size()-1)	
	harvest()