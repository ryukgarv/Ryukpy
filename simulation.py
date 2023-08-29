import pygame
import sys
import importlib

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (155, 255, 155)
RECTANGLE_COLOR = (155, 155, 255)
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 30

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Selection")

# Load font
font = pygame.font.Font(None, FONT_SIZE)

# Define rectangles for game selection
game_rectangles = [
    pygame.Rect(100, 150, 200, 100),
    pygame.Rect(500, 150, 200, 100),
    pygame.Rect(100, 350, 200, 100),
    pygame.Rect(500, 350, 200, 100)
]

game_names = ["Tic Tac Toe", "Runner", "Movie Guess", "cricket"]
selected_game = None

# Function to draw rectangles and text
def draw_game_selection():
    screen.fill(BACKGROUND_COLOR)
    for idx, rect in enumerate(game_rectangles):
        pygame.draw.rect(screen, RECTANGLE_COLOR, rect)
        text = font.render(game_names[idx], True, FONT_COLOR)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    pygame.display.flip()

# Function to execute a Python file
def execute_python_file(file_path):
    try:
        module_name = file_path.replace('.py', '')  # Remove the '.py' extension
        module = importlib.import_module(module_name)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except ModuleNotFoundError:
        print(f"Error: The module '{module_name}' could not be found.")
    except ImportError as e:
        print(f"Error: Unable to import '{module_name}': {e}")

# Function to select and play a game
def select_and_play_game():
    global selected_game
    selecting_game = True
    while selecting_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for idx, rect in enumerate(game_rectangles):
                    if rect.collidepoint(mouse_pos):
                        selected_game = game_names[idx]
                        selecting_game = False

        draw_game_selection()

    # Close Pygame window
    pygame.quit()

    # Execute the selected game's Python file
    if selected_game:
        execute_python_file(selected_game.replace(" ", "") + '.py')
        
    # Reload the game selection window
    pygame.init()
    select_and_play_game()

# Start the game selection loop
select_and_play_game()
