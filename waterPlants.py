def waterPlants(num):
	isDry = get_water()
	myWater = num_items(Items.Water_Tank)
	
	if isDry < num and myWater != 0:
		use_item(Items.Water_Tank)
		#print(isDry)
