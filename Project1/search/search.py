# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    import pdb
    from copy import copy

    # path will be the list of actions to take.
    path = []

    # curr is the current position of the path
    curr = problem.getStartState()

    # visited is the list of all visited nodes
    visited = [curr]

    # track is the track the pacman takes. used for backtracking indices
    track = [curr]

    # next_curr remembers the node that each key came from
    next_curr = {}

    # expand acts as a stack to expand new nodes.
    expand = []

    while not problem.isGoalState(curr):
        # pdb.set_trace()
        succ = problem.getSuccessors(curr)

        viable = [points for points in succ if points[0] not in visited][::-1]

        if len(viable) < 1:
            # Commence backtracking

            # Grabs next node to test
            next_pos = expand.pop()
            curr = next_pos[0]

            # Gets the node it came from
            expanded = next_curr[next_pos[0]]

            # Resets necessary objects
            index = track.index(expanded)
            track = track[0:index + 1]
            path = path[0:index]

        else:
            for v in viable:
                expand.append(v)
                next_curr[v[0]] = curr
            next_pos = expand.pop()
            curr = next_pos[0]

        # Update necessary objects
        path.append(next_pos[1])
        visited.append(curr)
        track.append(curr)
    return path


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    from copy import copy

    # curr is the current position
    curr = problem.getStartState()

    # paths will be a list of lists of paths
    paths = [[curr]]

    # dir will be a dictionary of directions
    dir = {}

    # traveled_pos keeps tracks of all of the traveled points so as to not traverse them again
    traveled_pos = [curr]

    while True:
        # Creates a temp object for paths so that the foreach loop doesn't mess up
        temp_paths = []
        for path in paths:
            # Sets the new curr node
            curr = path[-1]

            if problem.isGoalState(curr):
                path.pop(0)
                final = [dir[p] for p in path]

                return final

            succ = problem.getSuccessors(curr)

            viable = [point for point in succ if point[0] not in traveled_pos]
            if len(viable) < 1:
                continue

            for v in viable:
                temp = copy(path)
                temp.append(v[0])
                new_path = temp

                dir[v[0]] = v[1]

                temp_paths.append(new_path)
                traveled_pos.append(v[0])
        paths = copy(temp_paths)


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"

    # curr tracks the current position of the path
    curr = problem.getStartState()

    # exp_q hold the order in which to execute node exploration.
    exp_q = util.PriorityQueue()

    while not problem.isGoalState(curr):
        succ = problem.getSuccessors(curr)



    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
