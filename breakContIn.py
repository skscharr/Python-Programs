# breakContIn.py

# program for exercises on
# break, continue and in

 
def exercise1( L ):
 
    print "exercise 1" 
    for x in L:
        if x > 50:
            print(x)
            break
 
def exercise2():

    L = [ ]
    print "exercise 2" 
    print "Please enter positive integers. You may enter up to 100 numbers. \nEnter -1 when you are done."
    for x in range( 100 ):
        answer = eval(raw_input( "> " ))
        if answer == -1:
            break
        L.append( answer )

    print( L )
    
    
 
def exercise3( L ):
 
    print "exercise 3" 
    L2 = [ ]
    for x in L:
        if x % 2 == 0:
            L2.append( x )
    L = L2
    print "L=", L 
 
def exercise4( seven ):
 
    print "exercise 4" 
    print "You will have 10 tries to quess the name of one of Snow White's 7 dwarves."
    for i in range(10):
        name = raw_input( "> " )
        if name in seven:
            print "Congratulations! You guessed right!"
            break
        elif name not in seven:
            print "Sorry, try again!" 

 
def main():
    L = [ 1, 10, 20, 5, 100, 110, 21, 500 ]
    seven = [ "Sleepy", "Sneezy", "Bashful", "Happy", "Grumpy", "Dopey", "Doc" ]
 
    exercise1( L )
 
    exercise2()
 
    exercise3( L )
 
    exercise4( seven )
 
main()
