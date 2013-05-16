# StringRot.py

''' This function takes a string, reverses every other word,
and uses rot-13 encryption to return an encrypted sentence.'''

def rotate(s):
    split = s.split(' ')
    count = 0
    new = []
    for word in split:
        if count%2 == 0:
            new.append(word[::-1].encode('rot13'))
        else:
            new.append(word.encode('rot13'))
        count += 1
    return ' '.join(new)

def main():
    print '''Welcome to the encrypter! Please enter a string you would like
encrypted. To quit the program please enter 'exit'.'''
    
    x = True

    while x == True:
        s = raw_input("Please enter a word or sentence you would like encrypted:\n")
        if s != 'exit':
            print rotate(s)
        else:
            x = False
    print "\nGoodbye!"
        
main()
