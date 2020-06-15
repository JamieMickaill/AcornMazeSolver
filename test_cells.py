from game import Game
from cells import *
import sys



filename = '/home/board_simple.txt'

New = Game(filename)


def test_cells():
    # positive cases
    
    # confirming cell display
    assert Start().display == 'X','Test failed!'
    assert End().display == 'Y','Test failed!'
    assert Water().display == 'W','Test failed!'
    assert Wall().display == '*','Test failed!'
    assert Fire().display == 'F','Test failed!'
    assert Air().display == ' ','Test failed!'
    assert Teleport(1).display == '1','Test failed!'
    assert Teleport(2).display == '2','Test failed!'
        
    # confirming cell messages
    assert Start().message == None,'Test failed!'
    assert End().message == None,'Test failed!'
    assert Air().message == None,'Test failed!'
    assert Fire().message == None,'Test failed!'    
    assert Wall().message == 'You walked into a wall. Oof!\n','Test failed!'
    assert Water().message == "Thank the Honourable Furious Forest, you've found a bucket of water!\n",'Test failed!'
    assert Teleport(1).message == "Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n",'Test failed!'

    # confirming cell step() function
    assert Start().step(New) == True,'Test failed!'
    assert End().step(New) == True,'Test failed!'   
    assert Fire().step(New) == True,'Test failed!'
    assert Water().step(New) == True,'Test failed!'
    assert Air().step(New) == True,'Test failed!'
    assert Wall().step(New) == False,'Test failed!'
    assert Teleport(1).step(New) == False,'Test failed!' 

    # negative

    #corner/edge
    assert Teleport(11).display != 11,'Test failed!'
        

def run_tests():
    test_cells()

run_tests()
