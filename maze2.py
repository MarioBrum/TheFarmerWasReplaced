import mv
import lib

def containsList(l,item):
	for i in range(len(l)):
		if(l[i] == item):
			return True
	return False

#1,2,3,4
#^ < > v
def gira(positions, lado):
	if(positions[North] == North and lado == "esq"):
		resultado = {North:West, East:North, West:South, South:East}
		return resultado
	elif (positions[North] == North and lado == "dir"):
		pass

		
def seedMaze():
	harvest()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def recursive():
	x = get_pos_x()
	y = get_pos_y()
	#Norte Sul Leste Oeste
	#posicoes =  cima  baixo esq  dir 
	positions = {North:North, East:East, West:West, South:South}
	#positionsEsq = {North:West, East:North, West:South, South:East}
	#positionsBaixo = {North:South, East:West, West:East, South:North}
	#positionDir = {North:East, East:South, West:North, South:West}
	if(get_entity_type() == Entities.Treasure):
		harvest()
	else:
		pass
def colheita():
	#dickMapa = {(0,0):True}
	seedMaze()
	#treasure x,y
	#t_x, t_y = measure()
	l = []
	a = []
	#l.append((get_pos_x(),get_pos_y()))
	#a.append("North")
	while(True):
		recursive() 
	
#				_     
#		 |x  x| x x  
#                 -   
#north south west west

#       _             _         _ 
# |x|  |x  |x    ### |x|  |x|  |x   
#           -              -    -
#north south north   vira north east
#					 north 
# _                -
# x|  x|     ###   x|       
#     -            -
#south west     vira north 
# -
# x  
# -
#west
#clear()
colheita()

#treasure 4,4

#actual 0,0

#se y > t_y and can_move(East)
	#move(East)

#se y > t_y and can_move(East)
	#move(East)
#5,0 5,1 5,2 5,3 5,4 5,5
#4,0 4,1 4,2 4,3 4,4 4,5
#3,0 3,1 3,2 3,3 3,4 3,5
#2,0 2,1 2,2 2,3 2,4 2,5
#1,0 1,1 1,2 1,3 1,4 1,5
#0,0 0,1 0,2 0,3 0,4 0,5