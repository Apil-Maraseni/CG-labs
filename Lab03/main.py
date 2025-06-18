#Midpoint Circle Algorithm in Python using Pygame
import pygame
import sys

def midpointcircle(x1,y1,x2,y2,r,d):
    x = r
    y = 0
    d = 1 - r

    while x >= y:
        screen.set_at((x1 + x, y1 + y), WHITE)
        screen.set_at((x1 - x, y1 + y), WHITE)
        screen.set_at((x1 + x, y1 - y), WHITE)
        screen.set_at((x1 - x, y1 - y), WHITE)
        screen.set_at((x1 + y, y1 + x), WHITE)
        screen.set_at((x1 - y, y1 + x), WHITE)
        screen.set_at((x1 + y, y1 - x), WHITE)
        screen.set_at((x1 - y, y1 - x), WHITE)
        y += 1
        if d <= 0:
            d = d + 2 * y + 1
        else:
            x -= 1
            d = d + 2 * y - 2 * x + 1

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Algorithm Apil Maraseni 012")

WHITE = (12, 15, 255)
BLACK = (255, 255, 255)


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        midpointcircle(400, 300, 0, 0, 100, 0)
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()




