import mv
import lib

def set():
	harvest()
	till()

def colheita():
	clear()
	#mv.moveMap(set)
	#mv.moveTo(0,0)
	change_hat(Hats.Dinosaur_Hat)
	#mv.moveTo(0,0)
	count = 0
	while(count < 30):
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if(get_entity_type() == Entities.Apple):
					count+=1
				if(i%2==0):
					mv.moveTo(i,j)
				else:
					move(South)
			move(East)
		for i in range(get_world_size()):
			move(West)
			move(South)
	change_hat(Hats.Traffic_Cone)

#colheita()
	