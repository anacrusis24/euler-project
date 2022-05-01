'''
---------- main.py ----------
Time    :  2022/04/30 22:47:30
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  The main program to see the answers to the Euler problems
'''

##### Imports #####
import numpy as np
import os
from euler_problem.euler_problem_1_10 import *
from problem_statement import *


##### Make Exceptions ######
class NotInRange(Exception):
    'Raised when euler problem input is not in range of completed problems'

class NotYesNo(Exception):
    'Raised when answer to continue is not y or n'


##### Main Program #####
if __name__ == '__main__':
    # Global variables we need for display
    num_problems = len(os.listdir('euler_problem\\')) - 2
    problem_prompt = 'Enter which Euler problem you would like to solve: '
    solve_prompt = 'Would you like to solve more problems (y/n): '

    # Loop to continue solving Euler problems
    continue_solving = True
    while continue_solving:

        # Get the problem to solve 
        while True:
            try:
                # Get the problem from the user
                problem_to_solve = int(input(problem_prompt))

                # Raise an exception if not an integer
                if not isinstance(problem_to_solve, int):
                    raise NotAnInteger
                # Raise an exception if not in range
                elif problem_to_solve > num_problems:
                    raise NotInRange
                else:
                    problem_header = f'---------- Euler Problem {problem_to_solve} ----------'
                    break
            except ValueError:
                print('Only enter integer values. Ex. 1, 2, 3,...')
            except NotInRange:
                print(f'Enter only integers from 1 to {num_problems}')

        
        ### Euler Problem 1 ###
        if problem_to_solve == 1:
            # problem_statement = '''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.\nFind the sum of all the multiples of 3 or 5 below 1000.'''
            sum_mult_3_5 = sum_multiples(np.array([3, 5]), 1000)
            print('\n', problem_header)
            print(problem_statement_1, '\n')
            print(f'The answer to Euler problem {problem_to_solve} is:', sum_mult_3_5, '\n')
        

        # Let user decide weather to keep solving or not 
        while True:
            try:
                # Collect user answer
                solve_answer = input(solve_prompt)

                # Raise an exception if not 'y' or 'n'
                if solve_answer not in ['y', 'n']:
                    raise NotYesNo
                else:
                    break
            except NotYesNo:
                print('Enter only \'y\' or \'n\'')

        # End solving session 
        if solve_answer == 'n':
            continue_solving = False