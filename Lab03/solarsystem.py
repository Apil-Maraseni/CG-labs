#using midpoint circle algorithm to draw a solar system using pygame

import pygame
import sys      
import math
from pygame.locals import QUIT
from solarsystemrevised import midpoint_circle

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")
# Function to draw a circle using the midpoint circle algorithm
def midpoint_circle(x_center, y_center, radius):
    x = radius
    y = 0
    d = 1 - radius

    while x >= y:
        # Draw the eight symmetric points
        pygame.draw.circle(screen, WHITE, (x_center + x, y_center + y), 1)
        pygame.draw.circle(screen, WHITE, (x_center - x, y_center + y), 1)
        pygame.draw.circle(screen, WHITE, (x_center + x, y_center - y), 1)
        pygame.draw.circle(screen, WHITE, (x_center - x, y_center - y), 1)
        pygame.draw.circle(screen, WHITE, (x_center + y, y_center + x), 1)
        pygame.draw.circle(screen, WHITE, (x_center - y, y_center + x), 1)
        pygame.draw.circle(screen, WHITE, (x_center + y, y_center - x), 1)
        pygame.draw.circle(screen, WHITE, (x_center - y, y_center - x), 1)
        y += 1
        if d <= 0:
            d += 2 * y + 1
        else:
            x -= 1
            d += 2 * (y - x) + 1
        
# Function to draw the solar system
def draw_solar_system():
    screen.fill(BLACK)
    # Draw the sun
    midpoint_circle(WIDTH // 2, HEIGHT // 2, 50)
    # Draw planets
    for i in range(1, 6):
        radius = 20 * i
        x = WIDTH // 2 + radius * math.cos(pygame.time.get_ticks() / 1000)
        y = HEIGHT // 2 + radius * math.sin(pygame.time.get_ticks() / 1000)
        midpoint_circle(x, y, 10)
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        draw_solar_system()
        pygame.display.flip()
        pygame.time.delay(100)
        
if __name__ == "__main__":
    main()