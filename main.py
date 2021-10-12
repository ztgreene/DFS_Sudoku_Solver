import sys
import getopt
import solver
import argparse

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



title = '----> Backtracking Depth-First Search Sudoku Solving Software'
version = '-------> 1.0.0'
author = '------> Zac Greene'

h1 = 'colour.BOLD + colour.UNDERLINE + colour.PURPLE'
h2 = 'colour.BOLD + colour.YELLOW'
h3 = 'colour.BOLD + colour.CYAN'


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--print', action='store_true', help='Prints sudoku board at every step', \
    required = False, default = False)
parser.add_argument('-s', '--steps', action='store_true',  help='Prompts for input before each move', \
    required = False, default = False)
args = parser.parse_args()


def main(argv):

  printing = args.print
  steps = args.steps

  print_intro() ## prints the intro information

  if (args.print == False) and (args.steps == False): # if both set to false, double-check
    printing = check_printing(printing)
    steps = check_steps(steps)

  solver.solve_sudoku(printing, steps)
  

def print_intro():
  input(colour.BLUE + '\nHit enter for some info:\n'+colour.END)
  print(eval(h1) + f'{title}' + colour.END)
  print(eval(h2) + f'version {version}' + colour.END)
  print(eval(h3) + f'by {author}' + colour.END)

  input('\nenter again...\n')
  print(info1 + '\n' + info2)
 

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

def check_steps(steps):
  if steps: 
    sc='colour.GREEN'
  else:
    sc='colour.RED'

  #input(colour.BLUE + '\nenter again...\n' + colour.END)
  print('Step-by-steps moves currently set to ' + eval(sc) + f'{steps}' + colour.END)

  answer = input(eval(h3) + 'Would you like to change this?' + colour.END)  

  if answer.lower() == 'n':
    return steps
  if answer.lower() == 'y':
    return change_steps()

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
  colour = solver.colour
  main(sys.argv[0:])
  