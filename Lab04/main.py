#Midpoint Ellipse Algorithm in Python using Pygame
import pygame
import sys

def MidpointEllipse(rx,ry,xc,yc):
    x = 0
    y = ry
    p1 = ry**2 -rx**2*ry + 0.25*rx**2
    dx = 2*ry**2*x
    dy = 2*rx**2*y
    
    while dx < dy:
        screen.set_at((xc + x, yc + y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)
        if p1< 0:
            x += 1
            y = y
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
    while y>=0:
        screen.set_at((xc +x, yc + y), WHITE)
        screen.set_at((xc - x, yc + y), WHITE)
        screen.set_at((xc + x, yc - y), WHITE)
        screen.set_at((xc - x, yc - y), WHITE)
        if p2 > 0:
            x = x
            y = y -1
            p2 += -2*rx**2*y + rx**2
            dx = 2*ry**2*x
            dy = 2*rx**2*y
        else:
            x = x + 1
            y= y - 1
            p2 += rx**2 -2*rx**2*y + 2*ry**2*x
            dx = 2*ry**2*x
            dy = 2*rx**2*y
    
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Ellipse Algorithm Apil Maraseni 012")

WHITE = (12, 15, 255)
BLACK = (255, 255, 255)


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        MidpointEllipse(200, 100, 400, 300)
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()




