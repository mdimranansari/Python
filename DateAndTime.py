# to use Python functionality for Date and time, use import statements
# predefined classes to imported as follows
from datetime import date
from datetime import time
from datetime import datetime

class DateAndTime():
    print("**Date and Time Class**")
    
    def method1(self):
        today=date.today()
        print("Today's date is : ",today)
        # printing date's individual components
        # individual day, month, year associated with now 'today' variable 
        print("Total of today : day month year == ", today.day, today.month, today.year)
        # using week day number
        # 0 = monday 6= sunday
        print("Today's weekday # :", today.weekday())
        
        days=["mon", "tue","wed","thurs","fri","satur","sun"]
        print("Today is Week#:",today.weekday(),"that means today is :",days[today.weekday()])
        # today.weekday() say is 6 since today is actually Sunday
        # then days[6] will give 'sun' as at index 6 is 'sun' inside days

        # Now, using DATETIME class
        # 'now()' provides full detail of current date-time
        today=datetime.now()
        print("The current date-time", today)
        
        #Get the current TIME
        todaytime=datetime.time(datetime.now()) #picks the now object value to pick time from and then will provide it.
        print("Just the current time :",todaytime)
        
        
def main():
    print("This is main method")
    a=DateAndTime()
    
    a.method1()
    
if __name__=="__main__":
    main()