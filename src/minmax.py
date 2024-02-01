from specs import ROWS, COLS
from game import ConnectFour


class MinMaxAiBot:
    """
    Implementation of an AI bot using the Minimax algorithm for the Connect Four game.

    Parameters:
        max_depth (int): The maximum depth to search in the Minimax algorithm.

    Attributes:
        max_depth (int): The maximum depth to search in the Minimax algorithm.

    Methods:
        choose_move(game): Chooses the optimal move for the AI player.
        minimax(game, depth, maximizing_player): Implements the Minimax algorithm.
        evaluate(game): Evaluates the current state of the game.
        get_new_game_state(game, col, player): Creates a new game state after making a move.
    """

    def __init__(self, max_depth=4):
        """
        Initialize the MinMaxAiBot.

        Parameters:
            max_depth (int): The maximum depth to search in the Minimax algorithm.
        """
        self.max_depth = max_depth

    def choose_move(self, game):
        """
        Chooses the optimal move for the AI player using the Minimax algorithm.

        Parameters:
            game (ConnectFour): The current state of the Connect Four game.

        Returns:
            int: The chosen column for the next move.
        """
        _, move = self.minimax(game, self.max_depth, True)
        return move

    def minimax(self, game, depth, maximizing_player):
        """
        Implements the Minimax algorithm to determine the optimal move.

        Parameters:
            game (ConnectFour): The current state of the Connect Four game.
            depth (int): The current depth in the Minimax search.
            maximizing_player (bool): Indicates whether the AI player is maximizing.

        Returns:
            tuple: A tuple containing the evaluation score and the chosen move column.
        """
        if depth == 0 or game.is_winner('X') or game.is_winner('O') or game.is_board_full():
            return self.evaluate(game), None

        available_columns = [col for col in range(COLS) if game.board[0][col] == ' ']

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

            for col in available_columns:
                new_game = self.get_new_game_state(game, col, 'O')
                eval, _ = self.minimax(new_game, depth - 1, False)

                if eval > max_eval:
                    max_eval = eval
                    best_move = col

            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None

            for col in available_columns:
                new_game = self.get_new_game_state(game, col, 'X')
                eval, _ = self.minimax(new_game, depth - 1, True)

                if eval < min_eval:
                    min_eval = eval
                    best_move = col

            return min_eval, best_move

    def evaluate(self, game):
        """
        Evaluates the current state of the Connect Four game.

        Parameters:
            game (ConnectFour): The current state of the Connect Four game.

        Returns:
            int: The evaluation score.
        """
        if game.is_winner('O'):
            return 100
        elif game.is_winner('X'):
            return -100
        else:
            return 0

    def get_new_game_state(self, game, col, player):
        """
        Creates a new game state after making a move.

        Parameters:
            game (ConnectFour): The current state of the Connect Four game.
            col (int): The column where the move is made.
            player (str): The player making the move ('X' or 'O').

        Returns:
            ConnectFour: The new game state after the move.
        """
        new_game = ConnectFour()
        new_game.board = [row[:] for row in game.board]
        new_game.turn = game.turn
        new_game.drop_disc(col, player)
        return new_game
    
