import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 500))
running = True
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 100))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(test_surface, (150, 150))
    screen.blit(test_surface, (150, 150))
    pygame.display.update()   
    clock.tick(60)
