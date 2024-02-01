import pygame
import sys
from game import ConnectFour
from random_ai import RandomAiBot
from minmax import MinMaxAiBot
from alphabeta import AlphaBetaAiBot
from specs import *


class ConnectFourGUI:
    def __init__(self):
        """
        Initializes the ConnectFourGUI instance.

        Initializes Pygame, sets up the game window, initializes game-related variables, and loads fonts.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Connect Four")
        self.clock = pygame.time.Clock()

        self.game = ConnectFour()
        self.ai_bot = MinMaxAiBot()
        self.ai_playing = False

        # Load font
        self.font = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE)
        
        self.game_title = "Play Connect4 against AGI"
        self.game_title_font = pygame.font.Font(pygame.font.get_default_font(), FONT_SIZE + 10)
        self.game_title_position = (WIDTH // 2, HEIGHT // 4)

        # Main menu buttons
        self.play_first_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, FONT_SIZE * 2)
        self.play_second_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + FONT_SIZE * 3, WIDTH // 2, FONT_SIZE * 2)
        self.quit_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + FONT_SIZE * 6, WIDTH // 2, FONT_SIZE * 2)
        
        # Choosing AI bot buttons
        self.random_ai_button = pygame.Rect(WIDTH // 4, HEIGHT // 2, WIDTH // 2, FONT_SIZE * 2)
        self.minmax_ai_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + FONT_SIZE * 3, WIDTH // 2, FONT_SIZE * 2)
        self.alphabeta_ai_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + FONT_SIZE * 6, WIDTH // 2, FONT_SIZE * 2)


        # Initialize player labels
        self.player1_label = "Player 1"
        self.player2_label = "AI"

    def draw_main_menu(self):
        """
        Draws the main menu screen.

        Displays buttons for playing first, playing second, and quitting the game.
        """
        self.screen.fill(BACKGROUND_COLOR)

        # Draw game title
        game_title_text = self.game_title_font.render(self.game_title, True, FONT_COLOR)
        game_title_rect = game_title_text.get_rect(center=self.game_title_position)
        self.screen.blit(game_title_text, game_title_rect)

        pygame.draw.rect(self.screen, FONT_COLOR, self.play_first_button)
        pygame.draw.rect(self.screen, FONT_COLOR, self.play_second_button)
        pygame.draw.rect(self.screen, FONT_COLOR, self.quit_button)

        play_first_text = self.font.render("Play First", True, BACKGROUND_COLOR)
        play_first_rect = play_first_text.get_rect(center=self.play_first_button.center)
        self.screen.blit(play_first_text, play_first_rect)

        play_second_text = self.font.render("Play Second", True, BACKGROUND_COLOR)
        play_second_rect = play_second_text.get_rect(center=self.play_second_button.center)
        self.screen.blit(play_second_text, play_second_rect)

        quit_text = self.font.render("Quit", True, BACKGROUND_COLOR)
        quit_rect = quit_text.get_rect(center=self.quit_button.center)
        self.screen.blit(quit_text, quit_rect)

        pygame.display.flip()

    def run_main_menu(self):
        """
        Runs the main menu loop.

        Handles user input for selecting game options in the main menu.
        """
        menu_running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_first_button.collidepoint(event.pos):
                        self.player1_label = "PLAYER"
                        self.player2_label = "AI"
                        self.game.turn = 0  # Player plays first
                        menu_running = False  # Exit the main menu loop
                    elif self.play_second_button.collidepoint(event.pos):
                        self.player1_label = "AI"
                        self.player2_label = "PLAYER"
                        self.game.turn = 1  # AI plays first
                        menu_running = False  # Exit the main menu loop
                    elif self.quit_button.collidepoint(event.pos):  # Handle quit button click
                        pygame.quit()
                        sys.exit()

            self.draw_main_menu()
            self.clock.tick(30)
            
    def draw_ai_bot_dialog(self):
        """
        Draws the AI bot selection screen.

        Displays buttons for choosing between different AI bots.
        """
        self.screen.fill(BACKGROUND_COLOR)

        # Draw game title
        game_title_text = self.game_title_font.render("Select Difficulty", True, FONT_COLOR)
        game_title_rect = game_title_text.get_rect(center=self.game_title_position)
        self.screen.blit(game_title_text, game_title_rect)

        pygame.draw.rect(self.screen, FONT_COLOR, self.random_ai_button)
        pygame.draw.rect(self.screen, FONT_COLOR, self.minmax_ai_button)
        pygame.draw.rect(self.screen, FONT_COLOR, self.alphabeta_ai_button)

        random_bot_text = self.font.render("Easy", True, BACKGROUND_COLOR)
        random_bot_rect = random_bot_text.get_rect(center=self.play_first_button.center)
        self.screen.blit(random_bot_text, random_bot_rect)

        minmax_text = self.font.render("Hard", True, BACKGROUND_COLOR)
        minmax_rect = minmax_text.get_rect(center=self.play_second_button.center)
        self.screen.blit(minmax_text, minmax_rect)

        alphabeta_text = self.font.render("Turbo Hard", True, BACKGROUND_COLOR)
        alphabeta_rect = alphabeta_text.get_rect(center=self.quit_button.center)
        self.screen.blit(alphabeta_text, alphabeta_rect)

        pygame.display.flip()
    
    def choose_ai_opponent(self):
        """
        Handles user input for choosing an AI opponent.

        Runs a loop until the user selects an AI bot.
        """
        choosing_opponent = True
        while choosing_opponent:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.random_ai_button.collidepoint(event.pos):
                        self.ai_bot = RandomAiBot()
                        choosing_opponent = False
                    elif self.minmax_ai_button.collidepoint(event.pos):
                        self.ai_bot = MinMaxAiBot()
                        choosing_opponent = False
                    elif self.alphabeta_ai_button.collidepoint(event.pos):
                        self.ai_bot = AlphaBetaAiBot()
                        choosing_opponent = False
                        
            self.draw_ai_bot_dialog()
            self.clock.tick(30)
            pygame.display.flip()

    def draw_board(self):
        """
        Draws the game board.

        Displays the current game state, player names, and highlights the current player's turn.
        """
        self.screen.fill(BACKGROUND_COLOR)

        # Draw player names and highlight current turn
        player1_text = self.font.render(self.player1_label, True, FONT_COLOR)
        player2_text = self.font.render(self.player2_label, True, FONT_COLOR)
        player1_rect = player1_text.get_rect(center=(CELL_SIZE * COLS // 4, CELL_SIZE // 2))
        player2_rect = player2_text.get_rect(center=(CELL_SIZE * 3 * COLS // 4, CELL_SIZE // 2))
        
        if self.player1_label == "AI":
            if self.game.turn == 1:
                pygame.draw.rect(self.screen, (255, 255, 0), player1_rect.inflate(10, 5), 0)
            else:
                pygame.draw.rect(self.screen, BACKGROUND_COLOR, player1_rect.inflate(10, 5), 0)

            if self.game.turn == 0:
                pygame.draw.rect(self.screen, (255, 255, 0), player2_rect.inflate(10, 5), 0)
            else:
                pygame.draw.rect(self.screen, BACKGROUND_COLOR, player2_rect.inflate(10, 5), 0)
        else:
            if self.game.turn == 0:
                pygame.draw.rect(self.screen, (255, 255, 0), player1_rect.inflate(10, 5), 0)
            else:
                pygame.draw.rect(self.screen, BACKGROUND_COLOR, player1_rect.inflate(10, 5), 0)

            if self.game.turn == 1:
                pygame.draw.rect(self.screen, (255, 255, 0), player2_rect.inflate(10, 5), 0)
            else:
                pygame.draw.rect(self.screen, BACKGROUND_COLOR, player2_rect.inflate(10, 5), 0)
            

        self.screen.blit(player1_text, player1_rect)
        self.screen.blit(player2_text, player2_rect)

        # Draw the board cells and discs
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(self.screen, EMPTY_COLOR, (col * CELL_SIZE, (row + 2) * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.circle(self.screen, PLAYER1_COLOR if self.game.board[row][col] == 'X' else
                                PLAYER2_COLOR if self.game.board[row][col] == 'O' else
                                EMPTY_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, (row + 2) * CELL_SIZE + CELL_SIZE // 2),
                                CELL_SIZE // 2 - 5)

        # Draw vertical lines to divide columns
        for col in range(COLS + 1):
            pygame.draw.line(self.screen, FONT_COLOR, (col * CELL_SIZE, CELL_SIZE * 2),
                            (col * CELL_SIZE, HEIGHT + CELL_SIZE - CELL_SIZE), 2)

        # Draw column numbers below player names
        for col in range(COLS):
            col_text = self.font.render(str(col + 1), True, FONT_COLOR)
            col_rect = col_text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, CELL_SIZE * 1.5))
            self.screen.blit(col_text, col_rect)

    def draw_text(self, text, position, background_color=None):
        """
        Draws text on the screen.

        Parameters:
        - text (str): The text to be displayed.
        - position (tuple): The (x, y) coordinates of the text.
        - background_color (tuple or None): The background color behind the text (optional).
        """
        if background_color:
            text_surface = self.font.render(text, True, FONT_COLOR, background_color)
        else:
            text_surface = self.font.render(text, True, FONT_COLOR)

        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect)

    def run_game(self):
        """
        Runs the main game loop.

        Handles user input for playing the game and displays game results.
        """
        self.game = ConnectFour()
        while True:
            self.run_main_menu() 
            
            self.choose_ai_opponent()

            play_again_button = pygame.Rect(WIDTH // 4 - 1, 
                                            HEIGHT // 20 + 25, 
                                            WIDTH // 4, 
                                            FONT_SIZE * 2)
            
            quit_button = pygame.Rect(WIDTH // 2 + 1, 
                                      HEIGHT // 20 + 25, 
                                      WIDTH // 4, 
                                      FONT_SIZE * 2)
            
            main_menu_button = pygame.Rect(WIDTH // 4 - 1, 
                                           HEIGHT // 20 + FONT_SIZE * 2 + 1 + 25, 
                                           WIDTH // 2 + 2, 
                                           FONT_SIZE * 2)

            while not self.ai_playing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.pos[1] > CELL_SIZE * 2:
                            column = event.pos[0] // CELL_SIZE
                            if self.game.is_valid_move(column):
                                self.drop_disc_animation(column)
                                self.game.drop_disc(column, 'X' if self.game.turn == 0 else 'O')

                self.draw_board()

                pygame.display.flip()
                self.clock.tick(30)
                
                if (self.game.is_winner('X') or self.game.is_winner('O') or self.game.is_board_full()):
                    if self.game.is_board_full():
                        winner = "You matched AI level."
                    
                    if self.game.turn == 0:
                        winner = f"AI takes over the world!"
                    elif self.game.turn == 1:
                        winner = f"You won... Cheater!"

                    margin = 10
                    
                    pygame.draw.rect(self.screen, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT/8*2))

                    pygame.draw.rect(self.screen, FONT_COLOR, play_again_button)
                    pygame.draw.rect(self.screen, FONT_COLOR, quit_button)
                    pygame.draw.rect(self.screen, FONT_COLOR, main_menu_button)
                    

                    self.draw_text(winner, (WIDTH // 2, 40), BACKGROUND_COLOR)

                    play_again_button.inflate_ip(-margin, -margin)
                    quit_button.inflate_ip(-margin, -margin)
                    main_menu_button.inflate_ip(-margin, -margin)

                    pygame.draw.rect(self.screen, BACKGROUND_COLOR, play_again_button)
                    pygame.draw.rect(self.screen, BACKGROUND_COLOR, quit_button)
                    pygame.draw.rect(self.screen, BACKGROUND_COLOR, main_menu_button)

                    # Draw text on buttons
                    play_again_text = self.font.render("Play Again", True, FONT_COLOR)
                    play_again_rect = play_again_text.get_rect(center=play_again_button.center)
                    self.screen.blit(play_again_text, play_again_rect)

                    quit_text = self.font.render("Quit", True, FONT_COLOR)
                    quit_rect = quit_text.get_rect(center=quit_button.center)
                    self.screen.blit(quit_text, quit_rect)

                    main_menu_text = self.font.render("Main Menu", True, FONT_COLOR)
                    main_menu_rect = main_menu_text.get_rect(center=main_menu_button.center)
                    self.screen.blit(main_menu_text, main_menu_rect)
                    
                    pygame.display.flip()

                    waiting_for_input = True
                    while waiting_for_input:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                if play_again_button.collidepoint(event.pos):
                                    if self.player1_label == "AI":
                                        last_game_first = 1
                                    else:
                                        last_game_first = 0
                                        
                                    self.game = ConnectFour()
                                    self.game.turn = last_game_first
                                    waiting_for_input = False
                                    
                                elif quit_button.collidepoint(event.pos):
                                    pygame.quit()
                                    sys.exit()
                                
                                elif main_menu_button.collidepoint(event.pos):
                                    self.run_game()
                                    waiting_for_input = False
                                    
                if self.game.turn == 1 and not self.ai_playing:
                    self.ai_playing = True
                    pygame.time.delay(1000)

                    # AI's turn
                    column = self.ai_bot.choose_move(self.game)
                    if column is not None:
                        self.drop_disc_animation(column)
                        self.game.drop_disc(column, 'O')

                    self.ai_playing = False
                
                

    def drop_disc_animation(self, col):
        """
        Animates the dropping of a disc into a column.

        Parameters:
        - col (int): The column where the disc is dropped.
        """
        row = 0
        while row < ROWS:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BACKGROUND_COLOR)
            self.draw_board()
            pygame.draw.circle(self.screen, PLAYER1_COLOR if self.game.turn == 0 else PLAYER2_COLOR,
                               (col * CELL_SIZE + CELL_SIZE // 2, (row + 2) * CELL_SIZE + CELL_SIZE // 2),
                               CELL_SIZE // 2 - 5)
            pygame.display.flip()
            pygame.time.delay(50)
            row += 1
            
