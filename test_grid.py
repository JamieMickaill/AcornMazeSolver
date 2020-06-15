from game import Game
from cells import *
from grid import grid_to_string


import sys



filename = '/home/board_simple.txt'


New7 = Game(filename)
New8 = Game(filename)

def test_grid():
    """ create a new grid """
    string_grid = grid_to_string(New8.grid, New8.Player1)

    # positive cases


    """ check string returned """
    assert type(string_grid) == str, 'Test Failed!'

    """ check contents of string """
    assert string_grid == "A*X**\n*   *\n**Y**\n\nYou have 0 water buckets.\n", 'Test Failed!'

    """ check grid changes work - changing second wall cell to AIR cell """
    New77 = Game(filename)
    New77.Player1.grid_changes = True
    New77.Player1.change_coordinates.append([[0,1]])
    string_grid = grid_to_string(New77.grid, New77.Player1)
    assert type(string_grid) == str, 'Test Failed!'    
    assert string_grid == "A X**\n*   *\n**Y**\n\nYou have 0 water buckets.\n", 'Test Failed!'
    New77.Player1.change_coordinates = None
    New77.Player1.grid_changes = False

    """ confirm water buckets increase updated in string """
    New9 = Game(filename)
    New9.Player1.num_water_buckets += 1
    string_grid1 = grid_to_string(New9.grid, New9.Player1)   
    assert string_grid1 == "A*X**\n*   *\n**Y**\n\nYou have 1 water bucket.\n", 'Test Failed!'
   


    # negative
    """ passing string grid instead of cell grid """
    try:
        stringy = grid_to_string('x***', New7.Player1)
    except ValueError:
        pass
    else:
        print("Test Failed!") 

    # list of cells instead of list of list of cells
    try:
        stringy = grid_to_string([Wall(),Start(),End()], New7.Player1)
    except TypeError:
        pass
    else:
        print("Test Failed!") 



    #corner/edge

    """ 1d grid horizontal """
    one_dimensional_grid = grid_to_string([[Wall(), Start(), End()]], New9.Player1)
    assert one_dimensional_grid == 'AXY\n\nYou have 1 water bucket.\n'

    """ 1d grid vertical """
    one_dimensional_grid2 = grid_to_string([[Wall()],[Start()],[End()]], New9.Player1)
    assert one_dimensional_grid2 == 'A\nX\nY\n\nYou have 1 water bucket.\n'

    """ 1cell grid """
    try:
        one_cell_grid = grid_to_string([[Start()]], New7.Player1)
    except ValueError:
        pass
    else:
        print('Test Failed')

        

def run_tests():
    test_grid()

run_tests()
