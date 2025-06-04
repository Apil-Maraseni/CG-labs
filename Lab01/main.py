import pygame
import sys



def ddaLine(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    
    if(dx>dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    xinc = dx / steps
    yinc = dy / steps
    
    x = x1
    y = y1
    
    for i in range(int(steps) + 1):
        screen.set_at((round(x), round(y)), WHITE)#plot(int(x), int(y))
        x = x + xinc
        y = y + yinc



pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("DDA Line Drawing Algorithm")

WHITE = (12, 15, 255)
BLACK = (255, 255, 255)


def main():
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        ddaLine(25, 125, 700, 500)
        pygame.display.flip()
        pygame.time.delay(100)

if __name__ == "__main__":
    main()




