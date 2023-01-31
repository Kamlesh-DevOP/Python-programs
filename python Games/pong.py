import pygame
import sys
from random import * 
import time

def main():
    a=1
    pygame.init()
    clock=pygame.time.Clock()

    size = (940, 788)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Pong Arcade')

    paddle1_pos = [29, 300]
    paddle2_pos = [891, 300]
    paddle_width = 20
    paddle_height = 100
    paddle_speed = 2

    ball_pos = [470, 394]
    ball_radius = 20
    ball_speed_x = 1
    ball_speed_y = 1

    player1_score = 0
    player2_score = 0

    #initialising picture surfaces
    background_surface=pygame.image.load('D:/Kamlesh/python games/Assets/bg.jpg').convert()
    player_2_surf=pygame.image.load('D:/Kamlesh/python games/Assets/player 2 win.jpg').convert()
    player_1_surf=pygame.image.load('D:/Kamlesh/python games/Assets/player 1 win.jpg').convert()
    font = pygame.font.Font('D:/Kamlesh/python games/Assets/digital-7 (italic).ttf', 90)
    intro_surf=pygame.image.load('D:/Kamlesh/python games/Assets/start screen.jpg').convert()

    running=False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.blit(intro_surf, (0,0))
        
        #adding cursor
        pos=pygame.mouse.get_pos()
        if (pos[0]>306 and pos[0]<639 and pos[1]>364 and pos[1]<462) or (pos[0]>379 and pos[0]<578 and pos[1]>511 and pos[1]<591):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            if pos[0]>306 and pos[0]<639 and pos[1]>364 and pos[1]<462:
                running = True
                break
            if pos[0]>379 and pos[0]<578 and pos[1]>511 and pos[1]<591:
                running=False
                break

        pygame.display.flip()

#waiting time before start
    for i in range(500):
        screen.blit(background_surface, (0,0))
        for j in range(70):
            pygame.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
        for k in range(10):
            pygame.draw.rect(screen, (255, 255, 255), (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))
            pygame.draw.rect(screen, (255, 255, 255), (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
        pygame.display.flip()
        
    while running:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running=False  
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
            ball_pos = [470,randint(200,500)]
            ball_speed_x = 1
            ball_speed_y = 1
        elif ball_pos[0] >= 940:
            player1_score += 1
            ball_pos = [470,randint(200, 500)]
            ball_speed_x = -1
            ball_speed_y = -1

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the paddles

        screen.blit(background_surface, (0,0))
        pygame.draw.rect(screen, (255, 255, 255), (paddle1_pos[0], paddle1_pos[1], paddle_width, paddle_height))
        pygame.draw.rect(screen, (255, 255, 255), (paddle2_pos[0], paddle2_pos[1], paddle_width, paddle_height))

        # Draw the ball

        pygame.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

        # Display the score

        score1_text = font.render(str(player1_score), True, (255, 255, 255))
        score2_text = font.render(str(player2_score), True, (255, 255, 255))
        screen.blit(score1_text, (375, 50))
        screen.blit(score2_text, (525, 50))
        
        if player1_score==10:
            screen.blit(player_1_surf, (0,0))
            pygame.display.flip()
            time.sleep(3)
            sys.exit() 
            pygame.quit()

        if player2_score==10:
            screen.blit(player_2_surf,(0,0))
            pygame.display.flip()         
            time.sleep(3)
            sys.exit()
            pygame.quit()
            
        pygame.display.flip()

    pygame.quit()
    sys.exit()

main()

