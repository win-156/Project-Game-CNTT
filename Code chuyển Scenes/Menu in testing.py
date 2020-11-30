import pygame, sys

class GameState:            #Lớp các Scenes
	def __init__(self):
		self.state = "intro"

	def intro(self):       #Scene Intro
		screen = pygame.display.set_mode((width,height))
		screen.fill((255,255,255))

		start_button = pygame.transform.scale(pygame.image.load("start.png").convert(),(200,70))
		start_button_rect = start_button.get_rect(center = (400, 340))

		quit_button = pygame.transform.scale(pygame.image.load("quit.png").convert(),(200,70))
		quit_button_rect = quit_button.get_rect(center = (400, 425))

		settings = pygame.transform.scale(pygame.image.load("settings.png").convert_alpha(),(25,25))
		settings_rect = settings.get_rect(center = (750,450))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:       #Event click chuột
				pos = pygame.mouse.get_pos()              #Lấy tọa độ của chuột
				if start_button_rect.collidepoint(pos):    #Hàm va chạm (collision)
					self.state = "main_game"               #cái này giống như flag báo hiệu cho state_manager ở dưới
				if quit_button_rect.collidepoint(pos):
					pygame.quit()
					sys.exit()
				if settings_rect.collidepoint(pos):
					self.state = "language"
		
			
			screen.blit(start_button,start_button_rect)
			screen.blit(quit_button,quit_button_rect)
			screen.blit(settings, settings_rect)
		
			pygame.display.update()

	def main_game(self):            #Scene Game
		screen.fill((255,255,255))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("Input Main Game Here (press Enter to return to menu)", False, (0, 128, 0))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def language(self):           #Scene Language
		screen.fill((0,0,0))
		font = pygame.font.SysFont("Courier", 20)
		font = font.render("Input Language Here (press Enter to return to menu)", False, (255, 255, 255))
		screen.blit(font, (100,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					self.state = "intro"

			pygame.display.update()

	def state_manager(self):             #Quản lý các Scene
		if self.state == "intro":        #Nếu mà state là "intro" thì chạy Scene Intro
			self.intro()
		if self.state == "main_game":    #Nếu mà state là "main_game" thì chạy Scene game
			self.main_game()
		if self.state == "language":     #Nếu mà state là "language" thì chạy Scene Language
			self.language()


pygame.init()
clock = pygame.time.Clock()

width = 800
height = 500

screen = pygame.display.set_mode((width, height))
screen.fill((255,255,255))
pygame.display.set_caption("Test")

game_state = GameState()      #Cái này mình gán cái Class vào một object là game_state





while True:                          #Vòng loop chính của cả game (bao gồm tất cả Scenes)
	game_state.state_manager()       #Mình là chạy cái này để quản lý các Scenes
	clock.tick(30)
