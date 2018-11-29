# The global statement ================================================================
# It is impossible to assign a value to a variable defined outside a function without the global statement.

x = 50
def func():
    global x
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
print('\n'*2)

# ================================================================
def func1():
    #x = 3
    #print('x is', x)
    global x
    print('x is', x)
    x = 5
    print('Changed global x to', x)

func1()
print('Value of x is', x)
print('\t'*2)

# Default Argument Values ================================================================

def say(message, times=2):
    print(message * times)
say('Hello')
say('World', 3)
print('\t'*2)


# ================================================================
# If you have some functions with many parameters and you want to specify only some of them, then you can give values
# for such parameters by naming them - this is called keyword arguments - we use the name (keyword) instead of the
# position (which we have been using all along) to specify the arguments to the function.

def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
func(3, 7)
func(25, c=24)
func(c=50, a=100)
print('\t'*2)


# VarArgs parameters ================================================================

def total(a=5, *numbers, **phonebook):
    print('a', a)
    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item) # it will print 3 times as 1,2,3 items are being used in a for loop.
    #iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():   #
        print(first_part,second_part)

# on using below statement, a gets '10', now the format is not changed but the a's capacity to take anymore numbers is
# exhausted thus *numbers gets 1, 2, 3 .. then now the format of argument is changed thus it will be used till end

# the use of *, then ** given right to collect all the positional arguments from that point till the end
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
print('\t'*2)


# The return statement =================================

# to return from a function i.e. break out of the function. We can optionally return a value from the function as well.

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(3, 3))
print('\t'*2)


# DocStrings (documentation strings) ===========================================================================

def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
print('\t'*2)


def thisisFUN():
    '''Printing something is not easy 1.'''
print(thisisFUN.__doc__)
print('this is printed')
print('\t'*2)


def thisisFUN():
    '''Printing something is not easy 2.'''

print(thisisFUN.__doc__)
print('\t'*2)
help(thisisFUN)


sqrt=4
