import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 128, 0)  # Green
FONT_COLOR = (255, 255, 255)    # White
FONT_SIZE = 30

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cricket Game")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
player_score = 0
ai_choice = None
out = False

# Function to reset the game
def reset_game():
    global player_score, ai_choice, out
    player_score = 0
    ai_choice = None
    out = False

# Function to play the AI's turn
def play_ai_turn():
    return random.randint(1, 6)

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not out:
            if pygame.K_1 <= event.key <= pygame.K_6:  # Check if key is 1 to 6
                player_choice = event.key - pygame.K_0  # Convert key constant to numerical value
                ai_choice = play_ai_turn()

                if player_choice == ai_choice:
                    out = True
                else:
                    player_score += player_choice

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Display player score
    player_text = font.render(f'Your Score: {player_score}', True, FONT_COLOR)
    player_rect = player_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(player_text, player_rect)

    # Display AI choice if it's available
    if ai_choice is not None:
        ai_text = font.render(f'AI Chose: {ai_choice}', True, FONT_COLOR)
        ai_rect = ai_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(ai_text, ai_rect)

    # Display game status
    status_text = font.render('You are out!' if out else 'Choose a number (1-6)', True, FONT_COLOR)
    status_rect = status_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(status_text, status_rect)

    # Update the display
    pygame.display.flip()

    # Play again if 'R' key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        reset_game()

# Close Pygame
pygame.quit()
sys.exit()
