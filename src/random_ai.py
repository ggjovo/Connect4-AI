import random
from specs import *


class RandomAiBot:
    def choose_move(self, game):
        """
        Chooses a random valid move for the AI.

        Parameters:
        - game (ConnectFour): The ConnectFour game instance.

        Returns:
        - int or None: The column where the AI chooses to drop a disc, or None if no valid moves are available.
        """
        available_columns = [col for col in range(COLS) if game.board[0][col] == ' ']
        return random.choice(available_columns) if available_columns else None

