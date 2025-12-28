import mv
import lib

def seed():
	harvest()
	till()
	plant(Entities.Carrot)
	
def seedUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		seed()
	
def harvestUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		harvest()

def colheita():
	#mv.moveMap(seed)
	#mv.moveMap(harvest)
	mv.droneInLine(seedUp)
	mv.moveTo(0,0)
	while(num_drones() > 1):
		continue
	#lib.delay(10000)
	mv.droneInLine(harvestUp)
	#harvest()