def draw_box(pygame, screen, x, y, dif):
	for i in range(2):
		pygame.draw.line(screen, (89, 252, 116), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
		pygame.draw.line(screen, (89, 252, 116), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)
		
def draw(pygame, screen, dif, font1, grid):
	# Draw the lines	
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0:
				# Fill blue color in already numbered grid
				pygame.draw.rect(screen, (95, 206, 249), (i * dif, j * dif, dif + 1, dif + 1))
				# Fill grid with default numbers specified
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif + 18, j * dif + 10))
	# Draw lines horizontally and vertically to form grid		
	for i in range(10):
		if i % 3 == 0 :
			thick = 5
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)

def draw_val(val, font, screen,x,y, dif):
	text1 = font.render(str(val), 1, (0, 0, 0))
	screen.blit(text1, (x * dif + 18, y * dif + 10))