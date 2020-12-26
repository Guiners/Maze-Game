import pygame
import sys
pygame.init()
pygame.mixer.init()

SCREEN_SIZE_Y = 800
SCREEN_SIZE_X = 1600

music = r"C:\Users\Robert\Desktop\scary maze game\Retro muzyczka.mp3"
gameDisplay = pygame.display.set_mode((SCREEN_SIZE_X, SCREEN_SIZE_Y))
clock = pygame.time.Clock()

class text():
    #all text in game
    def __init__(self):
        #getting font
        self.font = pygame.font.Font((r"C:\Users\Robert\Desktop\scary maze game\Langar-Regular.ttf"), 200)
        self.font1 = pygame.font.Font((r"C:\Users\Robert\Desktop\scary maze game\Langar-Regular.ttf"), 80)
        self.font2 = pygame.font.Font((r"C:\Users\Robert\Desktop\scary maze game\Langar-Regular.ttf"), 30)
        #creating texts
        self.text1 = self.font.render("MAZE GAME", True, (218,112,214))
        self.text1_flash = self.font.render("MAZE GAME", True, (228,112,214))
        self.text2 = self.font1.render("Press 'SPACEBAR' to start", True, (186,85,211))
        self.text2_flash = self.font1.render("Press 'SPACEBAR' to start", True, (206,85,211))
        self.text3 = self.font1.render("Press 'ESC' to exit", True, (147,112,219))
        self.text3_flash = self.font1.render("Press 'ESC' to exit", True, (167,112,219))
        self.text4 = self.font2.render("Made by Guiners", True, (147,112,230))
        self.text4_flash = self.font2.render("Made by Guiners", True, (167,112,230))

    def drawing(self, counter, display):
        if counter%4 == 0: #flashing text
            display.blit(self.text1, (int((SCREEN_SIZE_X - self.text1.get_width())/2),80))
            display.blit(self.text2, (int((SCREEN_SIZE_X - self.text2.get_width())/2),380))
            display.blit(self.text3, (int((SCREEN_SIZE_X - self.text3.get_width())/2),580))
            display.blit(self.text4, (int((SCREEN_SIZE_X - self.text4.get_width())/2),750))
        else:
            display.blit(self.text1_flash, (int((SCREEN_SIZE_X - self.text1.get_width())/2),80))
            display.blit(self.text2_flash, (int((SCREEN_SIZE_X - self.text2.get_width())/2),380))
            display.blit(self.text3_flash, (int((SCREEN_SIZE_X - self.text3.get_width())/2),580))
            display.blit(self.text4_flash, (int((SCREEN_SIZE_X - self.text4.get_width())/2),750))


class car():
    def __init__(self, width, height, life = 3):
        self.x = 10 #do dopasowania
        self.y = (int(SCREEN_SIZE_Y - height)/2)
        self.width = width
        self.height = height
        self.velocity = 6
        self.life = life
        self.color = (228,112,214)

    def drawing(self, direction, display):
        #tu sie wstawi tekstury
        if direction == 1: #w prawo
            pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
        elif direction == 2: #w dol
            pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
        elif direction == 3: #w lewo
            pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))
        elif direction == 4: #w gora
            pygame.draw.rect(display, self.color, (self.x, self.y, self.width, self.height))

    def movment(self, direction):
        if direction == 1: self.x += self.velocity
        elif direction == 2: self.y += self.velocity
        elif direction == 3: self.x -= self.velocity
        elif direction == 4: self.y -= self.velocity

    def collision(self, block_list): #nie dziala
        for k in block_list:
            print('y1',k[1])
            print('y2', self.y)
            if self.x < k[0] and self.x >= k[0] - self.width and self.y < k[1] and self.y >= k[1] - self.height:
                print(k[0], k[1])
                self.x = 10 #do dopasowania
                self.y = (int(SCREEN_SIZE_Y - height)/2)
                self.life -= 1
                print("pytka")

class lvl_creator():
    def __init__(self):
        self.lvl1_color = 0
    def draw(display, color, coordinates):
        pygame.draw.rect(display, color, coordinates)


#loading music
pygame.mixer.music.load(music)
pygame.mixer.music.set_volume(0.07)
pygame.mixer.music.play()

#szerokosc/wysokosc korytarz ma 100 wysokosci/szerokosci
lvl1 = ((0,0,450,350), (450,0,1000,50), (1400,0,750,500), (1050,600,750,200), (0,750,1800,50), (0,450,120,400), (200,450,300,220),
(500,450,200,300), (550,140,150,310), (800,600,250,70), (800,140,600,360))
lvl1_color = (167,112,230)
run = True
level = 0
direction = 1
counter = 0
player = car(20,20)
texts = text()
creator = lvl_creator()

while run:
    counter += 1

    if level == 0: gameDisplay.fill((220,220,220)), texts.drawing(counter, gameDisplay)
    elif level == 1:
        gameDisplay.fill((35, 27, 52))
        for i in lvl1:
            pygame.draw.rect(gameDisplay,lvl1_color, i)

        player.collision(lvl1)
        player.drawing(direction, gameDisplay)
        player.movment(direction)




    for event in pygame.event.get():    #exit game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: exit()
            if event.key == pygame.K_SPACE: level = 1
            if event.key == pygame.K_RIGHT: direction = 1
            if event.key == pygame.K_DOWN: direction = 2
            if event.key == pygame.K_LEFT: direction = 3
            if event.key == pygame.K_UP: direction = 4
        elif event.type == pygame.QUIT:
            sys.exit(0)

    pygame.display.update()
    clock.tick(20) #frame per secound
