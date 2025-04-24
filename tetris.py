import pygame, sys, time, random
from pygame.locals import *
from framework import BaseGame

class Block:
    # Input: game of type Game, block_name of type string (e.g. 'hero')
    def __init__(self, game, block_name):
        self.name = block_name
        
        self.color = game.block_colors[self.name]
        
        self.rotation = random.randrange(len(game.block_list[self.name]))
        
        self.set_shape(game.block_list[self.name][self.rotation])
        self.x = int(game.board_width / 2) - int(self.width / 2)
        self.y = 0
        

    # Input: shape as array of strings
    # This function sets the height and width of a block. Do not change this.
    def set_shape(self, shape):
        self.shape = shape
        self.width = len(shape[0])
        self.height = len(shape)
        

    def right_rotation(self, rotation_options):
        self.rotation = (self.rotation + 1) % len(rotation_options)
        self.set_shape(rotation_options[self.rotation])
    

    def left_rotation(self, rotation_options):
        self.rotation = (self.rotation - 1) % len(rotation_options)
        self.set_shape(rotation_options[self.rotation])


class Game(BaseGame):
    def run_game(self):
        self.board = self.get_empty_board()

        current_block = self.get_new_block()
        next_block = self.get_new_block()
        
        self.score_dictionary = {
            0: 0,
            1: 40,
            2: 100,
            3: 300,
            4: 1200
        }

        # GameLoop
        while True:
            self.test_quit_game()
            
            if current_block == None:
                current_block = next_block
                next_block = self.get_new_block()
                
            if not self.is_block_on_valid_position(current_block):
                return
           
            
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_p:
                        self.show_text("Paused")
                elif event.type == KEYDOWN:
                    if event.key in [K_LEFT, K_a] and self.is_block_on_valid_position(current_block, x_change=-1):
                        current_block.x -= 1
                    elif event.key in [K_RIGHT, K_d] and self.is_block_on_valid_position(current_block, x_change=1):
                        current_block.x += 1
                    elif event.key in [K_DOWN, K_s] and self.is_block_on_valid_position(current_block, y_change=1):
                        current_block.y += 1
                    elif event.key == K_q:
                        current_block.left_rotation(self.block_list[current_block.name])
                    elif event.key == K_e:
                        current_block.right_rotation(self.block_list[current_block.name])
                

            if not self.is_block_on_valid_position(current_block, y_change=1):
                
                self.add_block_to_board(current_block)
                lines_removed = self.remove_complete_row()
                self.calculate_new_score(lines_removed, self.level)
                self.calculate_new_level(self.score)
                current_block = None
            else:
                current_block.y += 1
            
            
            self.display.fill(self.background)
            self.draw_game_board()
            self.draw_score()
            self.draw_level()
            self.draw_next_block(next_block)
            if current_block != None:
                self.draw_block(current_block)
            pygame.display.update()
            self.clock.tick(self.speed)
            

    # Check if Coordinate given is on board
    # Returns True if the coordinate is not in the board, False otherwise
    def is_coordinate_on_board(self, x, y):

        return 0 <= x < self.board_width and 0 <= y < self.board_height

    

    # Parameters block, x_change (any movement done in X direction), yChange (movement in Y direction)
    # Returns True if no part of the block is outside the Board or collides with another Block
    def is_block_on_valid_position(self, block, x_change=0, y_change=0):
        
        for y in range(block.height):
            for x in range(block.width):
                if block.shape[y][x] != self.blank_color:
                    new_x = block.x + x + x_change
                    new_y = block.y + y + y_change

                    if not self.is_coordinate_on_board(new_x, new_y):
                        return False

                    if self.gameboard[new_y][new_x] != self.blank_color:
                        return False

        return True
    
    
    
    def add_block_to_board(self, block):
        
        for y in range(block.height):
            for x in range(block.width):
                if block.shape[y][x] != self.blank_color:
                    self.gameboard[block.y + y][block.x + x] = block.color


    def check_row_complete(self, y_coord):
        
        for x in range(self.board_width):
            if self.gameboard[y_coord][x] == self.blank_color:
                return False
        return True
    
    

    def remove_complete_row(self):
        
        lines_removed = 0
        y = self.board_height - 1
        while y >= 0:
            if self.check_row_complete(y):
                del self.gameboard[y]
                self.gameboard.insert(0, [self.blank_color] * self.board_width)
                lines_removed += 1
            else:
                y -= 1
        return lines_removed
    
           

    def calculate_new_score(self, lines_removed, level):
        
        self.score += self.score_dictionary[lines_removed] * (level + 1)

    
    
    def set_game_speed(self, speed):
        
        self.speed = speed
    
    

    def calculate_new_level(self, score):
        
        old_level = self.level
        new_level = score // 300  
        if new_level > old_level:
            increase = new_level - old_level
            self.level = new_level
            self.set_game_speed(self.speed + increase)
       


    def get_new_block(self):

        blockname = random.choice(list(self.block_list.keys()))
        return Block(self, blockname)
    

def main():
    pygame.init()
    game = Game()

    game.display = pygame.display.set_mode((game.window_width, game.window_height))
    game.clock = pygame.time.Clock()
    pygame.display.set_caption('Tetris')

    game.show_text('Tetris')

    game.run_game()
    game.show_text('Game Over')


if __name__ == '__main__':
    main()


