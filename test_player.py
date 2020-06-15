from game import Game
from player import *
import sys



filename = '/home/board_simple.txt'




def test_player():
    New99 = Game(filename)
    # positive cases
     
    """ confirming cell display """
    assert Player().display == 'A','Test failed!'

    """ confirming existence of row and col """
    assert New99.Player1.row == 0
    assert New99.Player1.col == 0

    """ confirming player_move function """
    New99.Player1.move([0,1])
    assert New99.Player1.col == 1,'Test failed!'

    """ confirming starting water buckets = 0 """
    assert New99.Player1.num_water_buckets == 0,'Test failed!'
    
    # negative

    """ passing single int instead of list """
    try:
        New99.Player1.move(0)
    except TypeError:
        pass
    else:
        print('Test failed!')

    """ passing string instead of list """
    try:
        New99.Player1.move('string')
    except TypeError:
        pass
    else:
        print('Test failed!')


    #corner/edge

    """ No movement """
    New99.Player1.move([0,0])
    New99.Player1.move([0,0])
    assert New99.Player1.col == 1,'Test failed!'

    """ passing floats """
    New99.Player1.move((float(0.5),float(1.6)))
    assert New99.Player1.col == 2.6,'Test failed!'

def run_tests():
    test_player()

run_tests()
