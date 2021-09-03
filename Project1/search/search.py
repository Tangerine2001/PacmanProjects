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
    from game import Actions

    # path will be a list of vectors. Will change every action and backtrack.
    path = []

    # current_pos is the current position. Will change every action and backtrack
    current_pos = problem.getStartState()

    # current_direction is the direction the pacman will go if he moves in that direction.
    if len(problem.getSuccessors(current_pos)) > 0:
        current_direction = problem.getSuccessors(current_pos)[0][1]
    else:
        # return an empty path if there are no successors.
        return path

    # pos_dir will store that directions traveled from a specific point.
    pos_dir = {current_pos: []}

    # Perform depth-first until goal state is reached.
    while not problem.isGoalState(current_pos):
        # Gets all of the possible moves for the current position, including the reverse direction
        possible_moves = [successor[1] for successor in problem.getSuccessors(current_pos)]

        # Gets all of the possible actions. Excludes previously visited and opposite direction vectors
        possible_actions = [direction for direction in possible_moves if direction not in pos_dir[current_pos] and
                            direction != Actions.reverseDirection(current_direction) and
                            movePac(current_pos, Actions.directionToVector(direction)) not in pos_dir.keys()]

        # If there are no viable actions from the current position, backtrack
        while len(possible_actions) < 1:
            current_pos = (current_pos[0] - path[-1][0],
                           current_pos[1] - path[-1][1])
            path.pop()
            current_direction = Actions.vectorToDirection(path[-1])
            possible_moves = [successor[1] for successor in problem.getSuccessors(current_pos)]
            possible_actions = [direction for direction in possible_moves if direction not in pos_dir[current_pos] and
                                direction != Actions.reverseDirection(current_direction) and
                                movePac(current_pos, Actions.directionToVector(direction)) not in pos_dir.keys()]

        current_direction = possible_actions[0]

        pos_dir[current_pos].append(current_direction)
        action_to_take = Actions.directionToVector(current_direction)
        path.append(action_to_take)

        current_pos = movePac(current_pos, action_to_take)

        if current_pos not in pos_dir.keys():
            pos_dir[current_pos] = []

    # Path is a list of movement vectors, so we have to convert them to their actual coordinates.
    final = [Actions.vectorToDirection(vec) for vec in path]
    return final


def movePac(pos: tuple, vec: tuple) -> tuple:
    return pos[0] + vec[0], pos[1] + vec[1]


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    import pdb
    from copy import copy

    # current_pos is the current position.
    current_pos = problem.getStartState()

    # paths will be a list of lists of vectors
    paths = [[current_pos]]

    # traveled_pos keeps tracks of all of the traveled points so as to not traverse them again
    traveled_pos = [current_pos]

    while True:
        pdb.set_trace()
        temp_paths = []
        for path in paths:
            # Sets the current position to the last place in the path.
            current_pos = path[-1]

            # Gets all the successors for the last point in the path.
            possible_pos = [(path, successor[0]) for successor in problem.getSuccessors(current_pos)
                            if successor[0] not in traveled_pos]

            # If no successors, delete the path.
            if len(possible_pos) < 1:
                paths.remove(path)
                continue

            for potential in possible_pos:
                if problem.isGoalState(potential[1]):
                    path.append(potential[1])
                    final = stateToDirections(path)
                    return final
                temp = copy(potential[0])
                temp.append(potential[1])
                new_path = temp
                temp_paths.append(new_path)
                traveled_pos.append(potential[1])
        paths = copy(temp_paths)


def stateToDirections(path: list) -> list:
    from game import Actions
    final_path = []
    for i in range(len(path) - 1):
        vec = (path[i+1][0] - path[i][0],
               path[i+1][1] - path[i][1])
        final_path.append(Actions.vectorToDirection(vec))
    return final_path


def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
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
