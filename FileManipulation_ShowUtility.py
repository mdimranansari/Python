import os
from os import path
import shutil #to use the Shell Utility
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("D:/Coding/files/textfile1.txt")==True:
        print("exists")
        
        # MAKING DUPLICATE OF A FILE
        source=path.realpath("D:/Coding/files/textfile1.txt")
        print(str(source))
        destination=source+".bak"
        shutil.copy(source, destination)    # only copies the file content not its matadata like modification time, author etc
        shutil.copystat(source, destination)    #copies the matadata 
        print("done")
        
        #TO RENAME A FILE
        os.rename(source,"newFile.text")
        
        #ZIPPING A DIRECTORY OR A PATH , zip file using makearchive()
        root_dir,tail=path.split(source)
        shutil.make_archive("archive","zip",root_dir)
        
        #ADDING SPECIFIC FILES TO ARCHIVE OR ZIPPING SPECIFIC FILES
        with ZipFile("testzip.zip","w") as newzip:  #ZipFile() is an object constructor
            # 'with' keyword creates a local scope and makes it easy to work with objects
            # her a new zipfile object is created and using 'w' to specify we are gonna write to the file
            # the object newzip will be temporarily renamed then will use that obj to manipulate data and write content to file
            newzip.write("D:/Coding/files/textfile1.txt")
            newzip.write("D:/Coding/files/textfile1.txt.bak")
            #so these 2 files will be added to archive.zip
            
            #Above creates a new zip file and adds txt and txt.bak file into it. 