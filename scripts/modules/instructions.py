def instruction(screen, font):
	text1 = font.render("PLAY BY MOVING AROUND THE BOARD AND ENTERING VALUES", 1, (0, 0, 0))
	text2 = font.render("PRESS 'ENTER' TO AUTO-SOLVE | PRESS 'D' TO RESET THE BOARD", 1, (0, 0, 0))
	screen.blit(text1, (20, 520))	
	screen.blit(text2, (20, 540))
	
def result(screen, font):
	text1 = font.render("FINISHED! PRESS D TO RESTART", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))