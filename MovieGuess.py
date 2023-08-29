import pygame
import sys
import random

# Initialize Pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30

# Load movie names from the text file (between , and ( )
def load_movie_names(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        movie_names = []
        for line in lines:
            start_idx = line.find(',') + 1
            end_idx = line.find('(') if '(' in line else len(line)
            movie_name = line[start_idx:end_idx].strip()
            if movie_name:
                movie_names.append(movie_name.lower())
    return movie_names

# Select a random movie name
def choose_random_movie(movie_list):
    return random.choice(movie_list)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Movie")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Load movie names from text file
movie_names = load_movie_names('movies.txt')

# Choose a random movie
selected_movie = choose_random_movie(movie_names)

# Game variables
guesses = set()
chances = 9 # Number of chances is the length of the selected movie
game_over = False

# Function to reset the game
def reset_game():
    global selected_movie, guesses, chances, game_over
    selected_movie = choose_random_movie(movie_names)
    guesses = set()
    chances = 9
    game_over = False

# Check if all blanks in guessed movie are filled
def all_blanks_filled(selected_movie, guesses):
    for letter in selected_movie:
        if letter.isalpha() and letter not in guesses:
            return False
    return True

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.unicode.isalnum() and event.unicode not in guesses:
                guesses.add(event.unicode.lower())
                if event.unicode.lower() not in selected_movie:
                    chances -= 1
                if all_blanks_filled(selected_movie, guesses) or chances == 0:
                    game_over = True

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Display movie name with vowels and underscores
    display_text = ''
    for letter in selected_movie:
        if letter in 'aeiou':
            display_text += letter
        elif letter == ' ':
            display_text += ' '
        else:
            display_text += '_' if letter not in guesses else letter
    text = font.render(display_text, True, FONT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)

    # Display chances remaining
    chances_text = font.render(f'Chances left: {chances}', True, FONT_COLOR)
    chances_rect = chances_text.get_rect(topleft=(20, 20))
    screen.blit(chances_text, chances_rect)

    # Display game result
    if game_over:
        result_text = None
        movie_name_text = font.render(f'Movie: {selected_movie}', True, FONT_COLOR)
        movie_name_rect = movie_name_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(movie_name_text, movie_name_rect)
        
        if all_blanks_filled(selected_movie, guesses):
            result_text = font.render('Congratulations - You won!', True, FONT_COLOR)
        else:
            result_text = font.render('Game Over - You lost!', True, FONT_COLOR)
        result_rect = result_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        screen.blit(result_text, result_rect)
        
        play_again_text = font.render('Press R to play again', True, FONT_COLOR)
        play_again_rect = play_again_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
        screen.blit(play_again_text, play_again_rect)

    # Update the display
    pygame.display.flip()

    # Play again if 'R' key is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r] and game_over:
        reset_game()

# Close Pygame
pygame.quit()
sys.exit()
