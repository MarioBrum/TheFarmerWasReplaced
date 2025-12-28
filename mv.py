def moveMap(func1):
#def moveMap()
	for i in range(get_world_size()):
			for j in range(get_world_size()):
				#if(j < get_world_size()):
					#act
					moveTo(i,j)
					func1()
					
			#moveVerticalBack()		
			#act	
			#func2()	
def moveVerticalBack():
#def moveVerticalBack(#act)
	for i in range(get_world_size()):
			#act
			move(South)		

def moveHorizontalBack():
#def moveVerticalBack(#act)
	for i in range(get_world_size()):
			#act
			move(West)		
			
def nothing():
	pass			
	
def moveTo(x,y):
	tam = get_world_size()
	while(not(get_pos_x()== x and get_pos_y() == y)):
		if(get_pos_x() >= x and get_pos_x() >= tam/2 and (abs(get_pos_x()-x) > tam/2)):
			move(East)
		elif(get_pos_x() < x and get_pos_x() < tam/2 and (abs(get_pos_x()-x) > tam/2)):
			move(West)
		elif(get_pos_y() >= y and get_pos_y() >= tam/2 and (abs(get_pos_y()-y) > tam/2)):
			move(North)
		elif(get_pos_y() < y and get_pos_y() < tam/2 and (abs(get_pos_y()-y) > tam/2)):
			move(South)	
		elif(get_pos_x() < x):
			move(East)
		elif(get_pos_x() > x):
			move(West)
		elif(get_pos_y() < y):
			move(North)
		elif(get_pos_y() > y):
			move(South)
#clear()
#moveTo(0,22)

def goToAndDrone(i,j,func):
	x = get_pos_x()
	y = get_pos_y()
	moveTo(i,j)
	spawn_drone(func)
	moveTo(x,y)
	
def droneInLine(func):
	for i in range(0,get_world_size()):
		moveTo(i,0)
		if(num_drones() < max_drones()):
			spawn_drone(func)
		else:
			func()
			
def droneInColumn(func):
	for i in range(0,get_world_size()):
		moveTo(0,i)
		if(num_drones() < max_drones()):
			spawn_drone(func)
		else:
			func()
		
def example():
	x = get_pos_x()
	for i in range(0,get_world_size()):
		moveTo(x,i)
		harvest()
		till()
		
def colheita():
	for i in range(get_world_size()):
		if(num_drones() < max_drones()):
			goToAndDrone(i,0,example)
		else:
			goToAndDrone(i,0,example)
#clear()		
#colheita()
#droneInLine(example)
	