"""
Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn
"""

from game import Game
import os
import sys
from player import *
from grid import *

if len(sys.argv) > 0:
    filename = sys.argv[1]
else:
    print("Usage: python3 run.py <filename> [play]")
    sys.exit

def user_input():
    """ Function for recieving user input and converting to lowercase
    
    Returns:
        move -- string value containing user input "w" "a" "s" "d" e" or invalid inputs
    
    """
    while True:
        msg = "Input a move: "
        move = input(msg)
        move = move.lower()
        return move


# Create new game instance
New = Game(filename)
# Get starting coordinates and update player position
New.get_start_coordinate(New.grid,New.Player1)
# Convert parsed grid file into a string, 
# print to screen string grid and user stats/messages
print(grid_to_string(Game(filename).grid, New.Player1))

#Game loop
while True:
    # Request user input and store as a variable next_move
    next_move = user_input()
    # Parse user input in game_move, get associated new coordinates based on input
    new_coordinates = New.game_move(next_move)
    # Check if new coordinates are valid, 
    # Create a message variable corresponding to new coordinate
    message = New.check_new_coordinates_valid(new_coordinates, next_move)
    # Print to screen new string grid containing updated player position and water bucket count
    print(grid_to_string(Game(filename).grid, New.Player1))
    # If there is a cell interaction message returned, print it to screen
    if message:
        print(message)
    else:
        pass
    #if the game is won, print the success metrics
    if New.success == True:
        New.display_success_metrics(New)
    #if the game is lost, print the success metrics
    if New.failure == True:
        New.display_failure_metrics(New)
    else:
        pass
    


