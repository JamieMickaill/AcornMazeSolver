from game_parser import parse, read_lines
from cells import *

import sys


def test_parse():
    assert True


# positive cases
    """testing normal output of cells"""
    grid = parse(["*XY"])
    assert type(grid[0][0]) == type(Wall()), "Failed Parse!"
    assert type(grid[0][1]) == type(Start()), "Failed Parse!"
    assert type(grid[0][2]) == type(End()), "Failed Parse!"

    """testing normal output of cells"""
    grid1 = ["*XY", "WF*", "11*"]
    grid1p = parse(grid1)
    assert type(grid1p[1][0]) == type(Water()), "Failed Parse!"
    assert type(grid1p[1][1]) == type(Fire()), "Failed Parse!"
    assert type(grid1p[1][2]) == type(Wall()), "Failed Parse!"
    assert type(grid1p[2][0]) == type(Teleport(1)), "Failed Parse!"
    assert type(grid1p[2][1]) == type(Teleport(1)), "Failed Parse!"
    assert type(grid1p[2][2]) == type(Wall()), "Failed Parse!"

    # negative cases

    """ Type error for No file - readlines"""
    try:
        read_lines(None)
    except TypeError:
        pass
    else:
        print("Test Failed")

    """ two start positions """
    try:
        grid1 = parse(["*XXY"])
    except ValueError:
        pass
    else:
        print("Test failed!")



    """ two end positions """
    try:
        grid1 = parse(["*XYY"])
    except ValueError:
        pass
    else:
        print("Test failed!")

    """ Single teleporter """
    try:
        grid1 = parse(["*XA1"])
    except ValueError:
        pass
    else:
        print("Test failed!")    

    """ Single teleporter2 """
    try:
        grid1 = parse(["*XA2"])
    except ValueError:
        pass
    else:
        print("Test failed!")    

    """ 3 teleporter """
    try:
        grid1 = parse(["*XA111"])
    except ValueError:
        pass
    else:
        print("Test failed!")    

    """ 0 teleporter """
    try:
        grid1 = parse(["*XA00"])
    except ValueError:
        pass
    else:
        print("Test failed!")    

    """ no start end or player """
    try:
        grid1 = parse(["***"])
    except ValueError:
        pass
    else:
        print("Test failed!")    

    """ 1cell """
    try:
        grid1 = parse(["*"])
    except ValueError:
        pass
    else:
        print("Test failed!")

    """ only player """
    try:
        grid1 = parse(["*A"])
    except ValueError:
        pass
    else:
        print("Test failed!")       


    """ no start """
    try:
        grid1 = parse(["*Y"])
    except ValueError:
        pass
    else:
        print("Test failed!")   

    """ no end """
    try:
        grid1 = parse(["X*A"])
    except ValueError:
        pass
    else:
        print("Test failed!")   


    """ lowercase grid """
    try:
        grid1 = parse(["xyA"])
    except ValueError:
        pass
    else:
        print("Test failed!")  

    """ invalid character """
    try:
        grid1 = parse(["XYb"])
    except ValueError:
        pass
    else:
        print("Test failed!") 


    # edge cases

    """ uneven lines of grid """
    try:
        grid1 = parse(["X*A","Y11*"])
    except ValueError:
        pass
    else:
        print("Test failed!")

    """ two cell grid  """  
    grid1 = parse(["XY"])
    assert type(grid1[0][0]) == type(Start()), "Failed Parse!"
    assert type(grid1[0][1]) == type(End()), "Failed Parse!"
        
                
      

def run_tests():
    test_parse()

run_tests()
