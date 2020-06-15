"""
Author SID: 500611960
Date: 20/05/2020
IT1110 Assessment Task - Acorn
"""

from game import Game
from cells import *
import os
import sys
from player import *
from grid import *


# Check for length of CMD args
if len(sys.argv) > 0:
    filename = sys.argv[1]
if len(sys.argv) > 1:
    mode = sys.argv[2]
if len(sys.argv) == 0:
    print("Usage: python3 solver.py <filename> <mode>")
    sys.exit()


class Node:
    """ Node class contains game instance """
    def __init__(self, game):
        self.game = game
        self.neighbours = []



def apply_parent_moves(moves, node):
    """ Solver function to apply parent moves_count to child

    Arguements:
        moves -- list of strings corresponding to moves
        e.g. 'w' 'a' 's' 'd' 'e'

        node -- New node to apply moves to
   
    """
    for move_made in moves:
        node.game.solver_move_and_validate(move_made)



def update_grid(moves, node):
    """Solver function to change water/fire to Air()
    
    Arguements:
        moves -- list of strings corresponding to moves
    	e.g. 'w' 'a' 's' 'd' 'e'

        node -- Node containing game with grid for updating

    """
    if len(node.game.Player1.change_coordinates) > 0:
        for i in moves:
            for j in i:
                column = j[1]
                row = j[0]
                node.game.grid[row][column] = Air()


def parent_to_child(parent, child):
    """ Applies attributes of parent node to child node

    Arguements: 
        parent -- Parent node containing game instance
        child -- Child node containing game instance
    """
    apply_parent_moves(parent.game.total_moves, child)
    child.game.total_moves += parent.game.total_moves
    child.game.Player1.num_water_buckets += parent.game.Player1.num_water_buckets
    child.game.Player1.change_coordinates += parent.game.Player1.change_coordinates
    if parent.game.Player1.grid_changes == True:
        child.game.Player1.grid_changes == True
    if parent.game.teleport == True:
        child.game.teleport = True
    if parent.game.failure == True:
        child.game.failure = True 
    update_grid(parent.game.Player1.change_coordinates, child)



def DFS_iterative(node):
    """ DFS Iterative search to find path to End cell

    Arguements: 
        Node -- containing game cell

    Returns:
        List of strings if End cell found, e.g. ['w','a','s']
        False if failed
    """

    # Create visited cells list to optimize DFS
    visited = [grid_to_string(node.game.grid, node.game.Player1)]
    # Create node stack for DFS
    nodes_list = [node]

    while True:
        #Break when no more nodes available - No soloution found
        if len(nodes_list) == 0:
            break

        #Pop end node on stack
        node = nodes_list.pop(-1)

        # Check each surrounding cell
        # If movement valid - creates new node
        if node.game.solver_move_check('w') == True:
            # Create new Node containing game instance
            NewNode1 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode1.game.get_start_coordinate(NewNode1.game.grid, NewNode1.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode1)
            #perform move on node with new Game instance
            next_move1 = node.game.game_move('w')
            NewNode1.game.solver_check_new_coordinates_valid_and_move(next_move1, 'w')
            #Check if End found or game Failed, add to neighbours
            if NewNode1.game.success == True:
                return  NewNode1.game.total_moves
            if NewNode1.game.failure != True:
                node.neighbours.append(NewNode1)
            
        if node.game.solver_move_check('a') == True:
            # Create new Node containing game instance
            NewNode2 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode2.game.get_start_coordinate(NewNode2.game.grid, NewNode2.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode2)
            #perform move on node with new Game instance
            next_move2 = node.game.game_move('a')
            NewNode2.game.solver_check_new_coordinates_valid_and_move(next_move2, 'a')
            #Check if End found or game Failed, add to neighbours
            if NewNode2.game.success == True:
                return  NewNode2.game.total_moves
            if NewNode2.game.failure != True:
                node.neighbours.append(NewNode2)


        if node.game.solver_move_check('s') == True:
            # Create new Node containing game instance
            NewNode3 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode3.game.get_start_coordinate(NewNode3.game.grid, NewNode3.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode3)
            #perform move on node with new Game instance
            next_move3 = node.game.game_move('s')
            NewNode3.game.solver_check_new_coordinates_valid_and_move(next_move3, 's')
            #Check if End found or game Failed, add to neighbours
            if NewNode3.game.success == True:
                return NewNode3.game.total_moves
            if NewNode3.game.failure != True:
                node.neighbours.append(NewNode3)

        if node.game.solver_move_check('d') == True:
            # Create new Node containing game instance
            NewNode4 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode4.game.get_start_coordinate(NewNode4.game.grid, NewNode4.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode4)
            #perform move on node with new Game instance
            next_move4 = node.game.game_move('d')
            NewNode4.game.solver_check_new_coordinates_valid_and_move(next_move4, 'd')
            #Check if End found or game Failed, add to neighbours
            if NewNode4.game.success == True:
                return  NewNode4.game.total_moves
            if NewNode4.game.failure != True:
                node.neighbours.append(NewNode4)

        #check cell for teleporter before 'e' input
        blank = Game(filename)
        if node.game.check_cell_teleporter(blank.grid, node.game.Player1.col, node.game.Player1.row) == True:
            # Create new node
            NewNode5 = Node(Game(filename))
            # Get start coordinates for player from grid
            NewNode5.game.get_start_coordinate(NewNode5.game.grid, NewNode5.game.Player1)
            # If parent has previous moves - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode5)         
            next_move5 = node.game.game_move('e')
            # apply move to new node
            NewNode5.game.solver_check_new_coordinates_valid_and_move(next_move5, 'e')
            # append to node.neighbours
            node.neighbours.append(NewNode5)

        #If neighbours not visited, add to visited and add to stack
        for nodey in node.neighbours:
            if grid_to_string(nodey.game.grid, nodey.game.Player1) not in visited:
                visited.append(grid_to_string(nodey.game.grid, nodey.game.Player1))
                nodes_list.append(nodey)


