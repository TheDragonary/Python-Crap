import pygame
import random

# Set up game window
WIDTH = 800
HEIGHT = 600
FPS = 60

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame library
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Set up game variables
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 3 * random.choice([-1, 1])
ball_speed_y = 3 * random.choice([-1, 1])
player1_score = 0
player2_score = 0
font_name = pygame.font.match_font('arial')

# Set up game objects
player1 = pygame.Rect(50, HEIGHT // 2 - 50, 20, 100)
player2 = pygame.Rect(WIDTH - 70, HEIGHT // 2 - 50, 20, 100)
ball = pygame.Rect(ball_x, ball_y, 20, 20)

# Set up game functions
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_screen():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    draw_text(screen, str(player1_score), 40, WIDTH // 4, 30)
    draw_text(screen, str(player2_score), 40, WIDTH * 3 // 4, 30)

    # Draw center line
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

def move_ball():
    global ball_speed_x, ball_speed_y, player1_score, player2_score

    # Move ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        player2_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        player1_score += 1
        reset_ball()
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= HEIGHT:
        player1.bottom = HEIGHT
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= HEIGHT:
        player2.bottom = HEIGHT

    # Check for collision with players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

def reset_ball():
    global ball_speed_x, ball_speed_y, ball_x, ball_y

    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_speed_x *= random.choice([-1, 1])
    ball_speed_y *= random.choice([-1, 1])

    ball.center = (ball_x, ball_y)

# Run game loop
running = True
while running:
    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= 5
    if keys[pygame.K_s]:
        player1.y += 5
    if keys[pygame.K_UP]:
      player2.y -= 5
    if keys[pygame.K_DOWN]:
      player2.y += 5

    # Move ball
    move_ball()

    # Draw screen
    draw_screen()

    # Update screen
    pygame.display.flip()

    # Wait for next frame
    clock.tick(FPS)

