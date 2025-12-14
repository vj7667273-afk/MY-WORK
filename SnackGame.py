import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define game variables
cell_size = 20
snake_speed = 10

# Define the snake
snake = [(width // 2, height // 2)]
snake_direction = "RIGHT"

# Define the food
food_position = (
    (random.randint(0, width // cell_size - 1)) * cell_size,
    (random.randint(0, height // cell_size - 1)) * cell_size
)

# Define the score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    snake_head = list(snake[0])
    if snake_direction == "UP":
        snake_head[1] -= cell_size
    elif snake_direction == "DOWN":
        snake_head[1] += cell_size
    elif snake_direction == "LEFT":
        snake_head[0] -= cell_size
    elif snake_direction == "RIGHT":
        snake_head[0] += cell_size

    snake.insert(0, tuple(snake_head))

    # Check for collision with the food
    if snake[0] == food_position:
        score += 1
        food_position = (
            (random.randint(0, width // cell_size - 1)) * cell_size,
            (random.randint(0, height // cell_size - 1)) * cell_size
        )
    else:
        snake.pop()

    # Check for collision with snake's body
    if snake[0] in snake[1:]:
        running = False

    # Check for collision with the screen boundaries
    if (snake[0][0] < 0 or snake[0][0] >= width or
        snake[0][1] < 0 or snake[0][1] >= height):
        running = False

    # Refresh the screen
    window.fill(BLACK)
    for position in snake:
        pygame.draw.rect(window, GREEN, (position[0], position[1], cell_size, cell_size))
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], cell_size, cell_size))

    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
