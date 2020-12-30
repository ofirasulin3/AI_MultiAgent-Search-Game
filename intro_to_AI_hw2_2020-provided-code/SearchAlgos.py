"""Search Algos: MiniMax, AlphaBeta
"""
from utils import ALPHA_VALUE_INIT, BETA_VALUE_INIT
#TODO: you can import more modules, if needed


class SearchAlgos:
    def __init__(self, utility, succ, perform_move, players_score, goal=None, heuristic_f=None):
        """The constructor for all the search algos.
        You can code these functions as you like to, 
        and use them in MiniMax and AlphaBeta algos as learned in class
        :param utility: The utility function.
        :param succ: The succesor function.
        :param perform_move: The perform move function.
        :param goal: function that check if you are in a goal state.
        """
        self.utility = utility
        self.succ = succ
        self.perform_move = perform_move
        self.players_score = players_score
        self.goal = goal
        self.h = heuristic_f


    def search(self, state, depth, maximizing_player, players_score):
        pass


class MiniMax(SearchAlgos):

    def search(self, state, depth, maximizing_player, players_score):
        """Start the MiniMax algorithm.
        :param state: The state to start from.
        :param depth: The maximum allowed depth for the algorithm.
        :param maximizing_player: Whether this is a max node (True) or a min node (False).
        :return: A tuple: (The min max algorithm value, The direction in case of max node or None in min mode)
        """
        if self.goal(state):
            return [self.utility(state, players_score, maximizing_player), None]
        if depth == 0:
            return [self.h(state, players_score), None]
        direction = None
        if maximizing_player:
            max_val = float('-inf')
            for op in self.succ(state):
                new_state = self.perform_move(op, True)
                res = self.search(new_state, depth - 1, not maximizing_player)
                if res[0] > max_val:
                    direction = op
                    max_val = res[0]
                self.perform_move(op, False)
            return max_val, direction
        else:
            min_val = float('inf')
            for op in self.succ(state):
                new_state = self.perform_move(op, True)
                res = self.search(new_state, depth - 1, not maximizing_player)
                if res[0] < min_val:
                    direction = op
                    min_val = res[0]
                self.perform_move(op, False)
            return min_val, direction



class AlphaBeta(SearchAlgos):

    def search(self, state, depth, maximizing_player, alpha=ALPHA_VALUE_INIT, beta=BETA_VALUE_INIT):
        """Start the AlphaBeta algorithm.
        :param state: The state to start from.
        :param depth: The maximum allowed depth for the algorithm.
        :param maximizing_player: Whether this is a max node (True) or a min node (False).
        :param alpha: alpha value
        :param: beta: beta value
        :return: A tuple: (The min max algorithm value, The direction in case of max node or None in min mode)
        """
        #TODO: erase the following line and implement this function.
        raise NotImplementedError
