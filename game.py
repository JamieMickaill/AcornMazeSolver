"""
Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn
"""

from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import *
import sys



class Game:
    """ Game class contains game function related booleans , \
        creates a player and grid instance, keeps track of total moves"""
    def __init__(self, filename):
        self.exit = False
        self.filename = filename
        self.Player1 = Player()
        self.grid = read_lines(self.filename)
        self.success = False
        self.failure = False
        self.teleport = False
        self.total_moves = []
        self.total_moves_count = 0 
        self.oob = False
        self.incorrect_input = False
        self.e_count = 0


    def get_start_coordinate(self, grid, player):
        """ Searches parsed grid for the Start() instance coordinates, \
        updates player.row and player.col
        
        Arguements:
            grid -- list of lists of cell Class instances
            player -- player Class instance

        Returns:
            Player coordinates -- list of 2 integers e.g. [1,3]
        
        """
        starting_col = 0
        starting_row = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if "Start" in str(grid[i][j]):
                    starting_col = i
                    starting_row = j
        player.col = starting_col
        player.row = starting_row
        player_coordinates = [starting_col,starting_row]
        return player_coordinates




    def display_success_metrics(self, game):
        """ Displays total moves\
         and victory message upon saving the Fire nation, exits game
                
        Arguement:
            Game() instance

        Prints:
            Success message with game statistics (moves and move count)
        
        Exits game

        """
        print()
        print("You conquer the treacherous maze set up by the Fire Nation\
 and reclaim the Honourable Furious Forest Throne, restoring your hometown\
 back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
        print()
        if game.total_moves_count == 1:
            print("You made {} move.".format(game.total_moves_count))
        else:
            print("You made {} moves.".format(game.total_moves_count))
        if game.total_moves_count == 1:
            print("Your move: {}".format(''.join(game.total_moves)))
        else:
            print("Your moves: {}".format(', '.join(game.total_moves)))
        print()
        print("=====================")
        print("====== YOU WIN! =====")
        print("=====================")
        sys.exit()



    def display_failure_metrics(self, game):
        """ Displays total moves and failure message\
         upon losing to the Fire nation, exits game
        
        Arguement:
            Game() instance

        Prints:
            Failure message with game statistics (moves and move count)
        
        Exits game

        """

        print("\nYou step into the fires and watch your\
 dreams disappear :(.\n\
\nThe Fire Nation triumphs! The Honourable Furious Forest is \
reduced to a pile of ash and is scattered to the winds by\
 the next storm... You have been roasted.")
        print()
        if game.total_moves_count <2:
            print("You made {} move.".format(game.total_moves_count))
        else:
            print("You made {} moves.".format(game.total_moves_count))
        if game.total_moves_count < 2:
            print("Your move: {}".format(''.join(game.total_moves)))
        else:
            print("Your moves: {}".format(', '.join(game.total_moves)))
        print()
        print("=====================")
        print("===== GAME OVER =====")
        print("=====================")
        sys.exit()


    def check_cell_interaction(self, coordinates, move):
        """Checks if a move can be performed by the player.
        Takes new coordinates from game_move and move string from user input
        Runs step() function on destination cell,
        which returns boolean as to whether move can be performed.
        and performs step function for water and fire cells
        if coordinates are a special cell (end, tele, water or fire), 
        stores cells to be permenantly changed on the grid in Player1.
        
        Arguements:
            coordinates -- single list of two integers
            move -- string containing 'w' 'a' 's' 'd' 'e' 'q' / or invalid input 
        
        Returns:
            boolean: True or False if player can move to new cell

        """
        #check if new coordinates are valid
        self.coordinates = coordinates
        self.teleport = False
        row = coordinates[1] 
        column = coordinates[0]
        is_valid_move = self.grid[column][row].step(self)

        #Check if a special cell is encountered - perform special function
        if "End" in str(self.grid[column][row]):
            self.success = True

        elif "Water" in str(self.grid[column][row]):
            self.Player1.change_coordinates.append([coordinates])
            self.Player1.grid_changes = True
            
        elif "Fire" in str(self.grid[column][row]) and self.Player1.num_water_buckets == 0:
            self.failure = True
        elif "Fire" in str(self.grid[column][row]) and self.Player1.num_water_buckets > 0:
            self.Player1.num_water_buckets -= 1
            self.Player1.change_coordinates.append([coordinates])
            self.Player1.grid_changes = True

        elif "Teleport" in str(self.grid[column][row]):   
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    if "Teleport" in str(self.grid[i][j]):
                        if self.grid[i][j] != self.grid[column][row]:
                            if self.grid[i][j].teleporter_number == self.grid[column][row].teleporter_number:
                                self.Player1.col = i
                                self.Player1.row = j
                                self.teleport = True
                                return is_valid_move

        return is_valid_move




    def game_move(self, move):
        """  Creates a new_coordinate based on player coordinates + user input, 
        returns new coordinates and updates game boolean values 
        if input invalid or results in player out of bounds (oob).
        These boolean values will be used in check_cell_interactions and reset each move
        
        Arguements: 
            Move -- string containing 'w' 'a' 's' 'd' 'e' 'q' / or invalid input

        Returns:
            Single list of 2 integers [1,2]
        """
        # current row and column set as new_coordinates to be adjusted according to input 
        current_row = self.Player1.col
        current_column = self.Player1.row
        new_coordinates = [current_row,current_column]

        # game booleans oob (out of bounds) and incorrect_input are reset to False
        self.oob = False
        self.incorrect_input = False
        
        # if input is illegal - incorrect_input boolean is set to true
        if move != "w" and move != "a" and move != 's' and move != 'd' and move != 'e' and move != 'q':
            self.incorrect_input = True

        # update coordinate based on user input wasdeq
        elif move == 'w':
            if self.Player1.row != 0:
                self.oob=False
                new_coordinates[0] -= 1
            else:
                self.oob = True

        elif move == 'a':
            if self.Player1.row != 0:
                self.oob=False
                new_coordinates[1] -= 1
            else:
                self.oob = True

        elif move == 's':
            if self.Player1.col != self.Player1.grid_max_width:
                self.oob=False
                new_coordinates[0] += 1
            else:
                self.oob = True
         
        elif move == 'd':
            if self.Player1.row != self.Player1.grid_max_height:
                self.oob=False
                new_coordinates[1] += 1
            else:
                self.oob = True

        elif move == 'e':
            self.e_count +=1
            pass

        elif move == 'q':
            print()
            print("Bye!")
            sys.exit()
        
        #initial check to ensure coordinates are positive
        if new_coordinates[0] < 0 or new_coordinates[1] < 0:
            self.oob = True

        return new_coordinates



    def get_cell_text(self, coordinates):
        """Takes in new coordinates for player from game_move 
        returns the associated message output from the cell associated with the new coordinates
        
        Arguement: 
            coordinates -- list of 2 integers 

        Returns: 
            string: message from cell.message for game output
        """
        self.coordinates = coordinates
        row = coordinates[0] 
        column = coordinates[1]
        message = self.grid[row][column].message
        return message



    def check_new_coordinates_valid(self, new_coordinates, move):
        """ checks if the player movement is valid, 
        if yes - update player coordinates, moves and move count. 
        If not - pass. 
        return cell message
        
        Arguements:
            new_coordinates: single list of 2 integers e.g. [1,2]
            move: string containing 'w' 'a' 's' 'd' 'e' 'q' / or invalid input

        Returns:
            message -- string variable containing message responding to cell interaction
        
        """
        # Check for invalid input
        if self.incorrect_input == True:
            message = 'Please enter a valid move (w, a, s, d, e, q).' + '\n'
            self.incorrect_input = False
            return message

        # Check player not out of bounds
        if self.oob == False:

            # Check if move valid and perform step function, 
            # Update player coordinates and game moves list
            # return cell message
            if self.check_cell_interaction(new_coordinates, move) == True:
                self.Player1.col = new_coordinates[0]
                self.Player1.row = new_coordinates[1]
                self.total_moves.append(move)
                self.total_moves_count +=1
                message = self.get_cell_text(new_coordinates)
                return message

            #If move invalid, check if teleporter, if not, its a wall, return msg
            elif self.check_cell_interaction(new_coordinates, move) == False:
                if self.teleport == True:
                    self.total_moves.append(move)
                    self.total_moves_count +=1  
                message = self.get_cell_text(new_coordinates)
                return message

        # conditionals for if the cell move is invalid / self.oob = out of bounds
        # will create and return a message variable dependent on the specific cell
        else:
            if self.oob == True:
                message = ('You walked into a wall. Oof!' + "\n" )
                self.oob = False
                return message




    #SOLVER USE ONLY FUNCTIONS BELOW


    def check_cell_interaction_solver(self, coordinates, move):
        """Checks if a move can be performed by the player.
        Takes new coordinates from game_move and move string from user input
        Runs step_solver_bool() function on destination cell,
        which returns boolean as to whether move can be performed.
        *** Does not perform special cell functions ***
        *** Only used by solver ***
        
        Arguements:
            coordinates -- single list of two integers
            move -- string containing 'w' 'a' 's' 'd' 'e' 'q' / or invalid input 
        
        Returns:
            boolean: True or False if player can move to new cell

        """

        self.teleport = False
        row = coordinates[1] 
        column = coordinates[0]
        is_valid_move = self.grid[column][row].step_solver_bool(self)
        return is_valid_move

        
                          
    def solver_check_new_coordinates_valid_and_move(self, new_coordinates, move):
        """ checks if the player movement is valid, 
        If yes - update player coordinates, moves and move count.
        If not - pass. return cell message
        
        Arguements:
            new_coordinates: single list of 2 integers e.g. [1,2]
            move: string containing 'w' 'a' 's' 'd' 'e' 'q' / or invalid input

        Returns:
            boolean -- was move successful? T/F
        
        """
        #e_count used to optimize solver - limited to 1 use per map
        if move == 'e':
            self.e_count += 1
            if self.e_count > 1:
                return False

        #check for incorrect input
        if self.incorrect_input == True:
            message = 'Please enter a valid move (w, a, s, d, e, q).' + '\n'
            self.incorrect_input = False
            return False

        #check for oob
        if self.oob == False:

            #update player position, move count and moves list
            if self.check_cell_interaction(new_coordinates, move) == True:
                self.Player1.col = new_coordinates[0]
                self.Player1.row = new_coordinates[1]
                self.total_moves.append(move)
                self.total_moves_count +=1
                message = self.get_cell_text(new_coordinates)
                return True

            #If move invalid, check if teleporter, if not, its a wall, return msg
            elif self.check_cell_interaction(new_coordinates, move) == False:
                if self.teleport == True:
                    self.total_moves.append(move)
                    self.total_moves_count +=1  
                message = self.get_cell_text(new_coordinates)
                return False

        # conditionals for if the cell move is invalid / self.oob = out of bounds
        # will create and return a message variable dependent on the specific cell
        else:
            if self.oob == True:
                message = ('You walked into a wall. Oof!' + "\n" )
                self.oob = False
                return False



    def solver_check_new_coordinates_valid(self, new_coordinates, move):
        """ checks if the player movement is valid, if yes - returns true. If not - pass.
        
        Arguements:
            new_coordinates: single list of 2 integers e.g. [1,2]
            move: string containing 'w' 'a' 's' 'd' 'e' 'q' / or invalid input

        Returns:
            boolean - is move possible? T/F
        
        """
        # E_count - used for solver optimization
        if move == 'e':
            self.e_count += 1
            if self.e_count > 1:
                return False

        # Invalid input returns false
        if self.incorrect_input == True:
            message = 'Please enter a valid move (w, a, s, d, e, q).' + '\n'
            self.incorrect_input = False
            return False

        if self.oob == False:
            # Checks if move valid
            if self.check_cell_interaction_solver(new_coordinates, move) == True:
                return True

            # Checks if move valid
            if self.check_cell_interaction_solver(new_coordinates, move) == False:
                return False

        # Return false if OOB
        else:
            if self.oob == True:
                self.oob = False
                return False           

    
    def solver_move_and_validate(self, move):
        """ Solver function to move player 
        
        Arguements: move - 'w' 'a' 's' 'd' 'e' 'q'
        
        Returns boolean T/F whether move successful
        
        """
        # get new coordinates from game_move
        next_move = self.game_move(move)
        # check if new coordinates are valid and perform move
        return self.solver_check_new_coordinates_valid_and_move(next_move, move)


    def solver_move_check(self, move):
        """ Solver function to check if player move legal 
        
        Arguements: move - 'w' 'a' 's' 'd' 'e' 'q'
        
        Returns boolean T/F whether move possible
        
        """

        # get new coordinates from game_move
        next_move = self.game_move(move)
        # check if new coordinates are valid
        return self.solver_check_new_coordinates_valid(next_move, move)


    def check_cell_teleporter(self, grid1, column, row):
        """Checks if cell if a teleporter 
        - used for solver optimization of 'wait'

        Arguements:
            grid -- list of list of cell instances
            column -- players current column 
        
        Returns:
            boolean: True or False if cell is a teleporter

        """
        if "Teleport" in str(grid1[column][row]):
            #update player coordinates to new teleporter
            return True

