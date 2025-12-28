import mv
import lib

def seed():
	harvest()
	till()
	plant(Entities.Carrot)
	
def colheita():
	mv.moveMap(seed)
	mv.moveMap(harvest)