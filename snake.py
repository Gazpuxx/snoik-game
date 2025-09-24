import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Set up clock for controlling the frame rate
clock = pygame.time.Clock()
SPEED = 10  # Controls how many frames per second (snake speed)

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake initial settings
def init_snake():
    x = WIDTH // 2
    y = HEIGHT // 2
    return [(x, y), (x - CELL_SIZE, y), (x - 2 * CELL_SIZE, y)]

# Place food randomly on the grid
def place_food(snake):
    while True:
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        if (x, y) not in snake:
            return (x, y)

# Draw everything on the screen
def draw(snake, food, score):
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# Main game function
def main():
    snake = init_snake()
    direction = (CELL_SIZE, 0)  # Start moving right
    food = place_food(snake)
    score = 0
    running = True
    
    while running:
        clock.tick(SPEED)  # This controls the speed of the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Change direction based on key pressed
                elif event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

        # Move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        # Check for collisions with walls or self
        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake
        ):
            break  # Game over
        snake.insert(0, new_head)
        # Check if snake eats food
        if new_head == food:
            score += 1
            food = place_food(snake)
        else:
            snake.pop()  # Remove tail if not eating
        draw(snake, food, score)

    # Game over screen
    font = pygame.font.SysFont(None, 48)
    text = font.render('Game Over!', True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2 - 24))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
