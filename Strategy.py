import pygame

pygame.init()

white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0,75)
red = pygame.Color(255,0,0,)
blue = pygame.Color(0,0,255)
green = pygame.Color(0,255,0)

displayWidth = 640
displayHeight = 480

clock = pygame.time.Clock()
gridSize = 40
FPS = 30

horizontalGridCount = displayWidth // gridSize
verticalGridCount = displayHeight // gridSize

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
	
	window = pygame.display.set_mode((displayWidth,displayHeight), pygame.FULLSCREEN|pygame.SCALED)
	pygame.display.set_caption('Strategy')

	window = pygame.display.set_mode((displayWidth,displayHeight), pygame.FULLSCREEN|pygame.SCALED)
	#I HAVE NO CLUE WHY BUT THE WINDOW DOESN'T DISPLAY UNLESS I DECLARE window TWICE
	
	layer1 = window.convert_alpha()
	layer1.fill([0,0,0,0])
	
	movementIndicator = window.convert_alpha()
	
	layer2 = window.convert_alpha()
	layer2.fill([0,0,0,0])

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
			
	obstacles = characters.copy()
	obstacleCount = len(obstacles)
	obstacleTest = 0
	
	while not gameExit:
		window.fill(white)
		layer1.fill([0,0,0,0])
		movementIndicator.fill([0,0,0,0])
		layer2.fill([0,0,0,0])
		
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
						for i in obstacles:
							if mouseX() != locals()[i][0] or mouseY() != locals()[i][1]:
								obstacleTest += 1
						if obstacleTest == obstacleCount:
							locals()[commandState][0] = (mouseX())
							locals()[commandState][1] = (mouseY())
							commandState = 'none'
						obstacleTest = 0
		if commandState != 'none':
			for f in range(int(verticalGridCount/2+1)):
				for i in range(int(horizontalGridCount/2+1)):
					pygame.draw.rect(layer1, black, [i * gridSize * 2, f * gridSize * 2,gridSize,gridSize])
					pygame.draw.rect(layer1, black, [i * gridSize * 2 + gridSize, f * gridSize * 2 + gridSize,gridSize,gridSize])
					for xCoord in range(horizontalGridCount):
						for yCoord in range(verticalGridCount):
							if movementLimit - (abs((xCoord) - locals()[commandState][0]) + abs((yCoord) - locals()[commandState][1])) >= 0:
								pygame.draw.rect(layer2, pygame.Color(0,255,0,125), [int(game2system(xCoord)), int(game2system(yCoord)), gridSize, gridSize])
		
		pygame.draw.rect(layer2, red, [character1[0] * gridSize, character1[1] * gridSize, gridSize, gridSize])
		pygame.draw.rect(layer2, blue, [character2[0] * gridSize, character2[1] * gridSize, gridSize, gridSize])
		pygame.draw.rect(layer2, green, [int(game2system(character3[0])), int(game2system(character3[1])), gridSize, gridSize])
		
		window.blit(layer1, (0,0))
		window.blit(movementIndicator, (0,0))
		window.blit(layer2, (0,0))
		pygame.display.update()
		clock.tick(FPS)
		
gameloop()