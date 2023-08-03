import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 500))
running = True
clock = pygame.time.Clock()

x_pos = 100
stage = 0
test_surface = pygame.Surface((100, 100))


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    stage += 1
    
    if (stage < 100):
        x_pos += 1
    elif (stage < 110) : 
        x_pos += 4
    elif (stage < 120):
        x_pos += 7
    elif (stage < 130):
        x_pos += 4
    else : 
        x_pos += 1
    test_surface.fill((175, 215, 75))
    screen.fill(pygame.Color('black'))
    screen.blit(test_surface, (x_pos, 150))
    pygame.display.update()   
    clock.tick(60)
