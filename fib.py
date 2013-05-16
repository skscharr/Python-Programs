# fib.py

# finds the equivalent number in the fibonacci sequence corresponding
# to the number specifed by the user input
# i.e. if 5 is entered the program will look at the fib sequence
# 0, 1, 1, 2, 3, 5, 8, etc. and return 5 (the sequence starts at position 0)

def fib(n):
    combinations = 0
    if 0 <= n < 2:
        position = n
        return position
    if n == 2:
        position = 1
        return position
    else:
        return fib(n-1) + fib(n-2)
  

def main():
    print "Fibonacci Sequence Finder"
    n = int(raw_input("Please enter a positive number to find it's place in the Fibonacci sequence: "))
    print fib(n)    
        
    
main()
