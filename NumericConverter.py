# NumericConverter.py

'''This function converts a (non-negative) integer into its
spoken-language form, e.g.: 

3 => "three"
12 => "twelve"
355 => "three hundred fifty five"

This function works for numbers 0-999.'''

def converter(n):
    digits = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six',
               'seven', 'eight', 'nine']
    tens = ['and', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty',
            'seventy', 'eighty', 'ninety']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
             'seventeen', 'eighteen', 'nineteen']
    h = 'hundred'

    if 0 <= n < 10:
        return digits[n]
    
    elif 10 <= n <= 99:
        if n%10 == 0:
            x = (n/10)-1    # only if single digit
            return tens[x]
        elif 10 < n < 20:
            return teens[n-11]  # only if in the teens
        else:
            q = (n/10)    # tens position
            r = n%10    # digit position
            return tens[q] + " " + digits[r] 

    else:
        if n%100 == 0:
            x = n/100   # hundreds position
            return digits[x] + " " + h
        else:
            q = n/100   # hundreds position
            r = n%100   # tens position
            if r%10 == 0:
                x = (r/10)    #tens position
                return digits[q] + " " + h + " " + tens[x]
            else:
                y = (r/10)    # tens position
                z = r%10    # digit position
                return digits[q] + " " + h + " " + tens[y] + " " + digits[z]

def main():
    print '''Welcome to the number converter! Enter any positive integer
between 0 and 999, and I will convert it to it's English
spoken language form. \nPlease enter -1 when you wish to stop.'''
    
    x = True
    while x == True:
        n = int(raw_input(">> "))
        if n >= 0:
            print converter(n)
        else:
            x = False
            
    print "\nGoodbye!"

main()
