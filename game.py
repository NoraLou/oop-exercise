import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
######################

GAME_WIDTH = 7
GAME_HEIGHT = 7

######################



#### Put class definitions here ####
class DoorClosed(GameElement):
    IMAGE = "DoorClosed"
    SOLID = True

class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!"%(len(player.inventory)))

class TransportGem(Gem):

    def interact(self, player):
        #MAKE CHANGE LEVEL HERE
        GAME_BOARD.draw_msg("Message!")

class TaxGem(Gem):

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You got taxed! Welcome to poverty. You have %d items!"%(len(player.inventory)))

class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Horns"

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

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


            #def check_ boundary 
            # this takes  directions frome x, y)


    def keyboard_handler(self, symbol, modifier):
        
        direction = None
        if symbol == key.UP:
            direction = "up"
        elif symbol == key.DOWN:
            direction = "down"
        elif symbol == key.LEFT:
            direction = "left"
        elif symbol == key.RIGHT:
            direction = "right"

        self.board.draw_msg("[%s] moves %s" % (self.IMAGE, direction))
        
        if direction:
            next_location = self.next_pos(direction)

            if next_location:
                next_x = next_location[0]
                next_y = next_location[1]

                #attempt the following:
                try:    
                    #is there an existing element in next position?
                    existing_el = self.board.get_el(next_x, next_y)      

                    #if there is something in the next position, interact with that object, if possible
                    if existing_el:
                        existing_el.interact(self)

                    #if there is an existing element in next_position AND that thing is solid,
                    if existing_el and existing_el.SOLID:
                        #on the board, display this message:
                        self.board.draw_msg("There's something in my way!")
                    #if there isn't an existing element in the next position OR if that element isn't solid,
                    elif existing_el is None or not existing_el.SOLID:
                            #delete the character's sprite on the board in the current position
                            self.board.del_el(self.x, self.y)
                            #set the character's sprite on the board in the next position
                            self.board.set_el(next_x, next_y, self)      
                #if ANY of the things on previous lines (after try statement) returns an IndexError, do the following:
                except IndexError:
                    #display this message on the board: 
                    self.board.draw_msg("Heathen! Ye stay in Druid keepe!")                        
                    #set the character's sprite in the current position (so that it doesn't move)
                    self.board.set_el(self.x, self.y, self)  

        if symbol == key.SPACE:
            self.board.erase_msg()      

class BoardTiles(GameElement): 

    
    self.board.draw_game_map(self)
    self.board.base_board[0][0] 

##   End class definitions    ####

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
    
    # door_positions = [
    #     (3, 0)
    # ]


    # transportgem_positions = [
    #     (5, 4)
    # ]

    # taxgem_positions = [
    #     (2, 5)
    #]    

    gem_positions = [
        (3, 1)

    ]


    gems = []
    for pos in gem_positions:
        gem = Gem()
        GAME_BOARD.register(gem)
        GAME_BOARD.set_el(pos[0], pos[1], gem)
        gems.append(gem)


    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False
        
    for rock in rocks:
        print rock

    player = Character()
    GAME_BOARD.register(player)
    GAME_BOARD.set_el(2, 2, player)
    print player

    GAME_BOARD.draw_msg("This game is wicked awesome.")

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(2, 4, gem)

    # transportgem = TransportGem()
    # GAME_BOARD.register(TransportGem)
    # GAME_BOARD.set_el(2, 4, transportgem)
    
    # taxgem = TaxGem()
    # GAME_BOARD.register(TaxGem)
    # GAME_BOARD.set_el(2, 4, taxgem)