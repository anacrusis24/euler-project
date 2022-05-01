'''
---------- display_problem.py ----------
Time    :  2022/05/01 02:36:31
Version :  1.0
Author  :  Austin Villegas 
Github  :  https://github.com/anacrusis24
Contact :  ajv131@gmail.com
Desc    :  Function to cleanly display results
'''

##### Define Functions #####
def display_results(problem_header, problem_statement, problem_to_solve, answer):
    '''
    @display_results
    Function prints the results of the of the euler test
    
    @Input
    problem_header: the display header for the test
    problem_statement: the problem statement 
    problem_to_solve: the number of the euler problem
    answer: the answer to the problem
    
    @Output
    None
    '''
    print('\n', problem_header)
    print(problem_statement, '\n')
    print(f'The answer to Euler problem {problem_to_solve} is:', answer, '\n')

    return None