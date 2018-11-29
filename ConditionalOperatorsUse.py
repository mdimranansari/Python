def main():
    x,y=10,100
    if(x<y):
        st="x is less than y"
    elif(x>y):  #elif is else if condition combined together
        st="y is less than x"
    else:
        st="x and y are equal or some other shit happened!!!s"
        
    print(st)
    

    
# there is no equivalent to switch condition in Python as of now.

# for more complex scenarios we use 'conditional statements' in Python.
# Conditional Statement allows to write more complex comparisons in one line.
# it more concise way of writin comparision logic.
# SYNTAX:
# a if C else b"

    st="x is greater than y" if (x>y) else "y is greater than x or equal" 
    print(st)
    
    
if __name__=="__main__":
    main()