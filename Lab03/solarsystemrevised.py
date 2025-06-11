import pygame
import sys
import math

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_COLOR = (255, 204, 0)
PLANET_COLOR = (0, 153, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Midpoint Circle Algorithm (used for orbits)
def midpoint_circle(x_center, y_center, radius):
    x = radius
    y = 0
    d = 1 - radius

    while x >= y:
        for dx, dy in [
            (x, y), (-x, y), (x, -y), (-x, -y),
            (y, x), (-y, x), (y, -x), (-y, -x)
        ]:
            screen.set_at((x_center + dx, y_center + dy), WHITE)

        y += 1
        if d <= 0:
            d += 2 * y + 1
        else:
            x -= 1
            d += 2 * (y - x) + 1

# Planet data structure
class Planet:
    def __init__(self, orbit_radius, radius, speed, color):
        self.orbit_radius = orbit_radius
        self.radius = radius
        self.speed = speed
        self.color = color

    def position(self, time_ms):
        angle = (time_ms / 1000) * self.speed
        x = WIDTH // 2 + self.orbit_radius * math.cos(angle)
        y = HEIGHT // 2 + self.orbit_radius * math.sin(angle)
        return int(x), int(y)

# List of planets
planets = [
    Planet(80, 6, 0.8, (200, 100, 255)),
    Planet(120, 7, 0.6, (100, 255, 200)),
    Planet(160, 8, 0.4, (255, 150, 100)),
    Planet(200, 5, 0.3, (255, 255, 100)),
    Planet(240, 15, 0.2, (100, 150, 255)),
    Planet(280, 13, 0.1, (255, 100, 150)),
    Planet(320, 11, 0.05, (150, 255, 100)),
    Planet(360, 12, 0.02, (255, 100, 100))
]



# Main loop
def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Draw orbits
        for planet in planets:
            midpoint_circle(WIDTH // 2, HEIGHT // 2, planet.orbit_radius)

        # Draw sun
        pygame.draw.circle(screen, SUN_COLOR, (WIDTH // 2, HEIGHT // 2), 30)

        # Draw planets
        time_now = pygame.time.get_ticks()
        for planet in planets:
            x, y = planet.position(time_now)
            pygame.draw.circle(screen, planet.color, (x, y), planet.radius)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
