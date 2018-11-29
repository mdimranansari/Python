# Functiona are defined using 'def' keyword, and : indicates start of
# function scope block
#from _ast import Num

def func1():
    print("This is a function")
    
func1() #This is a function
print(func1())  #Prints following
#This is a function
#None
# -above is due to func1() execution and then print statement execution
# but since func1() does not return any value thus None is printed as the
# string value of None
  
print(func1)    #<function func1 at 0x000000DBF8895158>
#above the func1() is not being executed but we are printing the value of
# function definition itself which evaluates to the above string value
# demonstrating that functions themselves are objects that can be passed
# around to other pieces of python code.

def func2(arg1, arg2):
    print(arg1 ," ", arg2)

def cube(x):
    return(x*x*x)

print(" ")
func2(10,20)
print(func2(10,20))

print(" ")
cube(30)    #won't print anything as no print inside the function
print(cube(3))

def power(num,x=2):
    result=1
    for i in range(x): #runs for the value of x from 0 to 2 bydefault i.e. 2 times
        result=result*num
    return result
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
print(power(10,3))
print(power(10))
print(power(x=20,num=3)) #if you are supplying the name of argument along
# then even on reversing order or in any order you want to supply values
# it is allowed in python

print(" ")
# we can also use variable argument in Python
def variableArg(*args):
    result=0
    for j in args: # it runs for all the values in variableArg() arguments
        result=result+j
    return result

print(variableArg(10,20,30,40,50))

#variable argument should always be the last parameter if provided with
# formal arguments
def varArgFormalArg(m,n,*o):
    res=1
    for i in o:
        res*=i
    return m+n+res

print(varArgFormalArg(10, 20, 1,2,3,4))
