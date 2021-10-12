import sys
import argparse

## This allows for formatting and colouring console output
class colour:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'


# This allows each square to know the value stored in it,  as well as
# which row/column, and 'box' it belongs to
class BoardNode:
  def __init__(self, num, row, col, box):
      self.num = num            # The number in the node (1-9)
      self.row = row            # Location of row
      self.col = col            # Location of column
      self.box = box            # This location of box in [3x3] sub-matrix



# This takes an 81 digit string representing a sudoku puzzle
# Blank spaces are represente by zeroes.
# It then builds an array using the string, and determines
# which row/column/box each cell belongs to, along with its value.
# It then returns this sudoku board as an array
importString = \
'900170402160040095008003000010900573040000020589007010000400700670020058301058006'
def build_board(importString):
  board = []

  for i in range(81):
    num = int(importString[i])
    row = i//9
    col = i%9
    box = 3*(row//3) + col//3
    board.append(BoardNode(num, row, col, box))

  return board 


# Prints formatted Sudoku board, colouring nodes depending on
# context
def print_sudoku(board, node, txtColour):
  txt = f'colour.{txtColour}'

  for i in range(81):
    if (i%9 == 0 and i != 0):
      print(" | ")
    if (i%27 == 0 and i != 0):
      print("  -----------------------------")
    if (i%3 == 0):
      print(" |  ", end="")
    if (i == 80):
      if(i == node):
        print(eval(txt) + str(board[i].num) + colour.END + "  |")
      else:
        print(str(board[i].num) + "  |")
    else:
      if(i == node):
        print(eval(txt) + str(board[i].num) + colour.END + " ", end="")
      else:
        print(str(board[i].num) + " ", end="")
  print('\n')


# Searches for a position without a value
def find_move(board):
  for i in range(81):
    if (board[i].num == 0):
      return i
  return None


# This determines if a given move is valid
# It takes a sudoku board, a test value 1-9, and an index (cell)
# Returns false if the test value is already present in the row/col/box
# that the cell belongs to.
# Returns true if the move is valid
def valid(board, testNum, index):
  row = board[index].row
  col = board[index].col
  box = board[index].box
  boxStart = (index//27)*27 + (box%3)*3

# search the row 
  for i in range(row*9, row*9+9):
    if testNum == board[i].num: #return false if test number in row already
      return False

# Search the column
  for i in range(col, 81, 9):
    if testNum == board[i].num: #return false if number in col already
      return False

# Search the box
  for i in range(boxStart, boxStart+20, 9):
    for j in range(3):
      if testNum == board[i+j].num: #return false if number in sub-box already
        return False

  return True #return true if number was valid in the cell


# Simple Depth-First search with backtracking.
# Function takes a sudoku board, and a Boolean
# And attempts to find an empty cell:
#   if there are no empty cells, the puzzle is solved.
# Otherwise, it then iterates through the numbers 1-9, checking 
# if they are valid moves for the cell of interest.
# If the move is valid, the function places that number in 
# the cell, and recursively calls solve()
# If the function has has no valid moves to make,
# it backtracks and attempts another number
# If printing is set to True, the board is printed for each move
# If steps is true, 'enter' must be pressed each iteration
def solve(board, printing, steps): 
  find = find_move(board) # find empty cell
  if not find:
      print(colour.UNDERLINE\
        +colour.YELLOW + "\nWE COMPLETED THE PUZZLE FAM!\n" + colour.END + colour.END)        
      return True # puzzle is solved
  else:
    index = find # we found an empty cell

  for testNum in range(1,10): # iterate through possible numbers
    if valid(board, testNum, index): # check if the number is valid
        board[index].num = testNum # if valid, place the number in the board

        if steps == True: ## prompts user to hit enter
          input(colour.PURPLE + 'Hit enter for next move...' + colour.END)
        
        ## prints the move
        print('placed ' + colour.GREEN + f'{testNum}' + colour.END + f' in index {index}')

        if printing == True: ## print the node green
          print_sudoku(board, index, 'GREEN')   


        if solve(board, printing, steps): # call solve on the updated board
          return True 
        print('removed ' + colour.RED + f'{testNum}' + colour.END +f' from {index}')
      
        if printing == True: ## print backtrack node red
          print_sudoku(board, index, 'RED') 

        board[index].num = 0 #if no valid moves, remove last number

  print(colour.RED + "No possible moves here... Backtracking......\n" + colour.END)

  if steps == True: ## prompt user to hit enter
    input(colour.CYAN+'Hit enter to remove a number'+colour.END)

  return False  # and backtrack

# This is the 'driver' solve function
# it takes two booleans - 'printing' and 'steps'
# it builds the puzzle and displays it
# Then it solves the puzzle. and prints the solution
# Depending on the parameters, it can display every intermediate
# step, and wait at each step for user input 
def solve_sudoku(printing, steps):
  puzzle = build_board(importString)
  print(colour.YELLOW + 'HERE IS THE ORIGINAL PUZZLE:' + colour.END)
  print_sudoku(puzzle, -1, -1)
  print(colour.YELLOW + 'Starting the solve process...' + colour.END)

  solve(puzzle, printing, steps)
  print_sudoku(puzzle, -1, -1)

#############################################################################
# The following are for the main() function, and getting input/printing information
title = '----> Backtracking Depth-First Search Sudoku Solving Software'
version = '-------> 1.0.0'
author = '------> Zac Greene'

# to facilitate printing to console
info1 = 'This program uses a backtracking depth-first search\n'\
'in order to solve a sudoku puzzle.\n'\
'Essentially, the algorithm proceeds as follows:\n'\
'1. Search for a square without a number (equal to 0)\n'\
'\t\tif none are found, the puzzle is solved'

info2 = '2. For the square:\n'\
'\titerate through possible values (1-9):\n'\
'\t  if the number is valid:\n\t\tplace it, update the board,\n' \
'\t\tand recursively go back to step 1.\n'\
'\t  if no value 1-9 is valid:\n\t\ta previous value was incorrectly assigned,\n'\
'\t\tremove the last value,\n\t\treturn failure,\n'\
'\treturn failure.'

## for text formatting
h1 = 'colour.BOLD + colour.UNDERLINE + colour.PURPLE'
h2 = 'colour.BOLD + colour.YELLOW'
h3 = 'colour.BOLD + colour.CYAN'

# Parser for command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--print', action='store_true', help='Prints sudoku board at every step', \
    required = False, default = False)
parser.add_argument('-s', '--steps', action='store_true',  help='Prompts for input before each move', \
    required = False, default = False)
args = parser.parse_args()


# Main function
def main(argv):

  printing = args.print
  steps = args.steps
  
  print_intro() ## prints the intro information

  if (args.print == False) and (args.steps == False): # if both set to false, double-check
    printing = check_printing(printing)
    steps = check_steps(steps)

  solve_sudoku(printing, steps)

## This prints intro information
def print_intro():
  input(colour.BLUE + '\nHit enter for some info:\n'+colour.END)
  print(eval(h1) + f'{title}' + colour.END)
  print(eval(h2) + f'version {version}' + colour.END)
  print(eval(h3) + f'by {author}' + colour.END)

  input('\nenter again...\n')
  print(info1 + '\n' + info2)
 
## checks if printing preferences are set correctly
def check_printing(printing):
  if printing:      ##for text formatting
    pc='colour.GREEN'
  else:
    pc='colour.RED'

  input(colour.BLUE + '\nenter again...\n' + colour.END)
  print(colour.BLUE + 'Pretty sure you did not include any command-line arguments...\
  \nif you forgot to (or did not) you can change them now:' + colour.END)
  print('Printing every move is ' + eval(pc) + f'{printing}' + colour.END)

  answer = input(eval(h3) + 'Would you like to change this?' + colour.END)  

  if answer.lower() == 'n':
    return printing
  if answer.lower() == 'y':
    return change_print()

## allows for changing of printing settings
def change_print():
  print(eval(h1) + '\n------> Printing:' + colour.END)
  print('Enabling this will display the sudoku board every time a move is made')
  print('Disabling will print only the moves\n\n')
  printing=False #set as default

  answer = input(colour.PURPLE + 'Enable printing? (Y/N)' + colour.END)

  if answer.lower() == 'n':
    printing = False
  if answer.lower() == 'y':
    printing = True

  print(f'\n---> Printing set to {printing}!\n')
  return printing

# checks if step-by-step solving preferences are set correctly
def check_steps(steps):
  if steps: 
    sc='colour.GREEN'
  else:
    sc='colour.RED'

  input(colour.BLUE + '\nenter again...\n' + colour.END)
  print('Step-by-steps moves currently set to ' + eval(sc) + f'{steps}' + colour.END)

  answer = input(eval(h3) + 'Would you like to change this?' + colour.END)  

  if answer.lower() == 'n':
    return steps
  if answer.lower() == 'y':
    return change_steps()

# allows changing of step-by-step preferences
def change_steps():
  print(eval(h1) + '\n------> Step-by-step moves:' + colour.END)
  print('Enabling this will prompt the user to hit enter to make each move')
  print(colour.RED + 'WARNING' + colour.END + ' : this might require mashing that enter key!')
  print('Disabling will allow the program to proceed in the blink of an eye\n\n')
  steps=False

  answer = input(colour.PURPLE + 'Enable step-by-step solving? (Y/N)' + colour.END)

  if answer.lower() == 'n':
    steps = False
  if answer.lower() == 'y':
    steps = True

  print(f'\n---> Step-by-step solving set to {steps}!\n')
  return steps

if __name__ == "__main__":
  main(sys.argv[0:])
  