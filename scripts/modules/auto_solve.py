def solve(grid, i, j, pygame, screen, draw, font, dif, draw_box, valid):
	
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump()
	for it in range(1, 10):
		if valid(grid, i, j, it)== True:
			grid[i][j]= it
			global x, y
			x = i
			y = j
			# white color background\
			screen.fill((255, 255, 255))
			draw(pygame, screen, dif, font, grid) # Draw required lines for making Sudoku grid
			draw_box(pygame, screen, x, y, dif) # Highlight the cell selected
			pygame.display.update()
			pygame.time.delay(20)
			if solve(grid, i, j, pygame, screen, draw, font, dif, draw_box, valid)== 1:
				return True
			else:
				grid[i][j]= 0
			# white color background\
			screen.fill((255, 255, 255))
		
			draw(pygame, screen, dif, font, grid) # Draw required lines for making Sudoku grid
			draw_box(pygame, screen, x, y, dif) # Highlight the cell selected
			pygame.display.update()
			pygame.time.delay(50)
	return False
