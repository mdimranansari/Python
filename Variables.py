f=0
print(f)

f="global"
print(f)

#print("this is a string"+123)   #CE
#print("this is a string"+123)
#TypeError: must be str, not int
#Reason: Python is strongly typed language, we cannot change the type
#while operation and combine it with other types.

#Now, to doe this convert 123 into a string using method 'str'
print("this is a string "+str(123))

print("\n")

#Global and Locals
def localFunc():
    f="local"
    print(f)
    
localFunc() #runs the above defined function
print(f)    #prints global available value of f
# a local and global variable with same names are 2 different variables.
# to continue with the local variable as global, or to turn it into
# global- > tell the function that f is global 
print("\n")
def globalFunc():
    global f
    f="NOW Global"
    print("value of f from inside function "+f)
    
globalFunc()
print("value of f outside the function "+f)


#now to delete the definition of variable previously declared
del f
print(f)    #CE : NameError: name 'f' is not defined
