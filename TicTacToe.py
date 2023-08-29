import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 60
OVERLAY_ALPHA = 128  # Transparency level for overlay

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
def reset_game():
    global board, player_turn, game_over
    board = [['' for _ in range(3)] for _ in range(3)]
    player_turn = 'X'
    game_over = False

reset_game()

# Draw the Tic Tac Toe grid
def draw_grid():
    for row in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, row * HEIGHT // 3), (WIDTH, row * HEIGHT // 3), 5)
        pygame.draw.line(screen, LINE_COLOR, (row * WIDTH // 3, 0), (row * WIDTH // 3, HEIGHT), 5)

# Check for a win or draw
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
            return board[row][0]
        if board[0][row] == board[1][row] == board[2][row] and board[0][row] != '':
            return board[0][row]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    if all(board[row][col] != '' for row in range(3) for col in range(3)):
        return 'Draw'
    return None

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // (HEIGHT // 3)
            clicked_col = mouseX // (WIDTH // 3)
            
            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = player_turn
                player_turn = 'O' if player_turn == 'X' else 'X'
                
                winner = check_winner()
                if winner:
                    game_over = True

        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                reset_game()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            
    # Clear the screen
    screen.fill(BACKGROUND_COLOR)
    
    # Draw the grid
    draw_grid()

    # Draw X's and O's
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                text = font.render('X', True, FONT_COLOR)
                text_rect = text.get_rect(center=((col * WIDTH // 3) + WIDTH // 6, (row * HEIGHT // 3) + HEIGHT // 6))
                screen.blit(text, text_rect)
            elif board[row][col] == 'O':
                text = font.render('O', True, FONT_COLOR)
                text_rect = text.get_rect(center=((col * WIDTH // 3) + WIDTH // 6, (row * HEIGHT // 3) + HEIGHT // 6))
                screen.blit(text, text_rect)
    
    # Display game result and overlay
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(OVERLAY_ALPHA)
        overlay.fill(BACKGROUND_COLOR)
        screen.blit(overlay, (0, 0))
        
        result_text = None
        if winner == 'Draw':
            result_text = font.render('It\'s a Draw!', True, FONT_COLOR)
        else:
            result_text = font.render(f'{winner} wins!', True, FONT_COLOR)
        result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(result_text, result_rect)
        
        play_again_text = font.render('Press R to play again', True, FONT_COLOR)
        play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(play_again_text, play_again_rect)
        
        quit_text = font.render('Press Q to quit', True, FONT_COLOR)
        quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 160))
        screen.blit(quit_text, quit_rect)

    # Update the display
    pygame.display.flip()

# Close Pygame
pygame.quit()
sys.exit()
