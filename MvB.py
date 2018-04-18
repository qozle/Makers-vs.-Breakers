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
        self.speed = [randint(-4, 4),randint(-4, 4)]
        self.rect.topleft = (randint(0,750),randint(0,750))
        self.collided = False
        
        for key, value in kwargs.items():
            setattr(self, key, value)


class Breaker(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('breaker.png')
        self.rect = self.image.get_rect()
        self.speed = [randint(-4, 4),randint(-4, 4)]
        self.rect.topleft = (randint(0,750), randint(0,750))
        self.collided = False
        
        for key, value in kwargs.items():
            setattr(self, key, value)


class Neuter(pygame.sprite.Sprite):

    def __init__(self, *groups, **kwargs):
        super().__init__(*groups)
        self.image = pygame.image.load('neuter.png')
        self.rect = self.image.get_rect()
        self.speed = [randint(-4, 4),randint(-4, 4)]
        self.rect.topleft = (randint(0,750), randint(0,750))
        self.collided = False
        
        for key, value in kwargs.items():
            setattr(self, key, value)


def hit():
    hitsprite.speed[0], hitsprite.speed[1] = -hitsprite.speed[0], -hitsprite.speed[1]
    sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
    hitsprite.rect = hitsprite.rect.move(hitsprite.speed)
    sprite.rect = sprite.rect.move(sprite.speed)
    sprite.collided = hitsprite
    hitsprite.collided = sprite


def bounce():
    ## Bounce off of walls
    if sprite.rect.left < 0 or sprite.rect.right > width:
        sprite.speed[0] = -sprite.speed[0]
        sprite.rect = sprite.rect.move(sprite.speed)
        sprite.collided = False
        
    if sprite.rect.top < 0 or sprite.rect.bottom > height:
        sprite.speed[1] = -sprite.speed[1]
        sprite.rect = sprite.rect.move(sprite.speed)
        sprite.collided = False


## Initialize
breaker = Breaker(breakers)
maker1 = Maker(makers)
maker2 = Maker(makers)
maker3 = Maker(makers)
maker4 = Maker(makers)
maker5 = Maker(makers)
clock = pygame.time.Clock()


## Main loop
while 1:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == 32:
                print('spacebar was pressed')
                breakers.empty()
                breakers.add(Breaker(breakers))

## Makers loop
    for sprite in makers.sprites():
        dead = False
        bounce() # for bouncing off walls
        current.add(sprite)
        makers.remove(sprite)
        ## If a maker hits a maker, both change direction, make a new neuter
        for hitsprite in pygame.sprite.spritecollide(sprite, makers, False):
            if sprite.collided == hitsprite:
                pass
            else:
                hit()
                neuters.add(Neuter(neuters))
        ## If a maker hits a neuter, both change direction
        for hitsprite in pygame.sprite.spritecollide(sprite, neuters, False):
            if sprite.collided == hitsprite:
                pass
            else:
                hit()
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
        bounce() ## for bouncing off walls
        current.add(sprite)
        breakers.remove(sprite)
        ## If a breaker hits a breaker
        for hitsprite in pygame.sprite.spritecollide(sprite, breakers, False):
            if sprite.collided == hitsprite:
                pass
            else:
                hit()
        ## If a breaker hits a neuter
        for hitsprite in pygame.sprite.spritecollide(sprite, neuters, True):
            if sprite.collided == hitsprite:
                pass
            else:
                sprite.speed[0], sprite.speed[1] = -sprite.speed[0], -sprite.speed[1]
                sprite.rect = sprite.rect.move(sprite.speed)
                
        breakers.add(sprite)
        sprite.rect = sprite.rect.move(sprite.speed)

## Neuters loop
    for sprite in neuters.sprites():
        bounce()
        current.add(sprite)
        neuters.remove(sprite)
        ## If a neuter hits a neuter
        for hitsprite in pygame.sprite.spritecollide(sprite, neuters, False):
            if sprite.collided == hitsprite:
                pass
            else:
                hit()
        neuters.add(sprite)
        sprite.rect = sprite.rect.move(sprite.speed)
    
## Maintain sprite population
    if len(neuters) > 50:
        neuters.empty()
    if len(makers) < 5:
        makers.add(Maker(makers))
## Cleanup event queue and draw.
    pygame.event.pump()
    screen.fill(color)
    makers.draw(screen)
    breakers.draw(screen)
    neuters.draw(screen)
    pygame.display.flip()
