import sys

print('The command line arguments are:')
for i in sys.argv:  # till system arguments are there
    print(i)  # prints args
print('\n\nThe PYTHONPATH is', sys.path, '\n')  # prints the system path of all the directories.

# ==========================================================================

import os;
print("The current directory is : ",os.getcwd())    # Command to print the current dir from where prog is launched

# ==========================================================================

from PythonLearning4 import sqrt
print(sqrt)
# it is running all progs in PythonLearning4

from math import sqrt
print("Square root of 16 is", sqrt(16))
print('\n')



# **A module's __name__ attribute use==========================================================================

if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')
print('\n')


def say_hi():
    print('Hi, this is mymodule speaking.')
__version__ = '0.1'

say_hi()
print('\n')

# *====================================

import pymodule
pymodule.sayhi()
print("name : ",pymodule.__name__)
print("version : ",pymodule.__version__)

