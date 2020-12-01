import pygame, sys
import random

pygame.init()
clock = pygame.time.Clock()


width = 1000
height = 620

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("GAME")
bg = pygame.transform.scale(pygame.image.load("bg.jpg").convert(),(width,height))
bg_x = 0

player1 = pygame.transform.scale(pygame.image.load("player1.png").convert_alpha(),(100,100))
player1_x = 40
#player1_rect = player1.get_rect(center = (player1_x, height/2))

random_x = [0,0.2,0.4,0.5]
delta_x = random.choice(random_x)                 #delta_x se ngau nhien pick 1 so

PICKNUMBER = pygame.USEREVENT + 1
pygame.time.set_timer(PICKNUMBER, 5000)       # tao mot event se xay ra moi 5s



while True:
	bg_x -= 0.8
	screen.blit(bg, (bg_x,0))
	screen.blit(bg, (bg_x + width, 0))
	if bg_x < -width:
		bg_x = 0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == PICKNUMBER:
			delta_x = random.choice(random_x)    # cu moi 5s thì delta_x se randomly pick 1 so
				
	player1_x += delta_x                     # trong vong loop game thi player1_x se += delta_x (120fps)
	
	screen.blit(player1,(player1_x,height/2))


			

	pygame.display.update()
	clock.tick(120)