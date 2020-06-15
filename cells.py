"""
Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn
"""


class Start:
    """ The starting cell of the board, can be walked over"""
    def __init__(self):
        self.display = 'X'
        self.message = None
    def __str__(self):
        return "Start"
    def step(self, game):
        return True
    def step_solver_bool(self, game):
        return True

class End:
    """The ending cell of the board"""
    def __init__(self):
        self.display = 'Y'
        self.message = None
    def __str__(self):
        return "End"
    def step(self, game):
        return True
    def step_solver_bool(self, game):
        return True       


class Air:
    """A blank cell which can be walked over"""
    def __init__(self):
        self.display = ' '
        self.message = None
    def __str__(self):
        return "Air"
    def step(self, game):
        return True
    def step_solver_bool(self, game):
        return True


class Wall:
    """ A Wall cell - can not be walked through"""
    def __init__(self):
        self.display = '*'
        self.message = ('You walked into a wall. Oof!' + '\n')
    def __str__(self):
        return "Wall"
    def step(self, game):
        return False
    def step_solver_bool(self, game):
        return False    


class Fire:
    """Fire cell - can be walked over if player has 1 x water bucket, 
    is extinguished if water bucket is used, otherwise game over"""
    def __init__(self):
        self.display = 'F'
        self.message = None
    def __str__(self):
        return "Fire"
    def step(self, game):
        # If player has 1 or more water buckets - extinguish fire
        if game.Player1.num_water_buckets > 0:
            self.message = "With your strong acorn arms,\
 you throw a water bucket at the fire. You acorn roll\
 your way through the extinguished flames!\n"
        # If player has no water buckets - game over
        elif game.Player1.num_water_buckets == 0:
            game.failure = True
        return True
    def step_solver_bool(self, game):
        return True            


class Water:
    """ Water cell - picked up by player to extinguish fire cell"""
    def __init__(self):
        self.display = 'W'
        self.message = "Thank the Honourable Furious Forest, \
you've found a bucket of water!" + "\n"
    def step(self, game):
        game.Player1.num_water_buckets += 1
        return True
    def step_solver_bool(self, game):
        return True


class Teleport:
    """Teleport cell - relocates player to corresponding teleporter number location""" 
    def __init__(self,teleporter_number):
        self.display = str(teleporter_number)  # You'll need to change this!
        self.message = "Whoosh! The magical gates break Physics as we know it\
 and opens a wormhole through space and time.\n"
        self.teleporter_number = teleporter_number
    def step(self, game):
        return False
    def step_solver_bool(self, game):
        return True
