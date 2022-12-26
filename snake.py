import random
import pygame

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (600, 600)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Snake")

# Set the frame rate
fps = 10

# Set the size of the snake and food blocks
block_size = 20

# Set the initial position of the snake
snake_pos = [100, 50]

# Set the initial snake body
snake_body = [[100, 50], [90, 50], [80, 50]]

# Set the initial direction of the snake
direction = "RIGHT"

# Set the initial position of the food
food_pos = [300, 300]
food_spawn = True

# Set the score to 0
score = 0

# Set the game over flag to False
game_over = False

# Set the colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Set the font
font = pygame.font.SysFont("monospace", 35)

# Set the clock
clock = pygame.time.Clock()

# Function to draw the snake
def draw_snake(snake_pos, block_size):
    for pos in snake_pos:
        # Draw the snake block with a detailed texture
        snake_block = pygame.Surface((block_size, block_size))
        snake_block.fill(green)
        snake_block_rect = snake_block.get_rect()
        snake_block_rect.topleft = pos
        screen.blit(snake_block, snake_block_rect)

# Function to draw the food
def draw_food(food_pos, block_size):
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            elif event.key == pygame.K_DOWN:
                direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                direction = "RIGHT"

    # Update the snake position
    if direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "RIGHT":
        snake_pos[0] += 10

    # Update the snake body
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0]//block_size)) * block_size,
                    random.randrange(1, (window_size[1]//block_size)) * block_size]
    food_spawn = True

    screen.fill(black)
    draw_snake(snake_body, block_size)
    draw_food(food_pos, block_size)
    pygame.display.update()

    # Check for game over
    if snake_pos[0] < 0 or snake_pos[0] > window_size[0] or snake_pos[1] < 0 or snake_pos[1] > window_size[1]:
        game_over = True
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Set the frame rate
    clock.tick(fps)

# Display the game over message
while True:
    game_over_font = pygame.font.SysFont("monospace", 75)
    game_over_screen = game_over_font.render("Game Over", True, red)
    screen.blit(game_over_screen, (window_size[0]//2 - game_over_screen.get_width() // 2, window_size[1]//2 - game_over_screen.get_height() // 2))