#Classes are defined using 'class' keyword
# if this class inherited any other class then that class name will be
# put in the parenthesis
# first argument to any of the method of the class is the 'self' argument
# 'self' refers to the object itself. it is like 'this' keyword of JS
#  
class PythonClass():
    def method1(self):
        print("Class1 method 1")
        
    def method2(self,someString):
        print("Class1 method2 :"+someString)
        
class secondClass(PythonClass): #this class inherits above class
    def method1(self):
        PythonClass.method1(self) #need to pass 'self' since inside class
        print("Second Class method 1")
        
    def method2(self,someString):
        print("Second Class method 2")
                
#this main is outside the class
def main():
    c=PythonClass() #instantiate object instance of class and now can 
                    # call methods of class using 'c' object of class.
    c.method1()
    c.method2("argument of Class 1 method2")
    # here self keyword doesn't have to be supplied as automatically
    # taken care of by python runtime
    
    d=secondClass()
    
    d.method1()
    d.method2("argument of class2 method2") #this argument won't print`
    
    #print("Python Class and Method")
    
if __name__=="__main__":
    main()