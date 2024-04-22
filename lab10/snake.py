import psycopg2
import pygame
import random
import sys
from config import *

# Constants
WIDTH, HEIGHT = 400, 300
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 5.25
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 51)


def Score_snake():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS Score_snake (user_name VARCHAR(64) NOT NULL PRIMARY KEY, user_score BIGINT NOT NULL);"
            )
            print("Table created")

    except Exception as ex:
        print("[INFO] Error while creating table:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")


def insert_user_score(user_name, user_score):
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True

        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Score_snake (user_name, user_score)
                VALUES (%s, %s)
            """, (user_name, user_score))

        print("Score inserted successfully.")

    except Exception as ex:
        print("[INFO] Error while inserting score:", ex)

    finally:
        if connection:
            connection.close()
            print("[INFO] Postgres connection closed")


# Snake class
class Snake:
    def __init__(self):
        self.head = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
        self.body = [[self.head[0], self.head[1]], [
            self.head[0] - 1, self.head[1]], [self.head[0] - 2, self.head[1]]]
        self.direction = 'RIGHT'

    def change_direction(self, direction):
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'

    def move(self):
        if self.direction == 'RIGHT':
            self.head[0] += 1
        elif self.direction == 'LEFT':
            self.head[0] -= 1
        elif self.direction == 'UP':
            self.head[1] -= 1
        elif self.direction == 'DOWN':
            self.head[1] += 1

        self.body.insert(0, list(self.head))
        self.body.pop()  # Remove the last segment

    def grow(self):
        self.body.insert(0, list(self.head))

    def collide_with_wall(self):
        if self.head[0] < 0 or self.head[0] >= GRID_WIDTH or self.head[1] < 0 or self.head[1] >= GRID_HEIGHT:
            return True
        return False

    def collide_with_self(self):
        if self.head in self.body[1:]:
            return True
        return False

# Food class


class Food:
    def __init__(self):
        self.position = [random.randrange(
            0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)]
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = [random.randrange(
                0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)]
            self.is_food_on_screen = True
        return self.position

# Weight food class


class Weight_Food:
    def __init__(self):
        self.position = [random.randrange(
            0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)]
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = [random.randrange(
                0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)]
            self.is_food_on_screen = True
        return self.position

# Timed Food class


class TimedFood:
    def __init__(self, delay):
        self.position = None
        self.is_food_on_screen = False
        self.delay = delay
        self.timer = 0

    def update(self):
        self.timer += 1
        if self.timer >= self.delay:
            self.position = [random.randrange(
                0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)]
            self.is_food_on_screen = True
            self.timer = 0

    def spawn_food(self):
        return self.position


# Функция отображения текста в центре экрана
def display_centered_text_gameover(screen, text, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)


def display_centered_text_score(screen, text, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 1.5))
    screen.blit(text_surface, text_rect)


def display_centered_text_score_coins(screen, text, font_size, color):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 1.2))
    screen.blit(text_surface, text_rect)


user_name = input("your name:")


def main(user_name):

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    # Initialize game objects
    snake = Snake()
    food = Food()
    WeightFood = Weight_Food()
    timed_food = TimedFood(8)
    apples_eaten = 0
    points = 0

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')

        # Move snake and update game objects
        snake.move()

        # Check for collisions
        if snake.collide_with_wall() or snake.collide_with_self():
            screen.fill(RED)
            display_centered_text_gameover(screen, "Game Over", 36, WHITE)
            display_centered_text_score(screen, f"Points: {points}", 24, WHITE)
            display_centered_text_score_coins(
                screen, f"Apples eaten: {apples_eaten}", 12, WHITE)
            pygame.display.update()
            insert_user_score(user_name, points)  # Save user score
            pygame.quit()
            sys.exit()

        # Process eaten apples and display statistics
        if snake.head == food.position:
            snake.grow()
            food.is_food_on_screen = False
            points += 1
            apples_eaten += 1

        if snake.head == WeightFood.position:
            snake.grow()
            WeightFood.is_food_on_screen = False
            points += 2
            apples_eaten += 1

        if snake.head == timed_food.position:
            snake.grow()
            timed_food.is_food_on_screen = False
            points += 5
            apples_eaten += 1

        # Clear the screen
        screen.fill(BLACK)

        # Draw food
        food_position = food.spawn_food()
        pygame.draw.rect(
            screen, RED, (food_position[0] * GRID_SIZE, food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        WeightFood_position = WeightFood.spawn_food()
        pygame.draw.rect(
            screen, YELLOW, (WeightFood_position[0] * GRID_SIZE, WeightFood_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw timed food
        timed_food.update()
        if timed_food.is_food_on_screen:
            timed_food_position = timed_food.spawn_food()
            pygame.draw.rect(screen, (50, 50, 50), (
                timed_food_position[0] * GRID_SIZE, timed_food_position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Draw snake
        for segment in snake.body:
            pygame.draw.rect(
                screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        # Update the screen
        pygame.display.update()
        clock.tick(FPS)


Score_snake()
if __name__ == "__main__":
    main(user_name)
