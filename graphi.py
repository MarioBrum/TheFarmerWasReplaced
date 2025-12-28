import lib
#global nodes = []

def recursive():
	moves = [West,East,North,South]
	if(get_entity_type == Entities.Treasure):
		harvest()
		return True
	i = lib.rnd(4)
	if(can_move(moves[i])):
		move(moves[i])
		recursive(dickMapa)
	else:
		spawn_drone(recursive())

def explore():
	t_x,t_x = measure()
	#dickMapa = {(0,0):True}
	#move
	recursive()
	

def makeGraph():
	dickMapa = {(0,0):True}
	for i in range(0,max_drones()):
		spawn_drone(explore())
	return dickMapa

#def run():
	#while(len(nodes) <)
		