def BFS_iterative(node):
    """ BFS Iterative search to find shortest path to End cell

    Arguements: 
        Node -- containing game cell

    Returns:
        List of strings if End cell found, e.g. ['w','a','s']
        False if failed
    """

    # Create visited cells list to optimize DFS
    visited = [grid_to_string(node.game.grid, node.game.Player1)]
    # Create node stack for DFS
    nodes_list = [node]

    while True:
        #Break when no more nodes available - No soloution found
        if len(nodes_list) == 0:
            break

        #Pop start node on stack (the one line difference!)
        node = nodes_list.pop(0)

        # Check each surrounding cell
        # If movement valid - creates new node
        if node.game.solver_move_check('w') == True:
            # Create new Node containing game instance
            NewNode1 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode1.game.get_start_coordinate(NewNode1.game.grid, NewNode1.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode1)
            #perform move on node with new Game instance
            next_move1 = node.game.game_move('w')
            NewNode1.game.solver_check_new_coordinates_valid_and_move(next_move1, 'w')
            #Check if End found or game Failed, add to neighbours
            if NewNode1.game.success == True:
                return  NewNode1.game.total_moves
            if NewNode1.game.failure != True:
                node.neighbours.append(NewNode1)
            
        if node.game.solver_move_check('a') == True:
            # Create new Node containing game instance
            NewNode2 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode2.game.get_start_coordinate(NewNode2.game.grid, NewNode2.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode2)
            #perform move on node with new Game instance
            next_move2 = node.game.game_move('a')
            NewNode2.game.solver_check_new_coordinates_valid_and_move(next_move2, 'a')
            #Check if End found or game Failed, add to neighbours
            if NewNode2.game.success == True:
                return  NewNode2.game.total_moves
            if NewNode2.game.failure != True:
                node.neighbours.append(NewNode2)


        if node.game.solver_move_check('s') == True:
            # Create new Node containing game instance
            NewNode3 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode3.game.get_start_coordinate(NewNode3.game.grid, NewNode3.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode3)
            #perform move on node with new Game instance
            next_move3 = node.game.game_move('s')
            NewNode3.game.solver_check_new_coordinates_valid_and_move(next_move3, 's')
            #Check if End found or game Failed, add to neighbours
            if NewNode3.game.success == True:
                return NewNode3.game.total_moves
            if NewNode3.game.failure != True:
                node.neighbours.append(NewNode3)

        if node.game.solver_move_check('d') == True:
            # Create new Node containing game instance
            NewNode4 = Node(Game(filename))
            # Get starting position for new Player1
            NewNode4.game.get_start_coordinate(NewNode4.game.grid, NewNode4.game.Player1)
            # If previous moves/attributes - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode4)
            #perform move on node with new Game instance
            next_move4 = node.game.game_move('d')
            NewNode4.game.solver_check_new_coordinates_valid_and_move(next_move4, 'd')
            #Check if End found or game Failed, add to neighbours
            if NewNode4.game.success == True:
                return  NewNode4.game.total_moves
            if NewNode4.game.failure != True:
                node.neighbours.append(NewNode4)

        #check cell for teleporter before 'e' input - optimization
        blank = Game(filename)
        if node.game.check_cell_teleporter(blank.grid, node.game.Player1.col, node.game.Player1.row) == True:
            # Create new node
            NewNode5 = Node(Game(filename))
            # Get start coordinates for player from grid
            NewNode5.game.get_start_coordinate(NewNode5.game.grid, NewNode5.game.Player1)
            # If parent has previous moves - apply to child
            if node.game.total_moves_count > 0:
                parent_to_child(node, NewNode5)         
            next_move5 = node.game.game_move('e')
            # apply move to new node
            NewNode5.game.solver_check_new_coordinates_valid_and_move(next_move5, 'e')
            # append to node.neighbours
            node.neighbours.append(NewNode5)

        #If neighbours not visited, add to visited and add to stack
        for nodey in node.neighbours:
            if grid_to_string(nodey.game.grid, nodey.game.Player1) not in visited:
                visited.append(grid_to_string(nodey.game.grid, nodey.game.Player1))
                nodes_list.append(nodey)

def solve(mode):
    """ runs DFS or BFS and returns moves if successful
    If fails returns False

    Arguements:
        mode -- "DFS" or "BFS" - selects algorithm for search

    Returns:
        list of strings if path found
        False if no path found
    """

    #DFS mode
    if mode == 'DFS':
        New = Game(filename)
        New.get_start_coordinate(New.grid, New.Player1)
        node = Node(New)
        path = DFS_iterative(node)
        if path:
            return path
        else:
            return False

    #BFS mode
    if mode == 'BFS':
        New = Game(filename)
        New.get_start_coordinate(New.grid, New.Player1)
        node = Node(New)
        path = BFS_iterative(node)
        if path:
            return path
        else:
            return False

        
if __name__ == "__main__":
    #check if soloution found at startup
    solution_found = solve(mode)
    if solution_found:
        print("Path has {} moves.".format(len(solution_found)))
        print("Path: {}".format(', '.join(solution_found)))
    else:
        print("There is no possible path.")


    
