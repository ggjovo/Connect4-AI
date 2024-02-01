from specs import *


class ConnectFour:
    def __init__(self):
        """
        Initializes a ConnectFour game instance.

        Attributes:
        - rows (int): The number of rows on the game board.
        - cols (int): The number of columns on the game board.
        - board (list): A 2D list representing the game board.
        - turn (int): Represents the current player's turn. 0 for Player 1 (X), 1 for Player 2 (O).
        """
        self.rows = ROWS
        self.cols = COLS
        self.board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
        self.turn = 0  # 0 for Player 1 (X), 1 for Player 2 (O)


    def is_valid_move(self, col):
        """
        Checks if a given move is valid.

        Parameters:
        - col (int): The column where the player wants to drop a disc.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        return 0 <= col < self.cols and self.board[0][col] == ' '


    def drop_disc(self, col, player):
        """
        Drops a disc into the specified column for the current player.

        Parameters:
        - col (int): The column where the player wants to drop a disc.
        - player (str): The player making the move ('X' or 'O').

        Returns:
        - bool: True if the disc is successfully dropped, False otherwise.
        """
        for i in range(self.rows - 1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = player
                self.turn = 1 - self.turn  # Switch turn to the other player
                return True
        return False


    def is_winner(self, player):
        """
        Checks if the specified player has won the game.

        Parameters:
        - player (str): The player to check for a win ('X' or 'O').

        Returns:
        - bool: True if the player has won, False otherwise.
        """
        # Check for horizontal wins
        for row in self.board:
            if ''.join(row).count(player * 4) > 0:
                return True

        # Check for vertical wins
        for col in range(self.cols):
            column = ''.join(self.board[row][col] for row in range(self.rows))
            if column.count(player * 4) > 0:
                return True

        # Check for diagonal wins (top-left to bottom-right)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == player for i in range(4)):
                    return True

        # Check for diagonal wins (bottom-left to top-right)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == player for i in range(4)):
                    return True

        return False


    def is_board_full(self):
        """
        Checks if the game board is full.

        Returns:
        - bool: True if the board is full, False otherwise.
        """
        return all(cell != ' ' for row in self.board for cell in row)

