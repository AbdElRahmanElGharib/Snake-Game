import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 500))
running = True
clock = pygame.time.Clock()

##TODO: Game Loop
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()   
    clock.tick(60)
