import lib
import mv #move

def harvestTill():
	harvest()
	#till()
	lib.fertilWater()
	plant(Entities.Tree)
	
def justHarvest():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		harvest()
	
def seedUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		if(lib.isEven(j)):
			if(lib.isEven(i)):
				mv.moveTo(i,j)
				harvestTill()
		else:
			if(not lib.isEven(i)):
				mv.moveTo(i,j)
				harvestTill()
			
def colheita():
	mv.droneInLine(seedUp)
	mv.moveTo(0,0)
	mv.droneInLine(justHarvest)

	