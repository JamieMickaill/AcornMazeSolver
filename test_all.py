"""
A simple program that will import your tests and run them all!

Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn

Usage: python3 test_all.py
"""

import subprocess
from test_game import run_tests as test_game
from test_grid import run_tests as test_grid
from test_parser import run_tests as test_parser
from test_cells import run_tests as test_cells
from test_player import run_tests as test_player


print("###########################")
print("### Running unit tests! ###")
print("###########################\n")

test_game()
print("Test Game - tested OK")
test_grid()
print("Test Grid - tested OK")
test_parser()
print("Test Parser - tested OK")
test_cells()
print("Test Cells - tested OK")
test_player()
print("Test Player - tested OK")

# Run the e2e script
subprocess.call(['./test_e2e.sh'])
print("e2e tests OK!")
