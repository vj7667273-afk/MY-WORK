import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Geometry Dash Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (100, 150, 255)
BROWN = (160, 82, 45)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player variables
player_size = 50
player_x = 100
player_y = HEIGHT - player_size - 50
player_velocity_y = 0
GRAVITY = 1
JUMP_STRENGTH = -18
jumping = False
angle = 0

# Ground
GROUND_HEIGHT = 50

# Obstacles
spike_size = 50
obstacle_speed = 8
obstacle_list = []  # list of dicts: {'type','x','y','w','h','scored'}

# Background scroll
bg_scroll = 0
bg_speed = 2

# Score
score = 0
high_score = 0

font = pygame.font.SysFont("Arial", 40)
big_font = pygame.font.SysFont("Arial", 70)

# Load music
try:
    pygame.mixer.music.load("soundtrack.mp3")
    pygame.mixer.music.play(-1)
except Exception:
    print("⚠️ No soundtrack file found. Place 'soundtrack.mp3' in the same folder.")

def draw_background():
    global bg_scroll
    screen.fill(BLUE)
    bg_scroll -= bg_speed
    if bg_scroll <= -WIDTH:
        bg_scroll = 0
    for i in range(2):
        offset = i * WIDTH + bg_scroll
        pygame.draw.rect(screen, (180, 220, 255), (offset, HEIGHT - 200, WIDTH, 150))
        pygame.draw.rect(screen, (150, 200, 240), (offset + 100, HEIGHT - 150, WIDTH, 150))
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

def draw_player():
    global angle
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    square = pygame.Surface((player_size, player_size), pygame.SRCALPHA)
    square.fill(GREEN)
    rotated = pygame.transform.rotate(square, angle)
    rect = rotated.get_rect(center=player_rect.center)
    screen.blit(rotated, rect.topleft)

