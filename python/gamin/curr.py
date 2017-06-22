##import pygame
##
##
##pygame.init()
##window_size = window_width, window_height = 640, 480
##window = pygame.display.set_mode((640, 480))
##
##runnning = True
##
##while running:
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit()
d = dict()
n= int(input(), 2)
for _ in n.split(','):
    d[_] = _*_
print(d)

##n = int(input())
##dic_1 = dict()
##for i in range(1, n+1):
##    dic_1[i] = i*i
##
##print(dic_1)
