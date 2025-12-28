#import moduleIsEven
#import Math
import mv #move
import lib

def delay(n):
	aux = get_tick_count()
	while(abs(get_tick_count()-aux) <n):
		pass
		
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
		delay(5000)

def harvestTill():
	harvest()
	till()
	plant(Entities.Pumpkin)
			
def colheita():
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