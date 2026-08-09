""" Arrays included in other arrays, or matrixes """

board = []
empty = []
 
for i in range(8): # This is the ammount of columns that the matrix is going to have
    row = [empty for i in range(8)] # This instruction initializes a matrix row of 8 spaces
    board.append(row) # This append adds the row as the index [0][row n]




for i in range(8):
    board[1][i] = 'White Pawn'
    board[6][i] = 'Black Pawn'
   
board[0][0] = 'White Knight'
board[0][7] = 'White Knight'
board[7][0] = 'Black Knight'
board[7][7] = 'Black Knight'
board[7][5] = 'Black Bishop'
board[7][2] = 'Black Bishop'
board[0][2] = 'White Bishop'
board[0][5] = 'White Bishop'
board[7][6] = 'Black Horse'
board[7][1] = 'Black Horse'
board[0][1] = 'White Horse'
board[0][6] = 'White Horse'    
board[7][4] = 'Black King'
board[7][3] = 'Black Queen'
board[0][4] = 'White King'
board[0][3] = 'White Queen'
board[0][3][0] = 'White Queen'

for i in range(2):
    for j in range(8):
        print(f'White side, in position {i},{j} piece: {board[i][j]}')

print('-' * 10)
r = 6
for i in range(2):
    
    for j in range(8):
        print(f'Black side, in position {i},{j} piece: {board[r][j]}')
    r += 1

"""  """