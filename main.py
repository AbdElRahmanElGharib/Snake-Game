import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(7,10),Vector2(8,10),Vector2(9,10)]
    def draw_snake(self):
        for block in self.body:
           block_rect = pygame.Rect(block.x*cell_size,block.y*cell_size,cell_size-2,cell_size-2)
           pygame.draw.rect(screen,(123,11,223),block_rect)
class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)     
    def drawFruit(self):
        fruitRect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255,20,20),fruitRect)           

pygame.init()
running = True
cell_number = 20
cell_size = 40
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
fruit = FRUIT()
snake = SNAKE()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    fruit.drawFruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)
