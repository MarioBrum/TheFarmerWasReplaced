import lib
import mv #move

def harvestTill():
	harvest()
	till()
	lib.fertilWater()
	plant(Entities.Sunflower)
	
def seedUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		harvestTill()

def collect15():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 15):
			harvest()
		count+=1
	return count

def collect14():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 14):
			harvest()
		count+=1
		#mv.moveTo(i,y)
	return count

def collect13():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 13):
			harvest()
		count+=1
		#mv.moveTo(i,y)
	return count
	
def collect12():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 12):
			harvest()
		count+=1
		#mv.moveTo(i,y)
	return count

def collect11():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 11):
			harvest()
		count+=1
		#mv.moveTo(i,y)
	return count

def collect10():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 10):
			harvest()
		count+=1
		#mv.moveTo(i,y)
	return count

def collect9():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 9):
			harvest()
		count+=1
		#mv.moveTo(i,y)
	return count

def collect8():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		if(measure() == 8):
			harvest()
		count+=1
		#mv.moveTo(i,y)
	return count

def collect7():
	y = get_pos_y()
	count = 0
	for i in range(0,get_world_size()):
		mv.moveTo(i,y)
		harvest()
		count+=1
		#mv.moveTo(i,y)
	return count
			
def colheita():
	mv.droneInLine(seedUp)
	mv.droneInColumn(collect15)
	mv.droneInColumn(collect14)
	mv.droneInColumn(collect13)
	mv.droneInColumn(collect12)
	mv.droneInColumn(collect11)
	mv.droneInColumn(collect10)
	mv.droneInColumn(collect9)
	mv.droneInColumn(collect8)
	mv.droneInColumn(collect7)
