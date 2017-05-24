import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600), 0, 32)
clock = pygame.time.Clock()
FPS = 24

clr1 = (24,121,213)
clr2 = (230, 76, 230)
clr3 = (45, 224, 12)
i = 0
while True:
    # PROCESSES
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    ##

    # LOGIC
    i += 5
    if i > 255:
        i %= 255
    ##

    # DRAW
    screen.fill((255,255,255))
    pygame.draw.line(screen, clr2, (0, 0), (800, 600), 3)
    pygame.draw.rect(screen, clr3, (40, 40, 300, 45))
    pygame.draw.circle(screen, clr1, (400, 300), 70, 3)
    
    pygame.display.flip()

    ##
    clock.tick(FPS)
   
