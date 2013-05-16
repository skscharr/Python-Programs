# NumberCounting.py

'''This function takes a number N and counts how many numbers
between 1 and N (inclusive) do not contain any digits which
are '7'.

Note: This is most certainly not the most concise method
to solve this problem. It also only works from 1 to 999'''

def counting(N):
    count = 0
    for x in range(1, N+1):
        if x != 7 and len(str(x)) == 1:
            count += 1
        elif len(str(x)) == 2:
            if str(x)[0] != '7' and str(x)[1] != '7':
                count += 1
            else:
                continue
        elif len(str(x)) == 3:
            if str(x)[0] != '7' and str(x)[1] != '7' and str(x)[2] != '7':
                count += 1
            else:
                continue
        else:
            continue
            
    return count


def main():
    print '''No 7s!!!
Please enter a positive integer between 0 and 999 and
I will return the numberof numbers from 0 to your integer.
Enter -1 to exit.
i.e. If you enter 7 the program will return 6.'''
    x = True
    while x == True:
        n = int(raw_input(">> "))
        if n != -1:
            print "N = " + str(n) + ": " + str(counting(n))
        else:
            x = False

    print "\nGoodbye!"

main()
