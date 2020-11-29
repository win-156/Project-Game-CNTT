import pygame, sys

pygame.init()

clock = pygame.time.Clock()
screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255,255,255))
pygame.display.set_caption('GAME')

start_button = pygame.transform.scale(pygame.image.load("start.png").convert(),(200,70))
start_button_rect = start_button.get_rect(center = (400, 340))

quit_button = pygame.transform.scale(pygame.image.load("quit.png").convert(),(200,70))
quit_button_rect = quit_button.get_rect(center = (400, 430))

settings = pygame.transform.scale(pygame.image.load("settings.png").convert(),(25,25))
settings_rect = settings.get_rect(center = (750,450))


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			pos = pygame.mouse.get_pos()
			if start_button_rect.collidepoint(pos):
				print("START")
			if quit_button_rect.collidepoint(pos):
				pygame.quit()
				sys.exit()
			if settings_rect.collidepoint(pos):
				print("LANGUAGE")
	
		
	screen.blit(start_button,start_button_rect)
	screen.blit(quit_button,quit_button_rect)
	screen.blit(settings, settings_rect)
	

	pygame.display.update()
	clock.tick(30)
