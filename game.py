import pygame, sys, random
from pygame.math import Vector2


class Game:
    
    cell_number = 20
    cell_size = 40
    velocity = 120
    g_bogy = []

    class SNAKE:
        
        def __init__(self, screen):
            self.screen = screen
            self.body = [Vector2(11,10),Vector2(12,10),Vector2(13,10)]
            self.body_corner = [False, False, False]
            self.direction = Vector2(-1,0)
            self.direction_last_set = pygame.time.get_ticks()
            
            self.head_up = pygame.image.load('graphics/head_up.png').convert_alpha()
            self.head_down = pygame.image.load('graphics/head_down.png').convert_alpha()
            self.head_right = pygame.image.load('graphics/head_right.png').convert_alpha()
            self.head_left = pygame.image.load('graphics/head_left.png').convert_alpha()
            
            self.tail_up = pygame.image.load('graphics/tail_up.png').convert_alpha()
            self.tail_down = pygame.image.load('graphics/tail_down.png').convert_alpha()
            self.tail_right = pygame.image.load('graphics/tail_right.png').convert_alpha()
            self.tail_left = pygame.image.load('graphics/tail_left.png').convert_alpha()

            self.body_vertical = pygame.image.load('graphics/body_vertical.png').convert_alpha()
            self.body_horizontal = pygame.image.load('graphics/body_horizontal.png').convert_alpha()

            self.body_tr = pygame.image.load('graphics/body_topright.png').convert_alpha()
            self.body_tl = pygame.image.load('graphics/body_topleft.png').convert_alpha()
            self.body_br = pygame.image.load('graphics/body_bottomright.png').convert_alpha()
            self.body_bl = pygame.image.load('graphics/body_bottomleft.png').convert_alpha()
        
        def draw_snake(self):
            
            for index, block in enumerate(self.body):
                block_rect = pygame.Rect(block.x*Game.cell_size,block.y*Game.cell_size,Game.cell_size,Game.cell_size)
                if index == 0:
                    self.screen.blit(self.head(), block_rect)
                elif index == (len(self.body)-1):
                    self.screen.blit(self.tail(), block_rect)
                else:
                    next_block = self.body[index+1]
                    prev_block = self.body[index-1]
                    if next_block.x == prev_block.x:
                        self.screen.blit(self.body_vertical, block_rect)
                    elif next_block.y == prev_block.y:
                        self.screen.blit(self.body_horizontal, block_rect)
                    else:
                        self.body_corner[index] = True
                        next_block = next_block - block
                        prev_block = block - prev_block
                        if next_block.y == -1:
                            if prev_block.x == -1:
                                self.screen.blit(self.body_tr, block_rect)
                            else:
                                self.screen.blit(self.body_tl, block_rect)
                        elif next_block.y == 1:
                            if prev_block.x == -1:
                                self.screen.blit(self.body_br, block_rect)
                            else:
                                self.screen.blit(self.body_bl, block_rect)
                        elif next_block.x == -1:
                            if prev_block.y == -1:
                                self.screen.blit(self.body_bl, block_rect)
                            else:
                                self.screen.blit(self.body_tl, block_rect)
                        else:
                            if prev_block.y == -1:
                                self.screen.blit(self.body_br, block_rect)
                            else:
                                self.screen.blit(self.body_tr, block_rect)
        
        def head(self):
            if self.body_corner[1] == True:
                if self.direction == Vector2(-1, 0):
                    return self.head_left
                if self.direction == Vector2(1, 0):
                    return self.head_right
                if self.direction == Vector2(0, 1):
                    return self.head_down
                return self.head_up
            else:
                direction = self.body[0] - self.body[1]
                if direction == Vector2(-1, 0):
                    return self.head_left
                if direction == Vector2(1, 0):
                    return self.head_right
                if direction == Vector2(0, 1):
                    return self.head_down
                return self.head_up
                
        
        def tail(self):
            
            direction = self.body[-1] - self.body[-2]
            
            if direction == Vector2(-1, 0):
                return self.tail_left
            if direction == Vector2(1, 0):
                return self.tail_right
            if direction == Vector2(0, 1):
                return self.tail_down
            return self.tail_up
        
        def move_snake(self):
            
            body_copy = self.body[:-1]
            bcc = self.body_corner[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            bcc.insert(0,False)
            self.body=body_copy[:]
            self.body_corner = bcc
        
        def set_direction(self, new_direction):
            if (pygame.time.get_ticks() - self.direction_last_set) > Game.velocity/2:
                self.direction = Vector2(new_direction[:])
                self.direction_last_set = pygame.time.get_ticks()

    class FRUIT:
        
        def __init__(self, screen):
            self.screen = screen
            self.pos = Vector2(1,1)
            self.randomize()   
            self.apple = pygame.image.load('graphics/apple.png').convert_alpha()
        
        def draw_fruit(self):
            
            fruitRect = pygame.Rect(self.pos.x*Game.cell_size+2,self.pos.y*Game.cell_size+2,Game.cell_size-4,Game.cell_size-4)
            self.screen.blit(self.apple,fruitRect)
            
        def randomize(self):
            
            cells = []
            for i in range(Game.cell_number):
                for j in range(Game.cell_number):
                    cells.append(Vector2(i,j))
            score_cells = []
            for i in range(16, Game.cell_number):
                for j in range(18, Game.cell_number):
                    score_cells.append(Vector2(i,j))
            for item in score_cells:
                cells.remove(item)
            for item in Game.g_bogy:
                if item in cells:
                    cells.remove(item)
            self.pos = random.choice(cells)

    class MAIN:
        
        def __init__(self, screen):
            self.screen = screen
            pygame.mixer.pre_init()
            self.fruit = Game.FRUIT(self.screen)
            self.snake = Game.SNAKE(self.screen)
            Game.g_bogy = self.snake.body
            self.crunch_sound = pygame.mixer.Sound('sounds/crunch.wav')
            self.game_over_sound = pygame.mixer.Sound('sounds/game-over.wav')
            self.game_font = pygame.font.Font('fonts/BADABB__.TTF',25)
        
        def draw_score(self):
            score_text = str(len(self.snake.body)-3)
            score_surface = self.game_font.render(score_text,True,(56,74,12))
            score_x = int(Game.cell_size * Game.cell_number - 60)
            score_y = int(Game.cell_size * Game.cell_number - 40)
            score_rect = score_surface.get_rect(center=(score_x,score_y))
            apple_rect = self.fruit.apple.get_rect(midright=(score_rect.left, score_rect.centery))
            bg_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width + 6, apple_rect.height)
            
            pygame.draw.rect(self.screen,(167,209,61),bg_rect)
            self.screen.blit(self.fruit.apple, apple_rect)
            self.screen.blit(score_surface,score_rect)
            pygame.draw.rect(self.screen,(56,74,12),bg_rect,2)
            
        def draw_elements(self):
            
            self.grass_pattern()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()
        
        def update(self):
            
            self.snake.move_snake()
            Game.g_bogy = self.snake.body
        
        def check_collision(self):
            
            if self.snake.body[0] == self.fruit.pos:
                self.snake.body.append(self.snake.body[-1])
                self.snake.body_corner.append(False)
                self.crunch_sound.play()
                self.fruit.randomize()
            
        def grass_pattern(self):
        
            dark_color = (167, 209, 61)
            light_color = (187, 229, 81)
            for current_cell_h in range(Game.cell_number):
                for current_cell_v in range(Game.cell_number):
                    cell_rect = pygame.Rect(current_cell_h*Game.cell_size, current_cell_v*Game.cell_size, Game.cell_size, Game.cell_size)
                    if ((current_cell_h + current_cell_v) % 2) == 0:
                        color = light_color
                    else:
                        color = dark_color
                    pygame.draw.rect(self.screen, color, cell_rect)

    def run_game(self):
        pause_flag = 1
        pygame.init()
        screen = pygame.display.set_mode((self.cell_number*self.cell_size,self.cell_number*self.cell_size))
        pygame.display.set_caption("Snake Game")
        clock = pygame.time.Clock()
        self.main_game = Game.MAIN(screen)
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE,self.velocity)

        while True:
            
            for event in pygame.event.get():
                
                #EXIT GAME
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                #MOVEMENT UPDATE
                if event.type == pygame.USEREVENT:
                    self.main_game.update()
                
                #CONTROL
                if event.type == pygame.KEYDOWN:
                    
                    #pause
                    if event.key == pygame.K_SPACE:
                        if pause_flag == 1:
                            pygame.time.set_timer(SCREEN_UPDATE,0)
                            pause_flag = 0
                        elif pause_flag == 0:
                            pygame.time.set_timer(SCREEN_UPDATE,self.velocity)
                            pause_flag = 1        
                    
                    #direction control
                    if event.key == pygame.K_UP and self.main_game.snake.direction.y != 1 :
                        self.main_game.snake.set_direction((0,-1))
                    if event.key == pygame.K_DOWN and self.main_game.snake.direction.y != -1 :
                        self.main_game.snake.set_direction((0,1))
                    if event.key == pygame.K_RIGHT and self.main_game.snake.direction.x != -1 :
                        self.main_game.snake.set_direction((1,0))
                    if event.key == pygame.K_LEFT and self.main_game.snake.direction.x != 1 :
                        self.main_game.snake.set_direction((-1,0))
            
            self.main_game.check_collision()
                        
            ## GAME OVER
            for block in self.main_game.snake.body:
                if block.x > 19 or block.x < 0 or block.y > 19 or block.y < 0 :
                    channel = self.main_game.game_over_sound.play()
                    while channel.get_busy():
                        pass
                    pygame.quit()
                    sys.exit()
            
            for block in self.main_game.snake.body[1:]:
                if self.main_game.snake.body[0] == block:
                    channel = self.main_game.game_over_sound.play()
                    while channel.get_busy():
                        pass
                    pygame.quit()
                    sys.exit()
            
            screen.fill((175,215,70))
            self.main_game.draw_elements()
            pygame.display.flip()
            clock.tick(60)

if __name__ == '__main__':
    g = Game()
    g.run_game()
