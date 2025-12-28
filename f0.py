# 1. ESTADO GLOBAL: A direção que o robô está "olhando"
# Inicializamos o drone olhando para o Norte.
current_heading = North 

# Mapeamento para rotações (Sentido Horário)
RIGHT_TURN = {North: East, East: South, South: West, West: North}
LEFT_TURN = {North: West, West: South, South: East, East: North}
BACK_TURN = {North: South, East: West, South: North, West: East}

def get_relative_direction(relative):
	#"""Retorna a direção absoluta para uma direção relativa (Frente, Direita, etc)."""#
	if relative == "FRONT":
		return current_heading
	elif relative == "RIGHT":
		return RIGHT_TURN[current_heading]
	elif relative == "LEFT":
		return LEFT_TURN[current_heading]
	elif relative == "BACK":
		return BACK_TURN[current_heading]
	return current_heading # Padrão
	
def can_move_relative(relative):
	#"""Verifica se é possível mover na direção relativa (Frente, Direita, etc)."""
	absolute_dir = get_relative_direction(relative)
	# Assumimos que o can_move original ainda funciona com North/South/East/West
	return can_move(absolute_dir)

def turn_right():
	#"""Simula o drone virando 90 graus à direita e atualiza o heading."""
	global current_heading
	current_heading = RIGHT_TURN[current_heading]

def turn_left():
	#"""Simula o drone virando 90 graus à esquerda e atualiza o heading."""
	global current_heading
	current_heading = LEFT_TURN[current_heading]

def turn_back():
	#"""Simula o drone virando 180 graus e atualiza o heading."""
	global current_heading
	current_heading = BACK_TURN[current_heading]

def move_forward():
	#"""Move na direção atual do heading."""
	move(current_heading)


# --- FUNÇÃO PRINCIPAL DE NAVEGAÇÃO (Regra da Mão Direita) ---

def seedMaze():
	# ... (Seu código original de setup)
	harvest()
	plant(Entities.Bush)
	#substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 2)
	use_item(Items.Weird_Substance, substance)
	
def colheita():
	global current_heading # Deve acessar a variável global para manter o estado

	if get_entity_type() == Entities.Treasure:
		harvest()
		return

	# REGRA DA MÃO DIREITA: Prioridade de movimento
	
	# 1. TENTAR VIRAR À DIREITA
	if can_move_relative("RIGHT"):
		turn_right()
		move_forward()
		colheita()
		
	# 2. TENTAR SEGUIR EM FRENTE
	elif can_move_relative("FRONT"):
		move_forward()
		colheita()
		
	# 3. TENTAR VIRAR À ESQUERDA
	elif can_move_relative("LEFT"):
		turn_left()
		move_forward()
		colheita()
		
	# 4. BECCO SEM SAÍDA: VIRAR 180 GRAUS (Dar a volta)
	else:
		turn_back()
		colheita()
		# Não precisamos de move_forward() aqui, a função será chamada novamente no próximo ciclo
		# E a nova heading agora aponta para trás (que deve estar livre)

# --- EXECUÇÃO ---
def run():
	seedMaze()
	colheita()
	harvest()
# Inicializa o labirinto e o robô
#clear()
#seedMaze()
# O motor do jogo deve chamar colheita() repetidamente (ex: em um loop while)
#while get_entity_type() != Entities.Treasure:
#	colheita()