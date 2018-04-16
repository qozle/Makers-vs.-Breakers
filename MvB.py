import sys, pygame, time
from random import *

pygame.init()

size = width, height = 512, 512
color = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

makers = pygame.sprite.Group()
breakers = pygame.sprite.Group()
neuters = pygame.sprite.Group()


class Maker(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('maker.png')
        self.rect = self.image.get_rect()
        self.speed = [randint(1,2), randint(1,2)]
        self.rect.topleft = (randint(0,480),randint(0,480))

        for key, value in kwargs.items():
            setattr(self, key, value)


class Breaker(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('breaker.png')
        self.rect = self.image.get_rect()
        self.speed = [randint(1,2), randint(1,2)]
        self.rect.topleft = (randint(0,480), randint(0,480))

        for key, value in kwargs.items():
            setattr(self, key, value)


class Neuter(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('neuter.png')
        self.rect = self.image.get_rect()
        self.speed = [randint(1,2), randint(1,2)]
        self.rect.topleft = (randint(0,480), randint(0,480))

        for key, value in kwargs.items():
            setattr(self, key, value)


maker1 = Maker(makers)
maker2 = Maker(makers)
maker3 = Maker(makers)
maker4 = Maker(makers)

#breaker = Breaker(breakers)


## Main loop
while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ## Makers for loop
    for sprite in makers.sprites():
        if sprite.rect.left < 0 or sprite.rect.right > width:
            sprite.speed[0] = -sprite.speed[0]
        if sprite.rect.top < 0 or sprite.rect.bottom > height:
            sprite.speed[1] = -sprite.speed[1]
        for item in makers.sprites():
            if item == sprite:
                pass
            elif pygame.sprite.collide_circle(sprite, item):
                print(item)
                sprite.speed[0], sprite.speed[1] = -sprite.speed[1], -sprite.speed[1]
                sprite.rect = sprite.rect.move(sprite.speed)
                neuters.add(Neuter(neuters))
        for item in pygame.sprite.spritecollide(sprite, neuters, False, pygame.sprite.collide_circle):
            sprite.speed[0], sprite.speed[1] = -sprite.speed[1], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)
                
        sprite.rect = sprite.rect.move(sprite.speed)

    ## Breakers for loop
    for sprite in breakers.sprites():
        if sprite.rect.left < 0 or sprite.rect.right > width:
            sprite.speed[0] = -sprite.speed[0]
        if sprite.rect.top < 0 or sprite.rect.bottom > height:
            sprite.speed[1] = -sprite.speed[1]
        for item in pygame.sprite.spritecollide(sprite, makers, True, pygame.sprite.collide_circle):
            sprite.speed[0], sprite.speed[1] = -sprite.speed[1], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)
        for item in pygame.sprite.spritecollide(sprite, neuters, True, pygame.sprite.collide_circle):
            sprite.speed[0], sprite.speed[1] = -sprite.speed[1], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)
            
        sprite.rect = sprite.rect.move(sprite.speed)


    for sprite in neuters.sprites():
        if sprite.rect.left < 0 or sprite.rect.right > width:
            sprite.speed[0] = -sprite.speed[0]
        if sprite.rect.top < 0 or sprite.rect.bottom > height:
            sprite.speed[1] = -sprite.speed[1]
        for item in neuters.sprites():
            if item == sprite:
                pass
            elif pygame.sprite.collide_circle(sprite, item):
                print(item)
                item.speed[0], item.speed[1] = -item.speed[0], -item.speed[1]
                sprite.rect = sprite.rect.move(sprite.speed)
        
            
            
        sprite.rect = sprite.rect.move(sprite.speed)

    if len(neuters) > 10:
        neuters.remove(neuters.sprites()[0])
        

    screen.fill(color)
    makers.draw(screen)
    breakers.draw(screen)
    neuters.draw(screen)
    time.sleep(.007)
    pygame.display.flip()
    
