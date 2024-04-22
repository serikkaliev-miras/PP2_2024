# 1
import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH // 10))
            * 10, random.randrange(1, (SCREEN_HEIGHT // 10))*10]
food_spawn = True

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
dir = RIGHT

score = 0
level = 1
snake_speed = 15

game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != DOWN:
                dir = UP
            elif event.key == pygame.K_DOWN and dir != UP:
                dir = DOWN
            elif event.key == pygame.K_LEFT and dir != RIGHT:
                dir = LEFT
            elif event.key == pygame.K_RIGHT and dir != LEFT:
                dir = RIGHT
            elif event.key == pygame.K_SPACE:
                snake_speed = 0

    if dir == UP:
        snake_pos[1] -= 10
    elif dir == DOWN:
        snake_pos[1] += 10
    elif dir == LEFT:
        snake_pos[0] -= 10
    elif dir == RIGHT:
        snake_pos[0] += 10

    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - 10:
        game_over = True

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(
            1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        food_spawn = True

    snake_body.insert(0, list(snake_pos))

    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, RED, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score) +
                       "   Level: " + str(level), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

    if score > level * 3:
        level += 1
        snake_speed += 5

    clock.tick(snake_speed)

pygame.quit()
# 2
# import pygame
# import time
# import random

# pygame.init()

# # Установка цветов
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# orange = (255, 165, 0)

# WIDTH, HEIGHT = 600, 400

# # Установка экрана
# screen = pygame.display.set_mode([WIDTH, HEIGHT])
# pygame.display.set_caption("Змейка")

# clock = pygame.time.Clock()

# snake_size = 10
# snake_speed = 5  # Тут мы можем регулировать скорость нашей змеи. Больше пикселей в секунуду -> Быстрее змея

# message_font = pygame.font.SysFont('ubuntu', 30)
# score_font = pygame.font.SysFont('ubuntu', 25)
# level_font = pygame.font.SysFont('ubuntu', 30)
# # Определение функций


# def print_score(score):
#     text = score_font.render("Score " + str(score), True, orange)
#     screen.blit(text, [0, 0])


# def print_level(level):
#     text = level_font.render("Level: " + str(level), True, orange)
#     screen.blit(text, [WIDTH - 150, 0])


# def draw_snake(snake_size, snake_pixels):
#     for pixel in snake_pixels:
#         pygame.draw.rect(
#             screen, white, [pixel[0], pixel[1], snake_size, snake_size])


# def run_game():
#     global snake_speed

#     game_over = False
#     game_close = False

#     x = WIDTH / 2
#     y = HEIGHT / 2

#     x_speed = 0
#     y_speed = 0

#     snake_pixels = []
#     snake_length = 1

#     # Отвечает за положение нашего яблоко, для этого даем ему рандомные значения по
#     target_x = round(random.randrange(0, WIDTH-snake_size) / 10.0) * 10.0
#     # X и Y осям.
#     target_y = round(random.randrange(0, HEIGHT-snake_size) / 10.0) * 10.0

#     level = 1

#     while not game_over:  # Game Loop

#         while game_close:
#             screen.fill(black)
#             # Это все можно вывести за наш гейм луп в отдельную функцию
#             game_over_message = message_font.render("Game Over", True, red)
#             screen.blit(game_over_message, [WIDTH / 3, HEIGHT / 3])
#             print_score(snake_length - 1)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_1:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_2:
#                         run_game()
#                     if event.type == pygame.QUIT:
#                         game_over = True
#                         game_close = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True

#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     # Так как наше начальное положение змеи это центр экрана, для движения змеи
#                     x_speed = -snake_size
#                     # Мы имеем право сказать, что мы можем двигать ее по x-у или y-у на длину snake_size
#                     y_speed = 0

#                 if event.key == pygame.K_RIGHT:

#                     x_speed = snake_size
#                     y_speed = 0

#                 if event.key == pygame.K_UP:
#                     x_speed = 0
#                     y_speed = -snake_size

#                 if event.key == pygame.K_DOWN:
#                     x_speed = 0
#                     y_speed = snake_size

#         # Если координаты нашей змеи косаются наших границ экрана, то игра заканчивается
#         if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
#             game_close = True

#         x += x_speed  # Для изменения головы нашей змеи мы создаем зависимость скорость от координат
#         y += y_speed

#         screen.fill(black)
#         # Отрисовка нашего яблока
#         pygame.draw.rect(screen, orange, [
#                          target_x, target_y, snake_size, snake_size])

#         snake_pixels.append([x, y])  # Нам нужно хранить все пиксели нашей змеи

#         if len(snake_pixels) > snake_length:
#             del snake_pixels[0]

#         for pixel in snake_pixels[:-1]:  # Змея столкнулась сама с собой
#             if pixel == [x, y]:
#                 game_close = True

#         draw_snake(snake_size, snake_pixels)
#         print_score(snake_length - 1)
#         print_level(level)

#         pygame.display.update()

#         if x == target_x and y == target_y:
#             target_x = round(random.randrange(
#                 0, WIDTH-snake_size) / 10.0) * 10.0
#             target_y = round(random.randrange(
#                 0, HEIGHT-snake_size) / 10.0) * 10.0
#             snake_length += 1
#             level += 1
#             snake_speed += 2  # Увеличиваем скорость змеи

#         clock.tick(snake_speed)

#     pygame.quit()
#     quit()


# run_game()

# 3
# import pygame  # Import the Pygame library
# # Import color constants from color_palette module
# import time  # Import the time module for time-related functions
# import random  # Import the random module for random number generation

# pygame.init()  # Initialize Pygame

# # Define constants for the game window size and cell size
# WIDTH = 600
# HEIGHT = 600
# CELL = 30
# colorWHITE = (255, 255, 255)
# colorGRAY = (200, 200, 200)
# colorBLACK = (0, 0, 0)
# colorRED = (255, 0, 0)
# colorGREEN = (0, 255, 0)
# colorBLUE = (0, 0, 255)
# colorYELLOW = (255, 255, 0)

# # Initialize variables for game level, score, and snake speed
# level = 1
# score = 0
# snake_speed = 5

# # Function to draw the grid lines


# def draw_grid():
#     for i in range(HEIGHT // 2):
#         for j in range(WIDTH // 2):
#             pygame.draw.rect(screen, colorGRAY,
#                              (i * CELL, j * CELL, CELL, CELL), 1)

# # Function to draw a chessboard pattern on the grid


# def draw_grid_chess():
#     colors = [colorWHITE, colorGRAY]

#     for i in range(HEIGHT // 2):
#         for j in range(WIDTH // 2):
#             pygame.draw.rect(
#                 screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


# # Create the game window surface
# screen = pygame.display.set_mode((HEIGHT, WIDTH))

# # Define a Point class to represent coordinates


# class Point:
#     def __init__(self, x, y):  # Initialize with x and y coordinates
#         self.x = x
#         self.y = y

#     def __str__(self):  # Define a string representation for debugging
#         return f"{self.x}, {self.y}"

# # Define the Snake class


# class Snake:
#     def __init__(self):  # Initialize the snake with a starting body
#         self.body = [Point(10, 11), Point(10, 12),
#                      Point(10, 13)]  # Initial snake body
#         self.dx = 1  # Initial movement direction along x-axis
#         self.dy = 0  # Initial movement direction along y-axis

#     def move(self):  # Method to move the snake
#         for i in range(len(self.body) - 1, 0, -1):  # Iterate through the snake's body
#             # Move each segment of the body
#             self.body[i].x = self.body[i - 1].x
#             self.body[i].y = self.body[i - 1].y

#         # Move the head of the snake based on direction
#         self.body[0].x += self.dx
#         self.body[0].y += self.dy

#         # Check if the snake hits the boundary, return False to indicate game over
#         if self.body[0].x == -1 or self.body[0].x == 20 or self.body[0].y == -1 or self.body[0].y == 20:
#             return False

#     def draw(self):  # Method to draw the snake on the screen
#         head = self.body[0]  # Get the head of the snake
#         pygame.draw.rect(screen, colorGREEN, (head.x * CELL,
#                          head.y * CELL, CELL, CELL))  # Draw the head
#         for segment in self.body[1:]:  # Iterate through the body segments
#             pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL,
#                              segment.y * CELL, CELL, CELL))  # Draw each segment

#     def check_collision(self, food):  # Method to check collision with food
#         head = self.body[0]  # Get the head of the snake
#         if head.x == food.pos.x and head.y == food.pos.y:  # If snake head overlaps with food
#             print("Got food!")  # Print message indicating food is eaten
#             # Add a new segment to the snake's body
#             self.body.append(Point(head.x, head.y))
#             pygame.display.update()  # Update the display
#             food.change_pos()  # Change the position of the food

# # Define the Food class


# class Food:
#     def __init__(self):  # Initialize food with a random position
#         # Random position within grid
#         self.pos = Point(random.randrange(0, 19), random.randrange(0, 19))

#     # Method to generate a new position for food
#     def generate_new_position(self):
#         # Generate a new random position
#         new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))
#         while new_pos in snake.body:  # Keep generating until position is not inside snake's body
#             new_pos = Point(random.randrange(0, 19), random.randrange(0, 19))
#         return new_pos  # Return the valid new position

#     def change_pos(self):  # Method to change food position
#         global score  # Access the global score variable
#         # Generate a new valid position for food
#         self.pos = self.generate_new_position()
#         score += 1  # Increment the score when food is eaten

#     def draw(self):  # Method to draw the food on the screen
#         pygame.draw.rect(screen, colorRED, (self.pos.x * CELL,
#                          self.pos.y * CELL, CELL, CELL))  # Draw the food


# # Create a clock object to control game speed
# clock = pygame.time.Clock()

# # Create instances of Food and Snake classes
# food = Food()  # Initialize food
# snake = Snake()  # Initialize snake

# # Define the font and text for game over message
# font = pygame.font.SysFont("Verdana", 60)
# game__over = font.render("Game Over", True, colorBLACK)

# # Main game loop
# done = False
# while not done:  # Continue loop until done is True
#     for event in pygame.event.get():  # Iterate through events
#         if event.type == pygame.QUIT:  # If user closes the window
#             done = True  # Set done to True to exit the loop
#         if event.type == pygame.KEYDOWN:  # If a key is pressed
#             if event.key == pygame.K_RIGHT and snake.dx != -1:  # Right arrow key
#                 snake.dx = 1  # Set direction to move right
#                 snake.dy = 0
#             elif event.key == pygame.K_LEFT and snake.dx != 1:  # Left arrow key
#                 snake.dx = -1  # Set direction to move left
#                 snake.dy = 0
#             elif event.key == pygame.K_DOWN and snake.dy != -1:  # Down arrow key
#                 snake.dx = 0  # Set direction to move down
#                 snake.dy = 1
#             elif event.key == pygame.K_UP and snake.dy != 1:  # Up arrow key
#                 snake.dx = 0  # Set direction to move up
#                 snake.dy = -1

#     draw_grid_chess()  # Draw the chessboard grid

#     # Define font for score and level display
#     font = pygame.font.SysFont(None, 25)
#     text = font.render("Score: " + str(score) + "   Level: " +
#                        # Render score and level text
#                        str(level), True, colorBLACK)
#     screen.blit(text, (10, 10))  # Draw the text on the screen

#     if snake.move() == False:  # If snake movement returns False (game over condition)
#         done = True  # Set done to True to exit the loop

#         screen.fill(colorRED)  # Fill the screen with red
#         screen.blit(game__over, (125, 225))  # Display game over message

#         pygame.display.update()  # Update the display
#         time.sleep(2)  # Pause for 2 seconds before exiting

#     snake.check_collision(food)  # Check collision with food

#     if score > level * 3:  # If score exceeds three times the level
#         level += 1  # Increase the level
#         snake_speed += 3  # Increase the snake's speed

#     snake.draw()  # Draw the snake
#     food.draw()  # Draw the food

#     pygame.display.flip()  # Update the entire display
#     clock.tick(snake_speed)  # Control game speed based on snake's speed

# 1
# import pygame
# import random

# pygame.init()

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# SCREEN_WIDTH = 600
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Snake Game")

# snake_pos = [100, 50]
# snake_body = [[100, 50], [90, 50], [80, 50]]
# food_pos = [random.randrange(1, (SCREEN_WIDTH // 10))
#             * 10, random.randrange(1, (SCREEN_HEIGHT // 10))*10]
# food_spawn = True

# UP = 0
# DOWN = 1
# LEFT = 2
# RIGHT = 3
# dir = RIGHT

# score = 0
# level = 1
# snake_speed = 15

# game_over = False
# clock = pygame.time.Clock()

# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP and dir != DOWN:
#                 dir = UP
#             elif event.key == pygame.K_DOWN and dir != UP:
#                 dir = DOWN
#             elif event.key == pygame.K_LEFT and dir != RIGHT:
#                 dir = LEFT
#             elif event.key == pygame.K_RIGHT and dir != LEFT:
#                 dir = RIGHT

#     if dir == UP:
#         snake_pos[1] -= 10
#     elif dir == DOWN:
#         snake_pos[1] += 10
#     elif dir == LEFT:
#         snake_pos[0] -= 10
#     elif dir == RIGHT:
#         snake_pos[0] += 10

#     if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - 10:
#         game_over = True

#     if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
#         score += 1
#         food_spawn = False
#     else:
#         snake_body.pop()

#     if not food_spawn:
#         food_pos = [random.randrange(
#             1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
#         food_spawn = True

#     snake_body.insert(0, list(snake_pos))

#     screen.fill(BLACK)
# ----------------------------------------------------------------------------------
#     # for i, pos in enumerate(snake_body):
#     #     if i == 0:
#     #         pygame.draw.rect(screen, GREEN, pygame.Rect(
#     #             pos[0], pos[1], 10, 10))
#     #     else:
#     #         pygame.draw.rect(screen, WHITE, pygame.Rect(
#     #             pos[0], pos[1], 10, 10))
# ----------------------------------------------------------------------------------
#     pygame.draw.rect(screen, RED, pygame.Rect(
#         food_pos[0], food_pos[1], 10, 10))

#     font = pygame.font.SysFont(None, 25)
#     text = font.render("Score: " + str(score) +
#                        "   Level: " + str(level), True, WHITE)
#     screen.blit(text, (10, 10))

#     pygame.display.update()

#     if score > level * 3:
#         level += 1
#         snake_speed += 5

#     clock.tick(snake_speed)

# pygame.quit()
