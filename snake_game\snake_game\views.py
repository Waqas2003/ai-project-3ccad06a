import pygame
import sys
from .models import Snake, Food
from .constants import WIDTH, HEIGHT, BLOCK_SIZE, SPEED

def draw_snake(snake, screen):
    for pos in snake.body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

def draw_food(food, screen):
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food.position[0], food.position[1], BLOCK_SIZE, BLOCK_SIZE))

def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != 'DOWN':
                    snake.direction = 'UP'
                elif event.key == pygame.K_DOWN and snake.direction != 'UP':
                    snake.direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake.direction != 'RIGHT':
                    snake.direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake.direction != 'LEFT':
                    snake.direction = 'RIGHT'
        snake.move()
        if snake.eat(food.position):
            food.generate()
        screen.fill((0, 0, 0))
        draw_snake(snake, screen)
        draw_food(food, screen)
        pygame.display.update()
        clock.tick(SPEED)