##### TO DO: 
#### Remover comentarios desnecessarios
#### Fazer labirintos
####




#5,0 5,1 5,2 5,3 5,4 5,5
#4,0 4,1 4,2 4,3 4,4 4,5
#3,0 3,1 3,2 3,3 3,4 3,5
#2,0 2,1 2,2 2,3 2,4 2,5
#1,0 1,1 1,2 1,3 1,4 1,5
#0,0 0,1 0,2 0,3 0,4 0,5


#to no 5.1
#quero ir pro 0.2

#se currentX > x and currentX > tam/2 and (abs(currentX- x) > tam/2 )
	#move North
	
#to no 0.2
#quero ir pro 5.1	
#se currentX < x and currentX < tam/2
	#move East
	
print(abs(10-20))






clear()
mv.moveMap(harvestTill,harvestTill)
#mv.moveMap(till,till)
while(True):
	allItemsName = ["Hay","Wood","Carrot","Pumpkin","Cactus","Weird_Substance","Gold"]
	allItems = [Items.Hay,Items.Wood,Items.Carrot,Items.Pumpkin,Items.Cactus,Items.Weird_Substance,Items.Gold]
	allItemsBefore = [0,0,0,0,0,0,0]
	for i in range(len(allItems)):
		allItemsBefore[i] = num_items(allItems[i])
	#quick_print("Hay: ",num_items(Items.Hay),"Wood: ",num_items(Items.Wood),"Carrots: ",num_items(Items.Carrot))
	tempoInicio = get_time()
	colheita()
	tempoFinal = abs(tempoInicio-get_time())
	allItemsFinal = [0,0,0,0,0,0,0]
	for i in range(len(allItems)):
		allItemsFinal[i] = abs(num_items(allItems[i])-allItemsBefore[i])
		quick_print("Earned items: ")
		quick_print(allItemsName[i],": ",allItemsFinal[i])
		#quick_print(allItemsName[i],num_items(allItems[i]))
	quick_print("Time passed: ",tempoFinal)
	quick_print("#############################")
		
	
	
def sortingInY(y):
	l =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	mv.moveTo(0,0)
	for i in range(get_world_size()):
		mv.moveTo(i,0)
		l[i] = measure()
	
	#retorno = False
	haveChange = True
	while(haveChange):
		change = False
		for i in range(get_world_size()-1):
			#quick_print("Lista: ", l)
			mv.moveTo(i,y)
			if not(measure() >= measure(East)):
				swap(East)
				aux = l[i+1]
				l[i+1] = l[i]
				l[i] = aux
				change = True
				#haveChange = True
		if(not(change)):
			haveChange = not haveChange		
	
	