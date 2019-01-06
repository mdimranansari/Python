def main():
    f=open("D:/Coding/files/textfile1.txt", "w+")# open() has 2 parameters, first the file you want to access. Second the kind of access you need.
                                # w= write access, w+ = create the file if not already exist, a= Append to the data end of file not overwrite it.
                                #D:\Coding\files
    for i in range(10):
        f.write("this is text " + str(i)+"\r\n")
    f.close()
    print("Created")
    appendFile()
    read()
    readLineByLines()

def appendFile():   # To append at the end of file not in between
    f=open("D:/Coding/files/append.txt", "a")
    for i in range(10):
        f.write("This is text "+ str(i)+ "\r\n")
    f.close()
    print("appended")

def read(): 
    f=open("D:/Coding/files/append.txt", "r")
    if f.mode=='r':         #here check if the file was actually opened then only the file will be able to be read otherwise it will display error-
                            # PermissionError: [Errno 13] Permission denied: 'D:/Coding/files/append.txt
        content=f.read()
        print(content)
    f.close()
    print("read")
    
def readLineByLines():   #To read line by line for a larger file. Makes no sense to read all the lines. Reads content as an array of individual lines.
    f=open("D:/Coding/files/append.txt", "r")
    if f.mode=='r':
        rl=f.readlines()    #printing it will give all the texts including \n and wide spaces.
        for x in rl:
            print(x+" line")    #This will print the file linewise
         
        print(rl)       
    f.close()
    print("readLines")
        
if __name__=="__main__":
    main()
