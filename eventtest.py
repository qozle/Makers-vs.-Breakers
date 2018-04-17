import pygame

pygame.init()
size = width, height= 800, 800
screen = pygame.display.set_mode(size)
color = 0, 0, 0


while True:
    pygame.event.pump()
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == 273 or 274 or 275 or 276:
            print(event)
        if event.type == pygame.QUIT:
            quit()
                    

    
    screen.fill(color)
    pygame.display.flip()
