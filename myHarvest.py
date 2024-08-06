def myHarvest(myX, myY, grid):
	
	# Harvest / Plant grass
	if myX == 0:
		harvest()
		
	# Row 1 (Bushes)
	elif myX == 1:
		if myY > 0 and myY < grid -1:
			toPlant(Entities.Pumpkin)
			waterPlants(1)
		else:
			toPlant(Entities.Bush)
	
	# Row 2 (Pumpkins / Trees)
	elif myX == 2:
		if myY > 0 and myY < grid - 1:
			toPlant(Entities.Pumpkin)
			waterPlants(1)
		else:
			toPlant(Entities.Tree)
			waterPlants(.5)
				
	# Row 3 (Pumpkins / Trees)
	elif myX == 3:
		if myY > 0 and myY < grid - 1:
			toPlant(Entities.Pumpkin)
			waterPlants(1)
		else:
			toPlant(Entities.Bush)
		
	# Row 4 (Pumpkins)
	elif myX == 4:
		if myY > 0 and myY < grid - 1:
			toPlant(Entities.Pumpkin)
			waterPlants(1)
		else:
			toPlant(Entities.Tree)
			waterPlants(.5)
			
	# Row 5 (carrots)
	elif myX == 5:
		toPlant(Entities.Carrots)
		#waterPlants(.5)
		
	# Row 6 (sunflowers)
	elif myX == 6:
		if myY == grid:
			toPlant(Entities.Sunflower)
		else:
			toPlant(Entities.Carrots)
			#waterPlants(.5)
