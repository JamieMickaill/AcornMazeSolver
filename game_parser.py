"""
Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn
"""

from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
import sys


def read_lines(filename):
    """Reads in a configuration file, 
    processes it using parse() to turn strings into cell instances,
    returns the contents as a list of list of cells.
    
    Arguements:
        filename = directory for configuration file
        
    Returns:
        List of list of cell_Class instance objects        
        
    """

    try:
        with open(filename, 'r') as mapfile:
            lines = mapfile.readlines()            
        parsedboard = parse(lines)
        return parsedboard
    except FileNotFoundError: 
        print("{} does not exist!".format(filename))
        sys.exit()

def check_board(board):
    """ Checks board for invalid numbers of Start or End cells, 
    or invalid number of row cells

    Arguements:
        board = string containg board from config file (unparsed)
        
    Returns:
        ValueError if board invalid.       
        
    """

    x_count = 0
    y_count = 0

    # Count number of X and Y values in grid
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                x_count +=1
            elif board[i][j] ==  "Y":
                y_count +=1

    # Raise exceptions if invalid X or Y count
    if x_count != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(str(x_count)))
    if y_count != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(str(y_count)))

    # Raise exception if board not rectangular
    if len(board) > 1:
        if len(board[0]) != len(board[1]):
            raise ValueError("Each row needs an equal number of cells!")

def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """

    # Dictionary containing strings mapped to cell classes
    CELLS_MAP = {
        "X": Start,
        "Y": End,
        " ": Air,
        "*": Wall,
        "F": Fire,
        "W": Water,
    }



    # Parse grid
    grid = []
    teleport_count = {}
    for line in lines:
        line = line.strip()
        cell_line = []
        for char in line:
            try:
                int(char)
                cell = Teleport(char)
                if char not in teleport_count:
                    teleport_count[char] = 1
                else:
                    teleport_count[char] += 1
            except ValueError:
                if char not in CELLS_MAP:
                    raise ValueError('Bad letter in configuration file: {}.'.format(char))
                if char == 0:
                    raise ValueError('Bad letter in configuration file: {}.'.format(char))
                cell = CELLS_MAP[char]()
            cell_line.append(cell)
        grid.append(cell_line)

    # Check board for invalid characters (In order as requested)
    check_board(lines)

    #check teleport_count is even
    for (key, value) in teleport_count.items():
        if value != 2:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(key))

    return grid



