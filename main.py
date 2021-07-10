import random

#Global Variables
tictac_list = [["_","_","_"],["_","_","_"],["_","_","_"]]
row_num = ""
col_num = ""

#Prints the instructions for 1 player mode
def instructions_1():
  print()
  print("1) Your mark will be an X and the Computer's mark will be an O.")
  print("2) When prompted, enter the place where you will like to place your mark.")
  print("3) When either you or the Computer gets 3 marks in a row, the game will end.")

#Prints the instructions for 2 player mode
def instructions_2():
  print()
  print("1) Player 1's mark will be an X and Player 2's mark will be an O.")
  print("2) When prompted, enter the place where you will like to place your mark.")
  print("3) When either you or your opponent gets 3 marks in a row, the game will end.")

#Prints the board
def tictactoe_board():
  global tictac_list
  print()
  print("    1   2   3")
  for row in range(len(tictac_list)):
    print("  -------------")
    print(str(row + 1) + " | ", end = "")
    for col in range(len(tictac_list[row])):
      print(tictac_list[row][col], end = " | ")
    print()
  print("  -------------")

#asks user for their input
def userinput(num):
  global tictac_list
  global row_num
  global col_num
  print()
  row_num = input("Player " + str(num) + ": Which row do you wish to enter your mark? ")
  print()
  col_num = input("Player " + str(num) + ": Which column do you wish to enter your mark? ")
  while col_num not in ("1","2", "3") or row_num not in ("1","2", "3") or tictac_list[int(row_num) - 1][int(col_num) -1] != "_":
    if col_num not in ("1","2", "3") or row_num not in ("1","2", "3"):
      print()
      print("Your response is incorrect. Please enter an integer from 1-3.")
      print()
    elif tictac_list[int(row_num) - 1][int(col_num) - 1] != "_":
      x = "(" + row_num + "," + col_num + ")"
      print()
      print(x + " has already been taken. Please try again.")
      print()
    row_num = input("Player " + str(num) + ": Which row do you wish to enter your mark? ")
    print()
    col_num = input("Player " + str(num) + ": Which column do you wish to enter your mark? ")

#checks if there are 3 characters in a row
def being_in_a_row(mark):
  global tictac_list
  repetition = 0
  while repetition < 3:
    if mark in tictac_list[repetition][0] + tictac_list[repetition][1] + tictac_list[repetition][2]:
      return True
    repetition = repetition + 1
  return False

#checks if there are 3 characters in a column
def being_in_a_col(mark):
  global tictac_list
  repetition = 0
  while repetition < 3:
    if mark in tictac_list[0][repetition] + tictac_list[1][repetition] + tictac_list[2][repetition]:
      return True
    repetition = repetition + 1
  return False

#checks if there are 3 characters in a diagonal
def being_in_a_diag(mark):
  global tictac_list
  repetition = 0
  diag_1 = ""
  diag_2 = ""
  reverse_repetition = 2
  while repetition < 3:
    diag_1 = diag_1 + tictac_list[repetition][repetition]
    diag_2 = diag_2 + tictac_list[repetition][reverse_repetition]
    repetition = repetition + 1
    reverse_repetition = reverse_repetition - 1
  if mark in diag_1 or mark in diag_2:
    return True
  return False

#Searches to make sure the above conditions are true
def search(mark):
  if being_in_a_row(mark) == True:
    return True
  elif being_in_a_col(mark) == True:
    return True
  elif being_in_a_diag(mark) == True:
    return True
  else:
    return False

#updates the board depending on what the user says
def update_board(num):
  global row_num
  global col_num
  global tictac_list
  mark = ""
  if num == 1:
    mark = "X"
  if num == 2:
    mark = "O"
  tictac_list[int(row_num) - 1][int(col_num) - 1] = mark
  tictactoe_board()

#Allows computer to place its mark randomly
def computer_edits():
  global tictac_list
  row = random.randint(0,2)
  col = random.randint(0,2)
  while tictac_list[row][col] != "_":
    row = random.randint(0,2)
    col = random.randint(0,2)
  tictac_list[row][col] = "O"
  print()
  print("The Computer's response is:")
  tictactoe_board()

#Checks to see if the entire Tic-Tac-Toe board is filled or not
def full_board():
  global tictac_list
  for row in tictac_list:
    for col in row:
      if col == "_":
        return False
  print()
  print("It's a Tie!")
  return True

#Main function for 1 player game
def main_single_player():
  instructions_1()
  tictactoe_board()
  while search("XXX") or search("OOO") == False:
    userinput(1)
    update_board(1)
    if search("XXX") == True:
      print()
      print("Player 1 Wins!")
      break
    if full_board():
      break
    computer_edits()
    if search("OOO") == True:
      print()
      print("The Computer Wins!")
      break
    if full_board():
      break

#Main function for 2 player game
def main_double_player():
  instructions_2()
  tictactoe_board()
  while search("XXX") or search("OOO") == False:
    userinput(1)
    update_board(1)
    if search("XXX") == True:
      print()
      print("Player 1 Wins!")
      break
    if full_board():
      break
    userinput(2)
    update_board(2)
    if search("OOO") == True:
      print()
      print("Player 2 Wins!")
      break
    if full_board():
      break

#Decides which Game Mode will be played
StartGame = input("Welcome to Tic-Tac-Toe! Press 1 for single player or press 2 for double players: ")
while StartGame not in ("1","2"): 
  print()
  print("Please enter either 1 or 2.")
  print()
  StartGame = input("Welcome to Tic-Tac-Toe! Press 1 for single player or press 2 for double players: ")
if int(StartGame) == 1:
  main_single_player()
elif int(StartGame) == 2:
  main_double_player()
