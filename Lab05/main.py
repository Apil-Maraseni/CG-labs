import pygame
import sys
import math

def translate(x, y, tx, ty):
    return x + tx, y + ty

def rotate(x, y, angle, cx=0, cy=0):
    radians = math.radians(angle)
    x -= cx
    y -= cy
    x_new = x * math.cos(radians) - y * math.sin(radians)
    y_new = x * math.sin(radians) + y * math.cos(radians)
    return x_new + cx, y_new + cy

def scale(x, y, sx, sy):
    return x * sx, y * sy

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformations: Translation, Rotation, Scaling")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    screen.fill(BLACK)

    x1, y1 = 100, 100
    x2, y2 = 200, 200

    # Original line
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)

    # Translated line
    tx1, ty1 = translate(x1, y1, 150, 0)
    tx2, ty2 = translate(x2, y2, 150, 0)
    pygame.draw.line(screen, (255, 0, 0), (tx1, ty1), (tx2, ty2), 2)

    # Rotated line (around center of screen)
    cx, cy = WIDTH // 2, HEIGHT // 2
    rx1, ry1 = rotate(x1, y1, 45, cx, cy)
    rx2, ry2 = rotate(x2, y2, 45, cx, cy)
    pygame.draw.line(screen, (0, 255, 0), (rx1, ry1), (rx2, ry2), 2)

    # Scaled line
    sx1, sy1 = scale(x1, y1, 1.5, 1.5)
    sx2, sy2 = scale(x2, y2, 1.5, 1.5)
    pygame.draw.line(screen, (0, 0, 255), (sx1, sy1), (sx2, sy2), 2)

    pygame.display.flip()

if __name__ == "__main__":
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        main()
        # clock.tick(1)  # Refresh the screen once per second
