# LoanPaymentCalc.py

''' This program calculates the interest due on a 
loan and prints a payment schedule.'''

# Interest = Principal X Rate X Term 

def interestCalc(P, R, T):
  I = P*R*T
  return I

def payments(I):
  pass 
    
def main():
  print "Loan Calculator\n"

  P = float(raw_input("Amount Borrowed: "))
  R = float(raw_input("Interest Rate: "))
  T = float(raw_input("Term (years): "))

  print "\nAmount borrowed: $" + str(P)
  print "Total interest paid: $" + str(R) + "\n"

  print interestCalc(P, R, T)

main()