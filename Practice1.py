# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.

class Age:

    def age100(self):
        addyears=100
        self.age=input("Enter your current age : ")
        self.nm=input("Enter your name : ")
        self.age=int(self.age)    #converted the input from string to int
        self.age+=addyears
        print("Your age after 100 years will be : ", self.age)
        print("Your name will remain same : ", self.nm)

    def multiplePrints(self):
        timesinput=int(input("Enter the number times you want to print : "))

        i=0
        while i<timesinput:
            print(self.age)
            i+=1
            print("\n"*2)

classobj=Age()
classobj.age100()
classobj.multiplePrints()