def draw_obstacles():
    for obs in obstacle_list:
        otype = obs['type']
        x = obs['x']
        y = obs['y']
        w = obs['w']
        h = obs['h']
        if otype == "spike":
            points = [(x, y + h), (x + w // 2, y), (x + w, y + h)]
            pygame.draw.polygon(screen, RED, points)
        elif otype == "double_spike":
            # left spike
            points1 = [(x, y + h), (x + w // 2, y), (x + w, y + h)]
            # right spike (adjacent)
            points2 = [(x + w, y + h), (x + 3 * w // 2, y), (x + 2 * w, y + h)]
            pygame.draw.polygon(screen, RED, points1)
            pygame.draw.polygon(screen, RED, points2)
        elif otype == "block":
            pygame.draw.rect(screen, BROWN, (x, y, w, h))

def move_obstacles():
    global obstacle_list
    for obs in obstacle_list:
        obs['x'] -= obstacle_speed
    # remove once completely off screen (give margin)
    obstacle_list = [obs for obs in obstacle_list if obs['x'] > -300]

def generate_obstacles():
    # spawn if list empty or last obstacle passed a gap threshold
    if len(obstacle_list) == 0 or obstacle_list[-1]['x'] < WIDTH - 300:
        otype = random.choice(["spike", "double_spike", "block"])
        if otype == "spike":
            obstacle_list.append({
                'type': "spike",
                'x': WIDTH,
                'y': HEIGHT - GROUND_HEIGHT - spike_size,
                'w': spike_size,
                'h': spike_size,
                'scored': False
            })
        elif otype == "double_spike":
            obstacle_list.append({
                'type': "double_spike",
                'x': WIDTH,
                'y': HEIGHT - GROUND_HEIGHT - spike_size,
                'w': spike_size,
                'h': spike_size,
                'scored': False
            })
        elif otype == "block":
            height = random.choice([100, 150])
            obstacle_list.append({
                'type': "block",
                'x': WIDTH,
                'y': HEIGHT - GROUND_HEIGHT - height,
                'w': spike_size,
                'h': height,
                'scored': False
            })

def check_collisions():
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for obs in obstacle_list:
        otype = obs['type']
        x = obs['x']
        y = obs['y']
        w = obs['w']
        h = obs['h']
        if otype == "double_spike":
            spike_rect = pygame.Rect(x, y, w * 2, h)
            if player_rect.colliderect(spike_rect):
                return True
        elif otype == "spike":
            spike_rect = pygame.Rect(x, y, w, h)
            if player_rect.colliderect(spike_rect):
                return True
        elif otype == "block":
            block_rect = pygame.Rect(x, y, w, h)
            if player_rect.colliderect(block_rect):
                return True
    return False

def draw_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    high_text = font.render(f"High: {high_score}", True, BLACK)
    screen.blit(score_text, (20, 20))
    screen.blit(high_text, (20, 60))

def game_over():
    global high_score
    if score > high_score:
        high_score = score
    text = font.render("Game Over! Press R to Restart", True, BLACK)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
    pygame.display.update()
    pygame.mixer.music.stop()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False
                try:
                    pygame.mixer.music.play(-1)
                except Exception:
                    pass
    # when this function returns, the game_loop will end and main loop will restart it

def start_menu():
    global bg_scroll
    waiting = True
    while waiting:
        draw_background()
        title = big_font.render("Geometry Dash Clone", True, BLACK)
        press = font.render("Press SPACE to Start", True, BLACK)
        high_text = font.render(f"High Score: {high_score}", True, BLACK)

        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 100))
        screen.blit(press, (WIDTH//2 - press.get_width()//2, HEIGHT//2))
        screen.blit(high_text, (WIDTH//2 - high_text.get_width()//2, HEIGHT//2 + 80))

        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def pause_menu():
    """Pause screen until P is pressed again"""
    paused = True
    pygame.mixer.music.pause()
    while paused:
        draw_background()
        pause_text = big_font.render("Paused", True, BLACK)
        resume_text = font.render("Press P to Resume", True, BLACK)
        screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2 - 50))
        screen.blit(resume_text, (WIDTH//2 - resume_text.get_width()//2, HEIGHT//2 + 20))
        pygame.display.update()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = False
    pygame.mixer.music.unpause()

def game_loop():
    global player_y, player_velocity_y, jumping, angle, obstacle_list, bg_scroll, score, obstacle_speed
    obstacle_list = []
    player_y = HEIGHT - player_size - GROUND_HEIGHT
    player_velocity_y = 0
    jumping = False
    angle = 0
    bg_scroll = 0
    score = 0
    obstacle_speed = 8

    running = True
    while running:
        draw_background()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pause_menu()

        # Improved jump (buffered hold)
        if keys[pygame.K_SPACE] and not jumping:
            player_velocity_y = JUMP_STRENGTH
            jumping = True

        # Physics
        player_velocity_y += GRAVITY
        player_y += player_velocity_y

        if player_y >= HEIGHT - player_size - GROUND_HEIGHT:
            player_y = HEIGHT - player_size - GROUND_HEIGHT
            player_velocity_y = 0
            jumping = False

        if jumping:
            angle -= 10
        else:
            angle = 0

        # Obstacles
        generate_obstacles()
        move_obstacles()
        draw_obstacles()

        # Update score when player passes obstacles (use scored flag)
        for obs in obstacle_list:
            obs_right = obs['x'] + (obs['w'] * (2 if obs['type'] == 'double_spike' else 1))
            if (obs_right < player_x) and (not obs['scored']):
                score += 1
                obs['scored'] = True

        # Increase difficulty with score
        obstacle_speed = 8 + score // 5

        # Draw player and UI
        draw_player()
        draw_score()

        # Collision
        if check_collisions():
            game_over()
            # end this game loop and return to main loop to show start menu again
            return

        pygame.display.update()
        clock.tick(FPS)

# Run game: main loop handles start menu and game loop; no recursion
while True:
    start_menu()
    game_loop()
