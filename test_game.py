from game import Game
from cells import *
from player import *
import sys



filename = '/home/board_simple.txt'

# testing board_simple
New = Game(filename)

def test_game():

    """ Get start coordinates """
# positive
    """ checking coordinates correctly obtained from grid - should be [0,2] """
    coordinates = New.get_start_coordinate(New.grid, New.Player1),
    assert coordinates == ([0,2],), "Test case failed."

#negative
    """checking default start position is 0,0  """
    grid1 = [[Wall(), Wall(), Wall()]]
    coordinates = New.get_start_coordinate(grid1,New.Player1)
    assert coordinates == [0,0], "Test case failed."

# corner/edge
    """ two start positions """
    grid2 = [[Wall(), Wall(), Wall(), Start(), End(), Start()]]
    coordinates = New.get_start_coordinate(grid2,New.Player1)
    assert coordinates != [0,3], "Test case failed."

    """ player already on board? """
    grid2 = [[Wall(), Wall(), Player(), Start(), End(),]]
    coordinates = New.get_start_coordinate(grid2,New.Player1)
    assert coordinates == [0,3], "Test case failed."
    assert coordinates != [0,2], "Test case failed."

    """ Only two cells """
    grid2 = [[Wall(), Start()]]
    coordinates = New.get_start_coordinate(grid2,New.Player1)
    assert coordinates == [0,1], "Test case failed."


    """ check cell interactions - confirms if cell can be moved to by player """


    #   positive
    """ check if player can make legal moves """
    assert New.check_cell_interaction([1,1], 'd') == True, 'Test case Failed!'
    # ensure player cant walk through walls
    assert New.check_cell_interaction([0,0], 'd') == False, 'Test case Failed!'


    """ check that game.success metric is triggered upon interaction with end cell """
    New.success = False
    New.check_cell_interaction([2,2], 'd')
    assert New.success == True, 'Test Failed!'

# negative

    """ player attempt to walk through wall """
    assert New.check_cell_interaction([0,0], 'd') != True, 'Test case Failed!'

    # check out of bounds cell
    try:
        New.check_cell_interaction([9,9], 'd')
    except IndexError:
        pass
    else:
        print("Test failed!")  
        
         
# corner/edge

    """ no new coordinates """
    try: 
        New.check_cell_interaction([], 'd')
    except IndexError:
        pass
    else:
        print('Test case Failed!')

    """ correct coordinate but invalid move """
    assert New.check_cell_interaction([0,1], 'B') == False, 'Test case Failed!'    


    """ check check_new_coordinates_valid: - updates moves list and count, returns cell related message """
    # get_cell_text is used as part of check_new_coordinates_valid:
    # positive

    """ check that moves are added to move.list """
    New1 = Game(filename)
    New1.check_new_coordinates_valid([1,1], 'd')
    assert New1.total_moves_count == 1, 'Test case Failed!'  
    assert New1.total_moves == ['d'], 'Test case Failed!'

    """ check no message returned from air cell """
    assert New1.check_new_coordinates_valid([1,1], 'd') == None, 'Test case Failed!'  

    """ check message returned from Wall cell """
    assert New1.check_new_coordinates_valid([0,0], 'd') == ('You walked into a wall. Oof!' + "\n" ), 'Test case Failed!'  

    """ check that player coordinates are updated """
    New2 = Game(filename)
    New2.check_new_coordinates_valid([1,1], 'd')
    assert New2.Player1.col == 1, 'Test case Failed!'  
    assert New2.Player1.row == 1 , 'Test case Failed!'  

# negative
    New3 = Game(filename)
    """ invalid move """
    New3.check_new_coordinates_valid([0,0], 'f'), 'Test case Failed!'  
    assert New3.total_moves_count != 1, 'Test case Failed!'  
    assert New3.total_moves != ['f'], 'Test case Failed!'

# corner/edge

    """ valid move but invalid coordinates """
    try:
        New.check_new_coordinates_valid([5,5], 'a')
    except IndexError:
        pass
    else:
        print("Test Failed!")


    """ game_move """
    #   positive
    New4 = Game(filename)
    New4.Player1.row = 1
    New4.Player1.col = 1
    """  check game moves return correct new coordinates (player coordinates[1,1] + new input) """
    assert New4.game_move('w') == [0,1], 'Test case Failed!' 
    assert New4.game_move('s') == [2,1], 'Test case Failed!' 
    assert New4.game_move('a') == [1,0], 'Test case Failed!' 
    assert New4.game_move('d') == [1,2], 'Test case Failed!' 
    assert New4.game_move('e') == [1,1], 'Test case Failed!' 

# negative
    """ check invalid input does not update coordinates """
    assert New4.game_move('f') == [1,1], 'Test case Failed!'

# corner/edge
    """ check valid input uppercase does not update coordinates """
    assert New4.game_move('W') == [1,1], 'Test case Failed!'
    """ check double input does not update coordinates """
    assert New4.game_move('ww') == [1,1], 'Test case Failed!'
    """ check input with space  does not update coordinates """
    assert New4.game_move('w ') == [1,1], 'Test case Failed!'

def run_tests():
    test_game()

run_tests()
