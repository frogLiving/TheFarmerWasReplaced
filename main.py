mvRight = 0

while True:
	newSize = get_world_size() - 1
	# Update coordinates
	x1 = get_pos_x()
	y1 = get_pos_y()
	
	isMaze = get_entity_type() == Entities.Hedge
	
	if isMaze == False:	
		# Setup for seeds
		carrots = num_items(Items.Carrot_Seed)
		pumpkins = num_items(Items.Pumpkin_Seed)
		water = num_items(Items.Empty_Tank)
		fert = num_items(Items.Fertilizer)
		sFlower = num_items(Items.Sunflower_Seed)
		buySeeds(newSize + 1, carrots, Items.Carrot_Seed)
		buySeeds(newSize * 4, pumpkins, Items.Pumpkin_Seed)
		buySeeds(25, water, Items.Empty_Tank)
		buySeeds(newSize + 1, fert, Items.Fertilizer)
		buySeeds(newSize + 1, sFlower, Items.Sunflower_Seed)
		
		myHarvest(x1, y1, newSize)
		mvRight = myMove(newSize, mvRight)
		
	else:
		move(North)
