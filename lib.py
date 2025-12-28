def isEven(n):
	if(n%2==0):
		return True
	return False
	
def fertilWater():
	if get_water() <= 0.9:
		use_item(Items.Water)
	use_item(Items.Fertilizer)
	
def rnd(n):
	values = []
	for i in range(1,n+1):
		values.append(i)
	ret = values[random()*len(values)]
	#return (random()/n)*10
	return ret
	
def delay(n):
	aux = get_tick_count()
	while(abs(get_tick_count()-aux) <n):
		pass