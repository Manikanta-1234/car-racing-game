import pygame
import random

# Initialize Pygame
pygame.init()

# Screen Dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load Images
road = pygame.image.load("road.png")  # Background road image
player_car = pygame.image.load("car.png")  # Player's car
enemy_car = pygame.image.load("enemy_car.png")  # Enemy car

# Resize Images
road = pygame.transform.scale(road, (WIDTH, HEIGHT))
player_car = pygame.transform.scale(player_car, (50, 100))
enemy_car = pygame.transform.scale(enemy_car, (50, 100))

# Car Positions
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
enemy_x = random.randint(200, WIDTH - 100)
enemy_y = -100  # Start above screen

# Speed & Movement
player_speed = 5
enemy_speed = 5

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.blit(road, (0, 0))  # Draw Road
    screen.blit(player_car, (player_x, player_y))  # Draw Player Car
    screen.blit(enemy_car, (enemy_x, enemy_y))  # Draw Enemy Car

    enemy_y += enemy_speed  # Move Enemy Car Down

    # Reset Enemy Car if it goes off-screen
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(200, WIDTH - 100)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 200:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 100:
        player_x += player_speed

    pygame.display.update()
    clock.tick(30)

pygame.quit()
