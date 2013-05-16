# lab9b.py

from graphics import *
 
 
def isInside( c, r ):
    xc = c.getCenter().getX()
    yc = c.getCenter().getY()
    
    P1 = r.getP1()
    P2 = r.getP2()
    x1 = P1.getX()
    y1 = P1.getY()
    x2 = P2.getX()
    y2 = P2.getY()
    
    if (x1 <= xc <= x2 or x2 <= xc <= x1) \
       and (y1 <= yc <= y2 or y2 <= yc <= y1):
        return 1
    return 0
 
def main():
    w = 600
    h = 400
    x1 = 20
    y1 = 30
    x2 = w // 3
    y2 = h - y1
    x3 = 550
    y3 = 100
    x4 = 400
    y4 = 300
    win = GraphWin( "Click me to stop!", w, h )
 
 
    c = Circle( Point( w//2, h//4 ), 20 )
    c.setFill( "yellow" )
    c.draw( win )
 
    r = Rectangle( Point( x1, y1 ), Point( x2, y2 ) )
    r.setWidth(3)
    r.draw( win )

    r2 = Rectangle( Point( x3, y3), Point( x4, y4 ) )
    r2.setWidth(3)
    r2.draw( win )
 
    dirX = 5
    dirY = 3
 
    while True:
        c.move( dirX, dirY )
        xc = c.getCenter().getX()
        yc = c.getCenter().getY()
        if not ( 0 <= xc <= w ): dirX = -dirX
        if not ( 0 <= yc <= h ): dirY = -dirY
 
        if isInside( c, r )== 1:
            # center inside rectangle
            c.setFill( "red" )
        elif isInside( c, r2 ) == 1:
            c.setFill( "blue" )
        else:
            # center outside rectangle
            c.setFill( "yellow" )
 
        if win.checkMouse() != None:
            break
 
    win.close()
 
main()
