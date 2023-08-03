import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400, 500))
running = True
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 100))
test_surface.fill((175, 215, 75))
screen.blit(test_surface, (150, 150))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()   
    clock.tick(60)
