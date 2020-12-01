import pygame, sys
import random

pygame.init()
clock = pygame.time.Clock()

width = 1000
height = 620

screen = pygame.display.set_mode((width, height))
bg = pygame.transform.scale(pygame.image.load("bg.jpg").convert(),(width,height))
bg_x = 0

player1 = pygame.transform.scale(pygame.image.load("player1.png").convert_alpha(),(100,100))
player1_x = 40
#player1_rect = player1.get_rect(center = (player1_x, height/2))

random_x = [0.2,0.25,0.28,0.3,0.33,0.38,0.4,0.45,0.6]

delta_x = random.choice(random_x)
c = 0
while True:
	bg_x -= 0.4
	screen.blit(bg, (bg_x,0))
	screen.blit(bg, (bg_x + width, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	if bg_x < -width:
		bg_x = 0

	player1_x += 0.8

	screen.blit(player1,(player1_x,height/2))		

	pygame.display.update()
	clock.tick(120)