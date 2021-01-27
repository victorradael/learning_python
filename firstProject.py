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
  marker = ' '
  print(marker)
  while not (marker == 'X' or marker =='O'):
    marker = input('Player 1: Voce quer ser X ou O?').upper()

  if marker == 'X':
    return ('X', 'O')
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

def space_check(board, position):

  return board[position] == ' '

def full_board_check(board):
  for i in range(0, 10):
    if space_check(board, i):
      return False
  
  return True

def player_choice(board):
  position = ' '

  while position not in ' 1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
    position = input('Escolha sua jogada (1-9)')
  return int(position)

def replay():

  return input('Quer jogar novamente? "SIM" ou "NAO"').lower().startwith('s')


print('Vamos Jogar Jogo da Velha!')

while True:
  #Definindo ojogo
  board = [' '] * 10
  player1_marker, player2_marker = player_input()
  turn = choose_first()
  print(turn+' comeca!')

  game_on = True
  while game_on:
    #Vez do Player 1
    if turn == 'Player 1':
      display_board(board)
      position = player_choice(board)
      place_marker(board, player1_marker, position)
    
    #Checar vitoria
    if win_check(board, player1_marker):
      display_board(board)
      print('Player 1 Venceu!')
      game_on = False
    else:
      if full_board_check(board):
        display_board(board)
        print('Deu Velha!')
        break
      else:
        turn = 'Player 2'

      #Vez do Player 2
    if turn == 'Player 2':
      display_board(board)
      position = player_choice(board)
      place_marker(board, player1_marker, position)
    
    #Checar vitoria
    if win_check(board, player2_marker):
      display_board(board)
      print('Player 2 Venceu!')
      game_on = False
    else:
      if full_board_check(board):
        display_board(board)
        print('Deu Velha!')
        break
      else:
        turn = 'Player 1'

  if not replay():
    break

  