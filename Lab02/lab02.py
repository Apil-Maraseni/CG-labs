import pygame
import sys 
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bresenham's Line Algorithm - Apil Maraseni 012")
WHITE=(255,255,255)
BLACK=(0,0,0)
def draw_line(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2-y1
    x =x1
    y = y1
    if x2>x1:
        lx = 1
    else:
        lx = -1
    if y2>y1:
        ly = 1
    else:
        ly = -1
    if abs(dx)>abs(dy):
        p = 2*abs(dy)-abs(dx)
        for i in range(abs(dx)+1):
            screen.set_at((x,y),WHITE)
            if p<0:
               x=x+lx
               y=y
               p = p + 2*abs(dy)
            else:
                x=x+lx
                y=y+ly
                p = p + 2*(abs(dy)-abs(dx))
                screen.set_at((x,y),WHITE)
    else:
        p = 2*abs(dx)-abs(dy)
        for i in range(abs(dy)+1):
            screen.set_at((x,y),WHITE)
            if p<0:
                x=x
                y=y+ly
                p = p + 2*abs(dx)
            else:
                x=x+lx
                y=y+ly
                p = p + 2*(abs(dx)-abs(dy))
                screen.set_at((x,y),WHITE)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_line(2,2, 400, 500)
        pygame.display.flip()

if __name__=="__main__":
    main()