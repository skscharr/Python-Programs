#factorial.py

''' Calculates the factorial of the given number '''

def fact(n):
  if n <= 0:
    return "Error. Invalid Input"
  elif n == 1:
    return n
  else:
    return n * fact(n-1)

def main():
  print '''Factorial Calculator
  Please enter a number and I will calculate the factorial
  of that number.'''
  n = int(raw_input(">> "))
  print str(n) + "! = " + str(fact(n))

main()
