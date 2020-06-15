"""
Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn
"""

class Player:
    """Player class containing current display string, coordinates, number of water buckets, 
    max grid height and width, and list containing grid cells to be changed"""
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col = 0
        self.coordinates = [self.row,self.col]
        self.grid_changes = False
        self.change_coordinates = []
        self.grid_max_height = 0
        self.grid_max_width = 0
        self.message = None

    #solver function
    def step_solver_bool(self, game):
        return True

    #update player coordinates
    def move(self, move):
        """Updates the position of the player
        
        Arguements: 
            move - single list containing 2 integers, i.e. [1,2]

        """
        self.row += move[0]
        self.col += move[1]


