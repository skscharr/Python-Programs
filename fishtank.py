# lab13a.py
# fishy

 
from graphics import *
import random
H = 517   # use the same number as above
W = 700  # use the same number as above

class Fish:
    def __init__( self, fileName, dirX, dirY ):
         self.image = Image( Point( random.randrange(W-200), random.randrange(H-200)), fileName  )
         self.dx   = dirX
         self.dy   = dirY
 
    def draw( self, win ):
         self.image.draw( win )

    def move( self, dx, dy ):
        self.image.move( dx, dy )
 
def waitForClick( win, message ):
    """ waitForClick: stops the GUI and displays a message.  
    Returns when the user clicks the window. The message is erased."""
 
    # wait for user to click mouse to start
    startMsg = Text( Point( win.getWidth()/2, win.getHeight()/2 ), message )
    startMsg.draw( win )    # display message
    win.getMouse()          # wait
    startMsg.undraw()       # erase
 
 
def main():
    global H, W
    win = GraphWin( "111a-an Aquarium", W, H  )
    background = Image( Point( W/2, H/2 ), "tank2.gif" )
    background.draw( win )
    waitForClick( win, "click to start" )
    
    fish = Fish( "fish4.gif", -1, 0 )
    fish1 = Fish( "fish4.gif", -1, 0 )
    fish2 = Fish( "fish4.gif", -1, 0 )
    fish.draw( win )
    fish1.draw( win )
    fish2.draw( win )
    for x in range( 300 ):
        fish.move( -1, random.choice( [ 1, -1, 0, -2, 2, 0, 0, 0, ] ))
        fish1.move( -1, random.choice( [ 1, -1, 0, -2, 2, 0, 0, 0, ] ))
        fish2.move( -1, random.choice( [ 1, -1, 0, -2, 2, 0, 0, 0, ] ))
        
    waitForClick( win, "click to end" )
    win.close()
 
main()
