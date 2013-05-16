# Created 4/2/13
# @author Samantha Scharr
# project from "Battleship!" by Kate Lockwood
# on Codecademy.com Python course
# http://www.codecademy.com/courses/python-beginner-en-4XuFm


from random import randint

# Create Battleship board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print """Instructions: You have 4 turns to guess where the
battleship is on the board. Rows and columns are numbered
from 0 to 4, NOT 1 to 5. Have Fun!"""
print
print_board(board)

# Create random location of battleship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Begin game, players have 4 guesses
for turn in range(4):
    guess_row = input("Guess Row: ")
    guess_col = input("Guess Col: ")
    
    # If correct guess, congratulate and break from loop to end game
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        # Alert user if guess out of range
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        # Alert user if it is a repeat guess
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        # Alert user if guess is valid but not a hit
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    if turn < 3:
        print "Turn: " + str(turn+1)
        print_board(board)
    else:
        print "Game Over"
