def main():
    x=0
    #while loop
    while(x<5):
        print(x)
        x=x+1

    print("")
    for i in range(1,5):
        print(i)
        
    print("")
    #range(x) gives the values 0 to x-1
    #range(x,y) gives the values x to y-1
    
    #Now, for loop over collection
    days=["mon","tue","wed","thurs","fri","sat","sun"]
    for i in days:
        print(i)
    
    print("")
    #using break can continue statements
    for i in range(1,10):
        if(i==8): break #runs from 1 to 4 on 5 it will break
        # break causes this for loop to break and fall to the next block
        # of statement
        if(i==5): continue  #will skip 5 and then continue with the loop
        
        print(i)
        
    print("")
    
    days=["mon","tue","wed","thurs","fri","sat","sun"]
    for i,d in enumerate(days): #enumerate() gives the index thus this 
        # will give index along with the values of the days array
        print(i,d)
    #for loop does not generally uses index variable for loops
    #however it can use loop counter if needed    
      
if __name__=="__main__":
    main()


    