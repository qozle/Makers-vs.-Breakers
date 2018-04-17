import sys, pygame, time
from random import *

pygame.init()

size = width, height = 800, 800
color = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

makers = pygame.sprite.Group()
breakers = pygame.sprite.Group()
neuters = pygame.sprite.Group()
current = pygame.sprite.GroupSingle()


class Maker(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('maker.png')
        self.rect = self.image.get_rect()
        self.speed = [choice([-2,-1,1,2]),choice([-2,-1, 1,2])]
        self.rect.topleft = (randint(0,750),randint(0,750))

        for key, value in kwargs.items():
            setattr(self, key, value)


class Breaker(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('breaker.png')
        self.rect = self.image.get_rect()
        self.speed = [choice([-2,-1,1,2]),choice([-2,-1, 1,2])]
        self.rect.topleft = (randint(0,750), randint(0,750))

        for key, value in kwargs.items():
            setattr(self, key, value)


class Neuter(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('neuter.png')
        self.rect = self.image.get_rect()
        self.speed = [choice([-2,-1,1,2]),choice([-2,-1, 1,2])]
        self.rect.topleft = (randint(0,750), randint(0,750))

        for key, value in kwargs.items():
            setattr(self, key, value)


## Initialize
maker1 = Maker(makers)
maker2 = Maker(makers)
maker3 = Maker(makers)
maker4 = Maker(makers)
maker5 = Maker(makers)

breaker = Breaker(breakers)

clock = pygame.time.Clock()


## Main loop
while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ## Makers loop
    for sprite in makers.sprites():
        dead = False
        ## Bounce off of walls
        if sprite.rect.left < 0 or sprite.rect.right > width:
            sprite.speed[0] = -sprite.speed[0]
            sprite.rect = sprite.rect.move(sprite.speed)
        if sprite.rect.top < 0 or sprite.rect.bottom > height:
            sprite.speed[1] = -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)

        current.add(sprite)
        makers.remove(sprite)
        ## If a maker hits a maker, both change direction, make a new neuter
        for hitsprite in pygame.sprite.spritecollide(sprite, makers, False):
            hitsprite.speed[0], hitsprite.speed[1] = -hitsprite.speed[0], -hitsprite.speed[1]
            sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)
            hitsprite.rect = hitsprite.rect.move(hitsprite.speed)
            neuters.add(Neuter(neuters))
        ## If a maker hits a neuter, both change direction
        for hitsprite in pygame.sprite.spritecollide(sprite, neuters, False):
            hitsprite.speed[0], hitsprite.speed[1] = -hitsprite.speed[0], -hitsprite.speed[1]
            sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)
            hitsprite.rect = hitsprite.rect.move(hitsprite.speed)
        ## If a maker hits a breaker
        for hitsprite in pygame.sprite.spritecollide(sprite, breakers, False):
            hitsprite.speed[0], hitsprite.speed[1] = -hitsprite.speed[0], -hitsprite.speed[1]
            hitsprite.rect = hitsprite.rect.move(hitsprite.speed)
            dead = True

        if dead == True:
            pass
        else:
            makers.add(sprite)

        sprite.rect = sprite.rect.move(sprite.speed)

    ## Breakers loop
    for sprite in breakers.sprites():
        ## Bounce off walls
        if sprite.rect.left < 0 or sprite.rect.right > width:
            sprite.speed[0] = -sprite.speed[0]
            sprite.rect = sprite.rect.move(sprite.speed)
        if sprite.rect.top < 0 or sprite.rect.bottom > height:
            sprite.speed[1] = -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)

        current.add(sprite)
        breakers.remove(sprite)
        ## If a breaker hits a breaker
        for hitsprite in pygame.sprite.spritecollide(sprite, breakers, False):
            hitsprite.speed[0], hitsprite.speed[1] = -hitsprite.speed[0], -hitsprite.speed[1]
            sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)
            hitsprite.rect = hitsprite.rect.move(hitsprite.speed)
        ## If a breaker hits a neuter
        for hitsprite in pygame.sprite.spritecollide(sprite, neuters, True):
            sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)

        breakers.add(sprite)
            
        sprite.rect = sprite.rect.move(sprite.speed)

    ## Neuters loop
    for sprite in neuters.sprites():
        ## Bounce off walls
        if sprite.rect.left < 0 or sprite.rect.right > width:
            sprite.speed[0] = -sprite.speed[0]
            sprite.rect = sprite.rect.move(sprite.speed)
        if sprite.rect.top < 0 or sprite.rect.bottom > height:
            sprite.speed[1] = -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)

        current.add(sprite)
        neuters.remove(sprite)
        ## If a neuter hits a neuter
        for hitsprite in pygame.sprite.spritecollide(sprite, neuters, False):
            hitsprite.speed[0], hitsprite.speed[1] = -hitsprite.speed[0], -hitsprite.speed[1]
            sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
            sprite.rect = sprite.rect.move(sprite.speed)
            hitsprite.rect = hitsprite.rect.move(hitsprite.speed)

        neuters.add(sprite)
            
        sprite.rect = sprite.rect.move(sprite.speed)
    

    if len(neuters) > 20:
        neuters.empty()
    if len(makers) < 5:
        makers.add(Maker(makers))
        
    pygame.event.pump()
    screen.fill(color)
    makers.draw(screen)
    breakers.draw(screen)
    neuters.draw(screen)
    pygame.display.flip()
