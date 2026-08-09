""" Tic-Tac-Toe

Scenario

Your task is to write a simple program that simulates playing tic-tac-toe with the user. To make it easier, we've decided to simplify the game. Here are our rules:

the machine (i.e., the program) will play using 'X's;
the user (i.e., you) will play using 'O's;
the first move belongs to the machine — it always places an 'X' in the center of the board;
all squares are numbered starting from 1 (see the example for reference);
the user enters their move by typing in the number of the chosen square — the number must be valid, i.e., an integer greater than 0 and less than 10, and it can't be a square that's already occupied;
the program checks if the game has ended — there are four possible outcomes: the game continues, the game ends in a tie, you win, or the machine wins;
the machine responds with its move, and the game state is checked again;
no artificial intelligence needs to be implemented — the machine will choose a square randomly; that's enough for this game. """

import random

def machine_pick(): # Machine movement for the game
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    return x, y

def victory_check(victory): # Victory condition to end the game
    """ THIS MAY NOT BE THE LEAST COMPLEXITY APPROACH, but it does works pretty good """

    for i in range(3): # Victory condition for the horizontal lines
        for j in range(1):
            if victory[i][j] == victory[i][j+1] == victory[i][j+2] == 'X':
                print('The machine won (horizontal) this time mate :)')
                return False
            elif victory[i][j] == victory[i][j+1] == victory[i][j+2] == 'O':
                print('You\'re pretty good at this aren\'t you with that horizontal line?')
                return False
            
    for i in range (3): # Victory condition for the vertical lines
        for j in range(1):
            if victory[j][i] == victory[j+1][i] == victory[j+2][i] == 'X':
                print('The Machine won (vertical) this time mate :)')
                return False
            elif victory[j][i] == victory[j+1][i] == victory[j+2][i] == 'O':
                print('You\'re pretty good at this aren\'t you with that vertical line?')
                return False

    j = i = 0

    if victory[j][i] == victory[j+1][i+1] == victory[j+2][i+2] == 'X': # Left diagonal condition
        print('The machine won (L. diagonal) this time mate :)')
        return False
    elif victory[j][i] == victory[j+1][i+1] == victory[j+2][i+2] == 'O':
        print('You\'re pretty good at this aren\'t you with that L. diagonal line?')
        return False
    elif victory[j+2][i] == victory[j+1][i+1] == victory[j][i+2] == 'X': # Right diagonal condition
        print('The machine won (R. Diagonal) this time mate :)')
        return False
    elif victory[j+2][i] == victory[j+1][i+1] == victory[j][i+2] == 'O':
        print('You\'re pretty good at this aren\'t you with that R. Diagonal line?')
        return False
    else:
        return True           


    
print('Welcome to the Tic Tac Toe')

tic_tac = []
var = 1

for i in range(3): # Creation of the 3x3 table
    row = [] # Creation of a new list for new memory value of list
    for j in range(3): # Int value to store
        row.append(var)
        var += 1
    tic_tac.append(row) # Row append
    
play = one = two = True # One or two is to known who started the game
number = 0

for i in range(3): # Game state print
    print('-' * 19, '\n|                 |', '\n|', end='')
    for j in range(3):
        print(f'  {tic_tac[i][j]}  |', end='')
    print()
    print('|                 |')
    print('-' * 19)   


while play: # Start of the game
    try: # Player action, unpredictable pick
        turn = int(input('Select your turn 1 or 2: '))
    except:
        print('I\'m asking for a int as a value.')

    if turn == 1: # Player starts the game
        try: # Player action, unpredictable pick
            number = int(input('What number you want to pick: '))
            for i in range(3):
                for j in range(3):
                    if tic_tac[i][j] == number:
                        tic_tac[i][j] = 'O'                        
            print('\nThe game has started, the Player made his move!')

            for i in range(3): # Game state print
                print('-' * 19, '\n|                 |', '\n|', end='')
                for j in range(3):
                    print(f'  {tic_tac[i][j]}  |', end='')
                print()
                print('|                 |')
                print('-' * 19)
            two = False

        except:
            print('Only integers values.')

    elif turn == 2: # Machine starts the game
        tic_tac[1][1] = 'X'
        print('The game has started, Machine made his move!')

        for i in range(3): # Game state print
            print('-' * 19, '\n|                 |', '\n|', end='')
            for j in range(3):
                print(f'  {tic_tac[i][j]}  |', end='')
            print()
            print('|                 |')
            print('-' * 19)
        one = False
    play = False

victory = True
exist = False

while victory:
    if one: # The machine has to make his play
        while one:
            x, y = machine_pick()
            print('\n Machine Has made his move!')
            if tic_tac[x][y] != 'X' and tic_tac[x][y] != 'O':
                tic_tac[x][y] = 'X'
                one = False # Ends machine turn
                two = True # Starts player turn            
    
        for i in range(3): # Game state print
            print('-' * 19, '\n|                 |', '\n|', end='')
            for j in range(3):
                print(f'  {tic_tac[i][j]}  |', end='')
            print()
            print('|                 |')
            print('-' * 19)

    elif two: # The player has to make his play
        try:            
            number = int(input('Pick your next move player: '))
            for i in range(3):
                for j in range(3):
                    if tic_tac[i][j] == number:
                        tic_tac[i][j] = 'O'
                        one = True # Starts Machine turn
                        two = False # Ends player turn

            for i in range(3): # Game state print
                print('-' * 19, '\n|                 |', '\n|', end='')
                for j in range(3):
                    print(f'  {tic_tac[i][j]}  |', end='')
                print()
                print('|                 |')
                print('-' * 19)            
                
        except:
            print('Hmm... I think we\'ve already have little missunderstanding with the values, aren\'t we?')

    victory = victory_check(tic_tac)

print('\nThanks for Playing, hope you enjoyed the experience!')