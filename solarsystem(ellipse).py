#to draw the solar system with midpoint ellipse algorithm
#Midpoint Ellipse Algorithm in Python using Pygame
import math
import pygame
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Midpoint Ellipse Algorithm Apil Maraseni 012")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

def MidpointEllipse(rx, ry, xc, yc, color=WHITE):
    x = 0
    y = ry
    p1 = ry**2 - rx**2*ry + 0.25*rx**2
    dx = 2*ry**2*x
    dy = 2*rx**2*y

    while dx < dy:
        screen.set_at((int(xc + x), int(yc + y)), color)
        screen.set_at((int(xc - x), int(yc + y)), color)
        screen.set_at((int(xc + x), int(yc - y)), color)
        screen.set_at((int(xc - x), int(yc - y)), color)
        if p1 < 0:
            x += 1
            p1 += dx + ry**2
            dx = 2*ry**2*x
            dy = 2*rx**2*y
        else:
            x = x + 1
            y = y - 1
            p1 += 2*ry**2*x - 2*rx**2*y + ry**2
            dx = 2*ry**2*x
            dy = 2*rx**2*y

    p2 = ry**2*(x + 0.5)**2 + rx**2*(y - 1)**2 - rx**2*ry**2
    while y >= 0:
        screen.set_at((int(xc + x), int(yc + y)), color)
        screen.set_at((int(xc - x), int(yc + y)), color)
        screen.set_at((int(xc + x), int(yc - y)), color)
        screen.set_at((int(xc - x), int(yc - y)), color)
        if p2 > 0:
            x = x
            y = y - 1
            p2 += -2*rx**2*y + rx**2
            dx = 2*ry**2*x
            dy = 2*rx**2*y
        else:
            x = x + 1
            y = y - 1
            p2 += rx**2 - 2*rx**2*y + 2*ry**2*x
            dx = 2*ry**2*x
def draw_solar_system(rx, ry, xc, yc, angle=0):
    screen.fill(BLACK)
    # Draw the sun
    MidpointEllipse(50, 50, WIDTH // 2, HEIGHT // 2)
    # Draw planets
    for i in range(1, 6):
        radius = 20 * i
        angle_offset = (2 * math.pi / 5) * i  # Distribute planets evenly
        x = int(WIDTH // 2 + radius * math.cos(pygame.time.get_ticks() / 1000))
        y = int(HEIGHT // 2 + radius * math.sin(pygame.time.get_ticks() / 1000))
        MidpointEllipse(10, 10, x, y, color=WHITE)
        MidpointEllipse(10, 10, int(x), int(y))
        MidpointEllipse(10, 10, int(x), int(y), color=WHITE)



def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_solar_system(200, 100, 400, 300)
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()




