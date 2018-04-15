import sys, pygame, time
from pathlib import Path as path

pygame.init()

size = width, height = 512, 512
color = 0, 0, 0


screen = pygame.display.set_mode(size, pygame.RESIZABLE)

makers = pygame.sprite.Group()

maker1 = pygame.sprite.Sprite(makers)
maker1.image = pygame.image.load('maker.png')
maker1.rect = maker1.image.get_rect()
maker1.speed = [1,1]

maker2 = pygame.sprite.Sprite(makers)
maker2.image = pygame.image.load('maker.png')
maker2.rect = maker2.image.get_rect()
maker2.rect.left, maker2.rect.top = 50,50
maker2.speed = [-1,1]



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for item in makers.sprites():
        if item.rect.left < 0 or item.rect.right > width:
            item.speed[0] = -item.speed[0]
        if item.rect.top < 0 or item.rect.bottom > height:
            item.speed[1] = -item.speed[1]
        item.rect = item.rect.move(item.speed)
        
   
    screen.fill(color)
    makers.draw(screen)
    pygame.display.flip()
    time.sleep(.005)
