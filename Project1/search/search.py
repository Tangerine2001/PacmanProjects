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
    from game import Directions
    from game import Configuration
    import pdb

    # path will be a list of Actions. Will change every action and backtrack to last_index.
    path = []
    last_index = 0

    # current_pos is the current position. Will change every action and backtrack
    current_pos = problem.getStartState()

    # successors is just a temp variable to simplify code. Represents the available tiles nearby.
    successors = problem.getSuccessors(current_pos)

    # previous_pos tracks the last position that had more than one path. This way we can "teleport" to it.
    # Each backtrack teleports to the last element in the list, which is then removed from the array.
    if not problem.isGoalState(problem.getStartState()) and len(successors) > 2:
        previous_pos = [problem.getStartState()]

    # current_direction is the direction the pacman will go if he moves in that direction.
    if len(successors) > 0:
        current_direction = successors[0][1]
    else:
        # return an empty path if there are no successors
        return path

    #pdb.set_trace()

    # Perform depth-first until goal state is reached.
    while not problem.isGoalState(current_pos) or current_direction == 'Stop':
        possible_actions = Actions().getPossibleActions(Configuration(current_pos, current_direction), problem.walls)

        if not len(possible_actions) > 1:
            # Returns the last path if there were no solutions
            return path

        if possible_actions[0] != Actions.reverseDirection(current_direction):
            action = possible_actions[0]
        else:
            action = possible_actions[1]
        action_to_take = Actions.directionToVector(action)

        path.append(action_to_take)
        current_direction = action_to_take

        temp_pos = (current_pos[0] + action_to_take[0],
                    current_pos[1] + action_to_take[1])
        current_pos = temp_pos

    return path

    # print("Start:", problem.getStartState())
    # print("Start type:", type(problem))
    # print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    # print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    # print("successor type:", type(problem.getSuccessors(problem.getStartState())))
    #
    # print("Possible Actions:")

    # util.raiseNotDefined()


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


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
