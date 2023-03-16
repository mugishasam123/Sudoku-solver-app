# Raise error when wrong value entered

def raise_error1(screen, font):
	text1 = font.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))
def raise_error2(screen, font):
	text1 = font.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))