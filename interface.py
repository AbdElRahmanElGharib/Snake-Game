import game as g
import pyautogui


class Main:
    
    def start(self):
        self.game = None
        while True:
            self.game = g.Game()
            self.game.run_game()

    def up(self):
        pyautogui.press('up')

    def down(self):
        pyautogui.press('down')
        
    def right(self):
        pyautogui.press('right')
        
    def left(self):
        pyautogui.press('left')

    def get_state(self):
        
        if self.game == None:
            return None
        
        state = []
        
        state.append(self.game.main_game.snake.direction.x)
        state.append(self.game.main_game.snake.direction.y)
        
        for block in self.game.main_game.snake.body:
            state.append(block.x)
            state.append(block.y)
        
        state.append(self.game.main_game.fruit.pos.x)
        state.append(self.game.main_game.fruit.pos.y)
        
        return state
