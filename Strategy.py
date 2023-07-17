import pygame

pygame.init()

white = (255,255,255)
black = (125,125,125)
red = (255,0,0,)
blue = (0,0,255)
green = (0,255,0)

displayWidth = 640
displayHeight = 480

clock = pygame.time.Clock()
gridSize = 40
FPS = 30

horizontalGridCount = displayWidth / gridSize
verticalGridCount = displayHeight / gridSize

def mouseX():
	return pygame.mouse.get_pos()[0] // gridSize

def mouseY():
	return pygame.mouse.get_pos()[1] // gridSize
	
def game2system(i):
	return i * gridSize
	
def system2game(i):
	return i // gridSize

def gameloop():
	gameExit = False
	
	gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.FULLSCREEN|pygame.SCALED)
	pygame.display.set_caption('Strategy')

	gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.FULLSCREEN|pygame.SCALED)
	#I HAVE NO CLUE WHY BUT THE WINDOW DOESN'T DISPLAY UNLESS I DECLARE GAMEDISPLAY TWICE

	character1 = [0,0]
	character2 = [1,1]
	character3 = [2,2]
	movementLimit = 4
	commandState = 'none'
	characters = []
	variables = locals().copy()

	for i in variables:
		if 'character' in str(i) and 'characters' not in str(i):
			characters.append(i)
	
	while not gameExit:
		gameDisplay.fill(white)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			
			elif event.type == pygame.MOUSEBUTTONDOWN:	
				if event.button == pygame.BUTTON_LEFT and commandState == 'none':
					for i in characters:
						if locals()[i][0] == mouseX() and locals()[i][1] == mouseY():
							commandState = i
				elif event.button == pygame.BUTTON_LEFT and commandState != 'none':
					if movementLimit - (abs((mouseX()) - locals()[commandState][0]) + abs((mouseY()) - locals()[commandState][1])) >= 0:
						locals()[commandState][0] = (mouseX())
						locals()[commandState][1] = (mouseY())
						commandState = 'none'
		
		for f in range(int(verticalGridCount/2+1)):
			for i in range(int(horizontalGridCount/2+1)):
				pygame.draw.rect(gameDisplay, black, [i * gridSize * 2, f * gridSize * 2,gridSize,gridSize])
				pygame.draw.rect(gameDisplay, black, [i * gridSize * 2 + gridSize, f * gridSize * 2 + gridSize,gridSize,gridSize])
		
		pygame.draw.rect(gameDisplay, red, [character1[0] * gridSize, character1[1] * gridSize, gridSize, gridSize])
		pygame.draw.rect(gameDisplay, blue, [character2[0] * gridSize, character2[1] * gridSize, gridSize, gridSize])
		pygame.draw.rect(gameDisplay, green, [int(game2system(character3[0])), int(game2system(character3[1])), gridSize, gridSize])
		
		pygame.display.update()
		clock.tick(FPS)
		
gameloop()