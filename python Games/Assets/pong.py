import pygame
import sys
from random import * 
x=2
# Initialize pygame
pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption('Pong Arcade')
# Set up the screen.
size = (940, 788)
screen = pygame.display.set_mode(size)

# Set up the game variables
paddle1_pos = [29, 300]
paddle2_pos = [891, 300]
paddle_width = 20
paddle_height = 100
paddle_speed = 5

ball_pos = [470, 394]
ball_radius = 15
ball_speed_x = 3
ball_speed_y = 3

player1_score = 0
player2_score = 0

background_surface=pygame.image.load('D:/Kamlesh/python games/Assets/bg.jpg').convert()
# Initialize font
font = pygame.font.Font('D:/Kamlesh/python games/Assets/digital-7 (italic).ttf', 90)

# Start the main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if paddle1_pos[1]<=0:
            pass
        else:
            paddle1_pos[1] -= paddle_speed
    if keys[pygame.K_s]:
        if paddle1_pos[1]>=688:
            pass
        else:
            paddle1_pos[1]+= paddle_speed
    if keys[pygame.K_UP]:
        if paddle2_pos[1]<=0:
            pass
        else:
            paddle2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN]:
        if paddle2_pos[1]>=688:
            pass
        else:
            paddle2_pos[1] += paddle_speed
        
    clock.tick(60)
    # Move the ball
    ball_pos[0] += ball_speed_x
    ball_pos[1] += ball_speed_y

     # Check for collision with the paddles
    if (ball_pos[0] <= paddle1_pos[0] + paddle_width and
            ball_pos[1] >= paddle1_pos[1] and
            ball_pos[1] <= paddle1_pos[1] + paddle_height):
        ball_speed_x = -ball_speed_x
    if (ball_pos[0] >= paddle2_pos[0] - ball_radius and
            ball_pos[1] >= paddle2_pos[1] and
            ball_pos[1] <= paddle2_pos[1] + paddle_height):
        ball_speed_x = -ball_speed_x
    # Check for collision with the edges of the screen
    if ball_pos[1] <= 0 + ball_radius or ball_pos[1] >= 788 - ball_radius:
        ball_speed_y = -ball_speed_y
    # Handle scoring
    if ball_pos[0] <= 0:
        player2_score += 1
        ball_pos = [470, 394]
        ball_speed_x = 3
        ball_speed_y = 3
    elif ball_pos[0] >= 940:
        player1_score += 1
        ball_pos = [470, 394]
        ball_speed_x = -3
        ball_speed_y = -3
    # Clear the screen
    screen.fill((0, 0, 0))

    screen.blit(background_surface, (0,0))
    # Draw the paddles
    pygame.draw.rect(screen, (255, 255, 255), (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    # Display the score
    score1_text = font.render(str(player1_score), True, (255, 255, 255))
    score2_text = font.render(str(player2_score), True, (255, 255, 255))
    screen.blit(score1_text, (375, 50))
    screen.blit(score2_text, (525, 50))
    # Update the screen
    pygame.display.flip()
# Exit the game
pygame.quit()
sys.exit()

'''pg.init()
screen = pg.display.set_mode((940,788))
clock=pg.time.Clock()
pg.display.set_caption('Pong Arcade')

paddle1_x=10
paddle1_y=394
paddle2_x=920
paddle2_y=394

paddle_width=25
paddle_height=175

ball_pos=[470,394]
ball_radius=25

player_surface=pg.image.load()

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit() #for exiting game
            exit() #for exiting loop similar to 
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            paddle1_y -= 10
        if keys[pg.K_s]:
            paddle1_y += 10
        if keys[pg.K_UP]:
            paddle2_y -= 5
        if keys[pg.K_DOWN]:
            paddle2_y += 5

    pg.display.flip()
    # Draw the ball
    pg.draw.rect(screen, (255,0,0),(paddle1_x,paddle1_y,paddle_width,paddle_height))
    pg.draw.rect(screen, (0,0,255),(paddle2_x,paddle2_y,paddle_width,paddle_height))
    pg.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    
    pg.display.update()
    
  

    clock.tick(60)
    pg.display.update()
'''


