import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 5
GAME_HEIGHT = 5

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"

class Character(GameElement):
    IMAGE = "Girl" 
    IMAGE = "Horns"
    def keyboard_handler(self, symbol, modifier):
        if symbol == key.SPACE:
            self.board.erase_msg()

        elif symbol == key.UP:
            self.board.draw_msg('%s says: "You pressed up!"' % self.IMAGE)
            next_y = self.y -1
            self.board.del_el(self.x, self.y)
            self.board.set_el(self.x, next_y, self)

        elif symbol == key.LEFT:
            self.board.draw_msg('%s says:"Booty Booty Booty left!"' % self.IMAGE)
            next_x = self.x-1
            self.board.del_el(self.x, self.y)
            self.board.set_el(next_x, self.y, self)

        elif symbol == key.RIGHT:
            self.board.draw_msg('%s says:"Twerk twerk twerk right!"' % self.IMAGE)
            next_x = self.x +1
            self.board.del_el(self.x, self.y)
            self.board.set_el(next_x, self.y, self)

        elif symbol == key.DOWN:
            self.board.draw_msg('%s says:"Oh yeah! time to party!"' % self.IMAGE)
            next_y = self.y +1
            self.board.del_el(self.x, self.y)
            self.board.set_el(self.x, next_y, self)

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)
        return None


####   End class definitions    ####

def initialize():
    """Put game initialization code here"""
    rock_positions = [
        (2, 0),
        (1, 2),
        (2, 1),
        (3, 2),
        (2, 2),
        (2, 3)
    ]
    
    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)
        
    for rock in rocks:
        print rock

    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 2, player)
    print player

    GAME_BOARD.draw_msg("This game is wicked awesome.")