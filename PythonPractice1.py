def main():
    print("Hello World")
#on running above line nothing will happen because there is nothing 
#calling the main method. To run the main method the has to be something 
#calling main method.

#Q: Now, question is that unlike java main is not a predefined method 
#in Python? or is it?
#A: 

# Python does not have the braces (curly braces), or code blocks it 
#uses indentation to indicate where that code belongs.

# Now to execute main()

if __name__=='__main__':
    main()
    
#above line helps distinguish if the python file is being executed by 
#itself or is it being included in another project where it is actually
#called as a separate library and we don't want it to execute any code
#unprompted.

