import pygame

pygame.init()

white = (255,255,255)
black = (125,125,125)
red = (255,0,0,)
blue = (0,0,255)

displayWidth = 640
displayHeight = 480

clock = pygame.time.Clock()
gridSize = 40
FPS = 30

horizontalGridCount = displayWidth / gridSize
verticalGridCount = displayHeight / gridSize

def gameloop():
	gameExit = False
	
	gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.FULLSCREEN|pygame.SCALED)
	pygame.display.set_caption('Strategy')

	gameDisplay = pygame.display.set_mode((displayWidth,displayHeight), pygame.FULLSCREEN|pygame.SCALED)
	#I HAVE NO CLUE WHY BUT THE WINDOW DOESN'T DISPLAY UNLESS I DECLARE GAMEDISPLAY TWICE

	character1 = [0,0]
	character2 = [1,1]
	movementLimit = 4
	commandState = False
	
	while not gameExit:
		gameDisplay.fill(white)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			
			elif event.type == pygame.MOUSEBUTTONDOWN:	
				if event.button == pygame.BUTTON_LEFT and not commandState:
					if character1[0] == pygame.mouse.get_pos()[0] // gridSize and character1[1] == pygame.mouse.get_pos()[1] // gridSize:
						commandState = True
				elif event.button == pygame.BUTTON_LEFT and commandState:
					if movementLimit - (abs((pygame.mouse.get_pos()[0] // gridSize) - character1[0]) + abs((pygame.mouse.get_pos()[1] // gridSize) - character1[1])) >= 0:
						character1[0] = (pygame.mouse.get_pos()[0] // gridSize)
						character1[1] = (pygame.mouse.get_pos()[1] // gridSize)
						commandState = False
		
		for f in range(int(verticalGridCount/2+1)):
			for i in range(int(horizontalGridCount/2+1)):
				pygame.draw.rect(gameDisplay, black, [i * gridSize * 2, f * gridSize * 2,gridSize,gridSize])
				pygame.draw.rect(gameDisplay, black, [i * gridSize * 2 + gridSize, f * gridSize * 2 + gridSize,gridSize,gridSize])
				
		pygame.draw.rect(gameDisplay, red, [character1[0] * gridSize, character1[1] * gridSize, gridSize, gridSize])
		pygame.draw.rect(gameDisplay, blue, [character2[0] * gridSize, character2[1] * gridSize, gridSize, gridSize])
		
		pygame.display.update()
		clock.tick(FPS)
		
gameloop()