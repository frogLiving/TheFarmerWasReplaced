def toPlant(crops):
	toFertal = num_items(Items.Fertilizer)
	
	if crops == Entities.Bush:
		if toFertal != 0:
			use_item(Items.Fertilizer)
	
	if crops == Entities.Carrots or crops == Entities.Pumpkin or crops == Entities.Tree or Entities.Sunflower:
		if get_ground_type() != Grounds.Soil:
			till()
			
	peddles = measure()
	if crops == Entities.Sunflower and peddles == 15:
		harvest()
	
	if can_harvest():
		harvest()

	plant(crops)
