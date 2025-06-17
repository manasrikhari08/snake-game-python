# importing libraries
import pygame
import time
import random

snake_speed = 15

# Window size
window_x = 1024
window_y = 768

# defining colors
black = pygame.Color(10,10,10) #background color
green = pygame.Color(255,195,113)# snake color
white = pygame.Color(0,128,255) #fruit color
red = pygame.Color(80,40,40)# game over color
blue = pygame.Color(0, 0, 255)


# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Manas_gameing_MG')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0

# displaying Score function
def show_score(choice, color, font, size):
  
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
    
    # create the display surface object 
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    
    # displaying text
    game_window.blit(score_surface, score_rect)

# game over function
def game_over():
  
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # creating a text surface on which text 
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    
    # create a rectangular object for the text 
    # surface object
    game_over_rect = game_over_surface.get_rect()
    
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
    
    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # after 3 seconds we will quit the program
    time.sleep(3)
    
    # deactivating pygame library
    pygame.quit()
    
    # quit the program
    quit()


# Main Function
# Main Function
while True:
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validating direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move snake
    if direction == 'UP':
        snake_position[1] -= 10
    elif direction == 'DOWN':
        snake_position[1] += 10
    elif direction == 'LEFT':
        snake_position[0] -= 10
    elif direction == 'RIGHT':
        snake_position[0] += 10

    # Grow snake
    snake_body.insert(0, list(snake_position))
    if snake_position == fruit_position:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, window_x // 10) * 10,
                          random.randrange(1, window_y // 10) * 10]
    fruit_spawn = True

    # Fill background
    game_window.fill(black)

    # Colors for snake body
    body_colors = [pygame.Color(0, 150, 0), pygame.Color(0, 120, 0)]

    # Draw snake
    for i, pos in enumerate(snake_body):
        if i == 0:
            pygame.draw.ellipse(game_window, pygame.Color(0, 200, 0), pygame.Rect(pos[0], pos[1], 15, 15))
            pygame.draw.circle(game_window, white, (pos[0] + 4, pos[1] + 4), 2)
            pygame.draw.circle(game_window, white, (pos[0] + 10, pos[1] + 4), 2)
            pygame.draw.line(game_window, red, (pos[0] + 7, pos[1] + 13), (pos[0] + 7, pos[1] + 20), 2)
        else:
            color = body_colors[i % 2]
            pygame.draw.ellipse(game_window, color, pygame.Rect(pos[0], pos[1], 12, 12))

    # Draw fruit
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    # Show score
    show_score(1, white, 'times new roman', 20)

    # Update display
    pygame.display.update()

    # Control speed
    fps.tick(snake_speed)
