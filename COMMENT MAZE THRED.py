		#quick_print(dictMapa)
		#if(contains(dickMapa,planta_x,planta_y)):
		if((planta_x,planta_y) in visitedSet):  #CASO MEU TALE JA ESTEJA PLANTADO
			firstFreeRetorno = firstFree(visitedSet)
			if(firstFreeRetorno == (0,0) or len(visitedSet) == get_world_size()**2):
				#mv.moveTo(0,0)
				#mv.moveMap(harvest,harvest)
				mv.moveTo(0,0)
				mv.droneInLine(harvestUp)
				return
				#break
			planta_x = firstFreeRetorno[0]
			planta_y = firstFreeRetorno[1]
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			semeia()
			
		#quick_print("PLANTA:",planta," X:",planta_x," Y:",planta_y)
		#quick_print("Tamanho dict: ",len(dictMapa))
		#quick_print("MAH DICK: ",dickMapa)
		elif(companhia == None): #CASO NAO TENHA COMPANHIA
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			semeia()
		else:
			visitedSet.add(((planta_x,planta_y)))
			mv.moveTo(planta_x,planta_y)
			if(get_ground_type() == Grounds.Grassland and planta == Entities.Carrot):
				#harvest()
				till()
				#do_a_flip()
			plant(planta)
			#se tem drone deixa ele colher dali
			if(num_drones() < max_drones()-3):
				spawn_drone(colheitaRec)
				spawn_drone(colheitaRec)
				spawn_drone(colheitaRec)
			#redirect main drone
			firstFreeRetorno = firstFree(visitedSet)
			mv.moveTo(firstFreeRetorno[0],firstFreeRetorno[1])
			#spawn_drone(plantaUp)
		if(firstFree(visitedSet) == (0,0) or len(visitedSet) == 32**2):
			mv.moveTo(0,0)
			#mv.moveMap(harvest)
			mv.droneInLine(harvestUp)
			#break
			return