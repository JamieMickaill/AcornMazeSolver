"""
Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn
"""

from cells import *


def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player instance

    Returns:
        string: A string representation of the grid and player + player water buckets count.
    """

    #  Check grid input is valid
    if type(grid) != list:
        raise ValueError("Grid must be a list")
    if len(grid[0]) == 1 and len(grid) == 1:
        raise ValueError("Grid must be more than one character")

    grid1 = grid.copy()
    string_grid = ''

    # Updating water and fire cells that have been changed to air objects
    if player.grid_changes == True:
        for i in player.change_coordinates:
            for j in i:
                column = j[1]
                row = j[0]
                grid1[row][column] = Air()

    # Updating player position
    grid1[player.col][player.row] = player

    # Convert all grid object instances into their Display attribute
    for i in range(len(grid1)):
        for j in range(len(grid1[i])):
            string_grid += (grid1[i][j].display)
        string_grid = string_grid + '\n'

    # Display current water bucket count
    if player.num_water_buckets != 1:
        string_grid = string_grid + "\n" + "You have {} water buckets.".format(player.num_water_buckets)
    if player.num_water_buckets == 1:
        string_grid = string_grid + "\n" + "You have {} water bucket.".format(player.num_water_buckets)
    
    # Strip and newline
    string_grid += "\n"

    #update max grid size
    player.grid_max_width = (len(grid1) - 1)
    player.grid_max_height = (len(grid1[0]) - 1)
    
    return(string_grid)


