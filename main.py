import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    direction = Vector2(-1,0)
    def __init__(self):
        self.body = [Vector2(11,10),Vector2(12,10),Vector2(13,10)]
    def draw_snake(self):
        for block in self.body:
           block_rect = pygame.Rect(block.x*cell_size+2,block.y*cell_size+2,cell_size-2,cell_size-2)
           pygame.draw.rect(screen,(123,11,223),block_rect)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0]+self.direction)
        self.body=body_copy[:]
class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)     
    def draw_fruit(self):
        fruitRect = pygame.Rect(self.pos.x*cell_size+2,self.pos.y*cell_size+2,cell_size-4,cell_size-4)
        pygame.draw.ellipse(screen,(255,20,20),fruitRect)           

pygame.init()
running = True
cell_number = 20
cell_size = 40
velocity = 100
pause_flag = 1
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,velocity)

while running:
    for event in pygame.event.get():
        #EXIT GAME
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #MOVEMENT UPDATE
        if event.type == pygame.USEREVENT:
            snake.move_snake()
        #CONTROL
        if event.type == pygame.KEYDOWN:
            #pause
            if event.key == pygame.K_SPACE:
                if pause_flag == 1:
                    pygame.time.set_timer(SCREEN_UPDATE,0)
                    pause_flag = 0
                elif pause_flag == 0:
                    pygame.time.set_timer(SCREEN_UPDATE,velocity)
                    pause_flag = 1
                
            #direction control
            if event.key == pygame.K_UP:
                snake.direction=Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                snake.direction=Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                snake.direction=Vector2(1,0)
            if event.key == pygame.K_LEFT:
                snake.direction=Vector2(-1,0)
           
    ## GAME OVER (Experimental) 
    for block in snake.body:
        if block.x > 19 or block.x < 0 or block.y > 19 or block.y < 0 :
             pygame.quit()
             sys.exit()
    
    
    screen.fill((175,215,70))
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)