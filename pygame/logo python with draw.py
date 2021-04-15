import pygame

pygame.init()
win = pygame.display.set_mode((220, 220))

pygame.display.set_caption('First Game')


width = 10
height = 10
s = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
BLUE=(0, 0, 255)
run = True
pi = 3.14

while run:
    pygame.time.delay(30)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

   
    win.fill((WHITE))
    pygame.draw.ellipse(win,BLUE,(60, 10, 90, 45))
    pygame.draw.rect(win,BLUE, (60, 30, 90, 25))
    pygame.draw.circle(win, WHITE, (80, 30), width, height)

    pygame.draw.rect(win,BLUE, (115, 30, 35, 47))
    pygame.draw.rect(win,BLUE, (45, 60, 80, 25))
    pygame.draw.rect(win,BLUE, (35, 80, 100, 20))
    pygame.draw.rect(win,BLUE, (46, 94, 15, 46))
    pygame.draw.circle(win, BLUE, (130, 80), 20, 20)
    pygame.draw.ellipse(win,BLUE,(30, 60, 27, 80))

    
    pygame.draw.ellipse(win,YELLOW,(72, 150, 90, 45))
    pygame.draw.rect(win,YELLOW,(72,150,90,25))
    pygame.draw.circle(win, WHITE, (140, 175), width, height)
    
    pygame.draw.rect(win,YELLOW, (72, 135, 35, 42))
    pygame.draw.rect(win,YELLOW, (86, 106, 80, 25))
    pygame.draw.rect(win,YELLOW, (72, 125, 100, 20))
    pygame.draw.rect(win,YELLOW, (160, 65, 15, 46))
    pygame.draw.circle(win, YELLOW, (92, 126), 20, 20)
    pygame.draw.ellipse(win,YELLOW,(160, 65, 27, 80))
    pygame.display.update()
