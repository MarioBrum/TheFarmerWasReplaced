import policulture
import mv
import pumpkin
import cactus
import sunflower
import maze
import carrots
import dinossaur
#import maze2#
import f0
import cactusMultiThread
import sunflowerMultiThread
import pumpkinMultiThread
import carrotsMultiThread

def harvestTill():
	harvest()
	till()
	
def IMPRIME(metodo):
	allItemsName = ["Hay","Wood","Carrot","Pumpkin","Cactus","Weird_Substance","Gold","Power","Bone"]
	allItems = [Items.Hay,Items.Wood,Items.Carrot,Items.Pumpkin,Items.Cactus,Items.Weird_Substance,Items.Gold,Items.Power,Items.Bone]
	allItemsBefore = [0,0,0,0,0,0,0,0,0]
	for i in range(len(allItems)):
		allItemsBefore[i] = num_items(allItems[i])
	#quick_print("Hay: ",num_items(Items.Hay),"Wood: ",num_items(Items.Wood),"Carrots: ",num_items(Items.Carrot))
	tempoInicio = get_time()
	metodo()
	tempoFinal = abs(tempoInicio-get_time())
	allItemsFinal = [0,0,0,0,0,0,0,0,0]
	quick_print("Earned items")
	quick_print(" ")
	for j in range(len(allItems)):
		allItemsFinal[j] = num_items(allItems[j])-allItemsBefore[j]
		quick_print(allItemsName[j],": ",allItemsFinal[j])
		#quick_print(allItemsName[i],num_items(allItems[i]))
	quick_print(" ")
	quick_print("Items per minute: ")
	quick_print(" ")
	for k in range(len(allItemsFinal)):
		#print(allItemsName[k]," : ",allItemsFinal[k],"/",tempoFinal/60,"min")
		quick_print(allItemsName[k]," : ",allItemsFinal[k]/(tempoFinal/60),"min")
	quick_print("Time passed: ",tempoFinal/60,"min")
	quick_print("#############################")

######################################################
###################     EXECUCAO    ##################
######################################################
#clear()
#setup.setup()
#setupPumpkin.setup()
while(True):
	clear()
	#mv.moveMap(harvestTill,harvestTill)
	#moduleCarrotsTree.colheita()
	#moduleSunflowerTree.colheita()
	#cactusvagabund.colheita()
	#modulePumpkin.colheita()

	#IMPRIME(policulture.colheita)
	#IMPRIME(pumpkin.colheita)
	#IMPRIME(cactus.colheita)
	#IMPRIME(cactus.colheita)
	#IMPRIME(sunflower.colheita)
	#MPRIME(maze.colheita)
	#IMPRIME(carrots.colheita)
	
	if(num_items(Items.Power) < 5000):
		#IMPRIME(sunflower.colheita)
		IMPRIME(sunflowerMultiThread.colheita)

	#elif(num_items(Items.Carrot) < 1000000):
		#IMPRIME(carrots.colheita)
	#elif(num_items(Items.Pumpkin) < 26000000):
		#IMPRIME(pumpkin.colheita)
	#elif(num_items(Items.Cactus) < 26000000):
		#IMPRIME(cactus.colheita)
	else:
		#IMPRIME(policulture.colheita)
		#IMPRIME(dinossaur.colheita)
		#IMPRIME(maze2.colheita)
		#IMPRIME(f0.run)
		#IMPRIME(cactusMultiThread.colheita)
		#IMPRIME(pumpkinMultiThread.colheita)
		IMPRIME(carrotsMultiThread.colheita)
	
		