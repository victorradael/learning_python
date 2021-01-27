def display_board(board):

  print('      |   |   ')
  print('    '+board[7]+' | '+board[8]+' | ' +board[9])
  print('-----------------')
  print('      |   |   ')
  print('    '+board[4]+' | '+board[5]+' | ' +board[6])
  print('-----------------')
  print('      |   |   ')
  print('    '+board[1]+' | '+board[2]+' | ' +board[3])

# display_board([" "," "," "," "," ","X"," "," "," ", " "])

def player_input():
  market = '
  while not (market == 'X' or market =="O"):
    market = input('Player 1: Você quer ser X ou O?').upper()

  if marker == 'X':
    return ('X', "O")
  else:
    return ('O', 'X')

def place_marker(board, marker, position):
  board[position] = marker

def win_check(board, mark):
  return (
    (board[9] == mark and board[8] == mark and board[7] == mark)
    (board[6] == mark and board[5] == mark and board[4] == mark)
    (board[3] == mark and board[2] == mark and board[1] == mark)
    (board[7] == mark and board[5] == mark and board[3] == mark)
    (board[9] == mark and board[5] == mark and board[1] == mark)
    (board[7] == mark and board[4] == mark and board[1] == mark)
    (board[8] == mark and board[5] == mark and board[2] == mark)
    (board[9] == mark and board[6] == mark and board[3] == mark)
  )

import random
def choose_first():
  if random.randint(0, 1) == 0:
      return 'Player 2'
  else:
      return 'Player 1'
  pass