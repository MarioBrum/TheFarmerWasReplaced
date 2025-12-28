#import moduleIsEven
#import Math
import mv #move
import lib
		
def plantPumpkim():
	harvest()
	till()
	plant(Entities.Pumpkin)	
	lib.fertilWater()
	while(get_entity_type() != Entities.Pumpkin):
		#harvest()
		#till()
		plant(Entities.Pumpkin)	
		lib.fertilWater()
		lib.delay(5000)

def seedUp():
	j = get_pos_x()
	for i in range(0,get_world_size()):
		mv.moveTo(i,j)
		plantPumpkim()
			
def colheita():
	mv.droneInLine(seedUp)
	mv.moveTo(0,0)
	while(num_drones() > 1):
		continue
	#lib.delay(10000)
	harvest()
			
def colheitaDeprecated():
	#mv.moveMap(harvestTill)
	for i in range(get_world_size()):
			for j in range(get_world_size()):
				#move(East)
				#if get_water() <= 0.9:
				#	use_item(Items.Water)
				mv.moveTo(i,j)
				plantPumpkim()
				#if(get_pos_x() == get_world_size() and get_pos_y() == get_world_size()):
					#plantPumpkim()
					
	#moveTo(0,0)
	harvest()
	
#clear()
#mv.moveMap(till,till)
#while(True):
#	colheita()