# boundingball1.py

'''The ball bounces around the screen and changes color
when it passes through the middle of the window'''

from graphics import *
import time
 
def main():
    w = 500
    h = 500
    radius = 20
    win = GraphWin( "lab 7", w, h )
 
    c = Circle( Point( w/2, h/2 ), radius )
    c.setFill( "magenta" )
    c.draw( win )
 
    dirX = 5  # speed in the horizontal direction
    dirY = 1
    for step in range( 1000 ):
        c.move( dirX, dirY )        
        # uncomment next line if ball moves too fast
        # time.sleep( 0.05 )  # 5/100th sec.
        if   c.getCenter().getX()-20 < 0 or c.getCenter().getX()+20 > w :
            dirX = -dirX
        if   c.getCenter().getY()-20 < 0 or c.getCenter().getY()+20 > h :
            dirY = -dirY
        if   c.getCenter().getX() <= w/2 :
            c.setFill( "yellow" )
        else:
            c.setFill( "red" )

            
    Text( Point( w//2, h//2 ), "Click me to quit!" ).draw( win )
    win.getMouse()
    win.close()
 
main()
