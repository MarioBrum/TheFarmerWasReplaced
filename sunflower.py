import lib
import mv #move

def harvestTill():
	harvest()
	till()
	plant(Entities.Sunflower)
	#lib.fertilWater()
			
def colheita():
	mv.moveMap(harvestTill)
	#l = [15,14,13,12,11,10,9,8,7]
	collected = 0
	petels = 15
	while(collected < get_world_size()*2 or petels >= 7):
		#hasMaxPetels = False
		#collected < get_world_size()*2
		for i in range(get_world_size()):
				for j in range(get_world_size()):
					mv.moveTo(i,j)
					if(measure() == petels):
						harvest()
						collected+=1
						#plant(Entities.Sunflower)
						#hasMaxPetels = True
		petels-=1
				
		#if(not hasMaxPetels):
			#break
	#mv.moveMap(harvestTill,harvestTill)
	#moveTo(0,0)
	#harvest()
	
#clear()
#mv.moveMap(till,till)
#while(True):
#	colheita()