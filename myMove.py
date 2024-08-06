def myMove(num, moveRight):	
	
	# Move first	
	move(North)
	y = get_pos_y()
	
	# Check for num largest value
	if num == y:
		moveRight = 1
		
	
	# Move left if rest
	if y == 0 and moveRight == 1:
		move(East)
		step = False
		moveRight = 0
		
	# return value
	return moveRight
