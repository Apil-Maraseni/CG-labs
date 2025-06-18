#implementation of Bresenham's  line algorithm to draw a football field using pygame
import pygame
import sys 
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bresenham's Line Algorithm - Apil Maraseni 012")
WHITE=(255,255,255)
GREEN=(70,255,70)
def draw_line(x1, y1, x2, y2):
    #x1= int(input("Enter x1: "))
    # y1= int(input("Enter y1: "))
    # x2= int(input("Enter x2: "))
    # y2= int(input("Enter y2: "))
    # if x1<0 or x1>WIDTH or y1<0 or y1>HEIGHT or x2<0 or x2>WIDTH or y2<0 or y2>HEIGHT:
    #     print("Coordinates out of bounds. Please enter values between 0 and", WIDTH, "for x and 0 and", HEIGHT, "for y.")
    #     return
    
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

       screen.fill(GREEN)
       # Draw the football field
       draw_line(100, 100, 700, 100)
       draw_line(100, 500, 700, 500)
       draw_line(100, 100, 100, 500)
       draw_line(700, 100, 700, 500)
       #draw the center line
       draw_line(400, 100, 400, 500)
       #draw the center circle
       pygame.draw.circle(screen, WHITE, (400, 300), 100, 1)
       #draw the center spot
       pygame.draw.circle(screen, WHITE, (400, 300), 5)
       #draw the penalty area
       draw_line(100, 200, 200, 200)  
       draw_line(100, 400, 200, 400)
       draw_line(200, 200, 200, 400)
       draw_line(700, 200, 600, 200)
       draw_line(700, 400, 600, 400)
       draw_line(600, 200, 600, 400)
       #draw a player
       draw_line(350, 300, 370, 300)    
       draw_line(360, 290, 360, 310)
       draw_line(350, 300, 360, 290)

       draw_line(350, 300, 360, 310)
       draw_line(370, 300, 360, 290)
       draw_line(370, 300, 360, 310)



       

       
       pygame.display.flip()

if __name__=="__main__":
    main()