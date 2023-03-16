import pygame
from modules.check_valid import valid
from modules.raise_error import raise_error1, raise_error2
from modules.instructions import instruction, result
from modules.board_drawing import draw, draw_box, draw_val
from modules.track_cord import get_cord
from modules.auto_solve import solve

# Load test fonts for future use
pygame.font.init()
font1 = pygame.font.SysFont("comicsans", 25)
font2 = pygame.font.SysFont("comicsans", 14)

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("SUDOKU GAME WITH AUTO-SOLVER")
img = pygame.image.load('./assets/game-icon.png')
pygame.display.set_icon(img)

# Global variables
x = 0
y = 0
dif = 500 / 9
val = 0
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# Default Sudoku Board.
grid =[
[7, 8, 0, 4, 0, 0, 1, 2, 0],
[6, 0, 0, 0, 7, 5, 0, 0, 9],
[0, 0, 0, 6, 0, 1, 0, 7, 8],
[0, 0, 7, 0, 4, 0, 2, 6, 0],
[0, 0, 1, 0, 5, 0, 9, 3, 0],
[9, 0, 4, 0, 6, 0, 0, 0, 5],
[0, 7, 0, 3, 0, 0, 0, 1, 2],
[1, 2, 0, 0, 0, 7, 4, 0, 0],
[0, 4, 9, 2, 0, 6, 0, 0, 7]
]

# The loop thats keep the window running
while run:	
	screen.fill((255, 255, 255)) # White color background	
	for event in pygame.event.get(): # Loop through the events stored in event.get()
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag1 = 1
			pos = pygame.mouse.get_pos()
			get_cord(pos, dif)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT:
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP:
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN:
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			if event.key == pygame.K_RETURN:
				flag2 = 1
			if event.key == pygame.K_d: # If D is pressed reset the board to default
				rs = 0
				error = 0
				flag2 = 0
				grid =[
					[7, 8, 0, 4, 0, 0, 1, 2, 0],
					[6, 0, 0, 0, 7, 5, 0, 0, 9],
					[0, 0, 0, 6, 0, 1, 0, 7, 8],
					[0, 0, 7, 0, 4, 0, 2, 6, 0],
					[0, 0, 1, 0, 5, 0, 9, 3, 0],
					[9, 0, 4, 0, 6, 0, 0, 0, 5],
					[0, 7, 0, 3, 0, 0, 0, 1, 2],
					[1, 2, 0, 0, 0, 7, 4, 0, 0],
					[0, 4, 9, 2, 0, 6, 0, 0, 7]
				]
	if flag2 == 1:
		if solve(grid, 0, 0, pygame, screen, draw, font1, dif, draw_box, valid)== False:
			error = 1
		else:
			rs = 1
		flag2 = 0
	if val != 0:		
		draw_val(val, font1, screen, x , y, dif) # Fill value entered in cell
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2(screen, font1) # Raise error when wrong value entered
		val = 0
	
	if error == 1:
		raise_error1(screen, font1)
	if rs == 1:
		result(screen, font1) # Display options when solved
	if flag1 == 1:
		draw_box(pygame, screen, x, y, dif)	# Highlight the cell selected

	draw(pygame, screen, dif, font1, grid) # Draw required lines for making Sudoku grid
	instruction(screen, font2)

	# Update window
	pygame.display.update()

# Quit pygame window
pygame.quit()	
