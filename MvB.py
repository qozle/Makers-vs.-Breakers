import sys, pygame, time
from pathlib import Path as path
from random import *

pygame.init()

size = width, height = 512, 512
color = 0, 0, 0


screen = pygame.display.set_mode(size, pygame.RESIZABLE)

makers = pygame.sprite.Group()

class Maker(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('maker.png')
        self.rect = self.image.get_rect()
        self.speed = [randint(1,3),randint(1,3)]
        self.rect.topleft = (randint(0,480),randint(0,480))

        for key, value in kwargs.items():
            setattr(self, key, value)

maker1 = Maker(makers)
maker2 = Maker(makers)
maker3 = Maker(makers)
maker4 = Maker(makers)

maker_num = 4    

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    for sprite in makers.sprites():
        if sprite.rect.left < 0 or sprite.rect.right > width:
            sprite.speed[0] = -sprite.speed[0]
        if sprite.rect.top < 0 or sprite.rect.bottom > height:
            sprite.speed[1] = -sprite.speed[1]
        for item in pygame.sprite.spritecollide(sprite, makers, False, pygame.sprite.collide_circle):
            item.speed[0], item.speed[1] = -item.speed[0], -item.speed[1]
            sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
    
        sprite.rect = sprite.rect.move(sprite.speed)
        
   
    screen.fill(color)
    makers.draw(screen)
    pygame.display.flip()
    time.sleep(.01)
