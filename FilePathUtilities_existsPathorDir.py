#To find if the file exists, path of file, if given path is file or a directory.

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    print(os.name) #Prints the os name
    #Output: 
    #nt
    
    #CHECKING FILE'S EXISTENSE, IF THE PATH IS A FILE PATH OR A DIRECTORY PATH
    print("Item exists? : "+str(path.exists("D:/Coding/files/textfile1.txt")))
    print("Item is a file? : "+str(path.isfile("D:/Coding/files/textfile1.txt")))
    print("Item is a directory? : "+str(path.isdir("D:/Coding/files/textfile1.txt")))
    #Output:
    #Item exists? : True
    #Item is a file? : True
    #Item is a directory? : False
    
    # TO FIND THE REAL PATH, SPLITTING NAME FROM THE REAL PATH OF FILE
    print("Item path : "+str(path.realpath("D:/Coding/files/textfile1.txt")))
    print("Item path and name : "+str(path.split("D:/Coding/files/textfile1.txt")))
    print("Item realpath and name : "+str(path.split(path.realpath("D:/Coding/files/textfile1.txt"))))
    filepath,filename=path.split("D:/Coding/files/textfile1.txt")
    print("File path : "+filepath)
    print("File name : "+filename)
    filepath,filename=path.split(path.realpath("D:/Coding/files/textfile1.txt"))
    print("File path : "+filepath)
    print("File name : "+filename)
    #Output:
    #Item path : D:\Coding\files\textfile1.txt
    #Item path and name : ('D:/Coding/files', 'textfile1.txt')
    #Item realpath and name : ('D:\\Coding\\files', 'textfile1.txt')
    #File path : D:/Coding/files
    #File name : textfile1.txt
    #File path : D:\Coding\files
    #File name : textfile1.txt
    
    #TO GET MODIFICATION TIME
    t=time.ctime(path.getmtime("D:/Coding/files/textfile1.txt"))    #First way
    print(t)
    print("Modification Time : "+str(datetime.datetime.fromtimestamp(path.getmtime("D:/Coding/files/textfile1.txt")))) #Second way
    #Output:
    #Sat Jan  5 20:49:49 2019
    #Modification Time : 2019-01-05 20:49:49.635641
    
    #TO GET THE TIME SINCE THE MODIFICATION WAS DONE
    td=datetime.datetime.now()-datetime.datetime.fromtimestamp(path.getmtime("D:/Coding/files/textfile1.txt"))
    print("Time since modification : "+str(td)) #Modification time
    print("Time since modification in seconds : "+str(td.total_seconds())+" seconds")   #Modification time in seconds
    #Output:
    #Time since modification : 17:48:27.520957
    #Time since modification in seconds : 64107.520957 seconds
    
if __name__=="__main__":
    main()