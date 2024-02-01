from specs import ROWS, COLS
from game import ConnectFour


class AlphaBetaAiBot:
    """
    Implementation of an AI bot using the Alpha-Beta Pruning algorithm for the Connect Four game.

    Parameters:
        max_depth (int): The maximum depth to search in the Alpha-Beta Pruning algorithm.

    Attributes:
        max_depth (int): The maximum depth to search in the Alpha-Beta Pruning algorithm.

    Methods:
        choose_move(game): Chooses the optimal move for the AI player.
        alphabeta(game, depth, alpha, beta, maximizing_player): Implements the Alpha-Beta Pruning algorithm.
        evaluate(game): Evaluates the current state of the game.
        get_new_game_state(game, col, player): Creates a new game state after making a move.
    """

    def __init__(self, max_depth=7):
        """
        Initialize the AlphaBetaAiBot.

        Parameters:
            max_depth (int): The maximum depth to search in the Alpha-Beta Pruning algorithm.
        """
        self.max_depth = max_depth

    def choose_move(self, game):
        """
        Chooses the optimal move for the AI player using the Alpha-Beta Pruning algorithm.

        Parameters:
            game (ConnectFour): The current state of the Connect Four game.

        Returns:
            int: The chosen column for the next move.
        """
        _, move = self.alphabeta(game, self.max_depth, float('-inf'), float('inf'), True)
        return move

    def alphabeta(self, game, depth, alpha, beta, maximizing_player):
        """
        Implements the Alpha-Beta Pruning algorithm to determine the optimal move.

        Parameters:
            game (ConnectFour): The current state of the Connect Four game.
            depth (int): The current depth in the Alpha-Beta Pruning search.
            alpha (float): The alpha value for pruning.
            beta (float): The beta value for pruning.
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
                eval, _ = self.alphabeta(new_game, depth - 1, alpha, beta, False)

                if eval > max_eval:
                    max_eval = eval
                    best_move = col

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None

            for col in available_columns:
                new_game = self.get_new_game_state(game, col, 'X')
                eval, _ = self.alphabeta(new_game, depth - 1, alpha, beta, True)

                if eval < min_eval:
                    min_eval = eval
                    best_move = col

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval, best_move

    def evaluate(self, game):
        """
        Improved evaluation method that assigns scores based on winning positions and three in a row/diagonal/column.

        Parameters:
            game (ConnectFour): The current state of the Connect Four game.

        Returns:
            int: The evaluation score.
        """
        if game.is_winner('O'):
            return 100_000
        elif game.is_winner('X'):
            return -100_000
        else:
            score = 0

            # Check for three in a row
            for row in range(game.rows):
                for col in range(game.cols - 2):
                    window = [game.board[row][col], game.board[row][col + 1], game.board[row][col + 2]]
                    score += self.evaluate_window(window)

            # Check for three in a column
            for col in range(game.cols):
                for row in range(game.rows - 2):
                    window = [game.board[row][col], game.board[row + 1][col], game.board[row + 2][col]]
                    score += self.evaluate_window(window)

            # Check for three in a diagonal (top-left to bottom-right)
            for row in range(game.rows - 2):
                for col in range(game.cols - 2):
                    window = [game.board[row][col], game.board[row + 1][col + 1], game.board[row + 2][col + 2]]
                    score += self.evaluate_window(window)

            # Check for three in a diagonal (bottom-left to top-right)
            for row in range(2, game.rows):
                for col in range(game.cols - 2):
                    window = [game.board[row][col], game.board[row - 1][col + 1], game.board[row - 2][col + 2]]
                    score += self.evaluate_window(window)

            return score

    def evaluate_window(self, window):
        """
        Helper method to evaluate a window of three cells.

        Parameters:
            window (list): A list of three cells in a row, column, or diagonal.

        Returns:
            int: The score based on the contents of the window.
        """
        ai_count = window.count('O')
        player_count = window.count('X')

        if ai_count == 2:
            return 5
        elif player_count == 2:
            return -5
        elif ai_count == 1 and window.count(' ') == 1:
            return 1
        elif player_count == 1 and window.count(' ') == 1:
            return -1
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
    
