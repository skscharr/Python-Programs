# evenFunc.py

# This program will tell the user if they entered
# an odd or even integer.

def is_even(n):
    if n%2 == 0:
        return "You entered an even number"
    else:
        return "You entered an odd number"

def main():
    print '''Odd or Even
Please enter a positive integer and I will tell you if
it is odd or even. Please enter -1 to exit the program.'''
    
    x = True
    while x == True:
        num = int(raw_input("Enter a number: "))
        if num >= 0:
            print is_even(num)
        else:
            x = False
    print "\nGoodbye!"

main()
