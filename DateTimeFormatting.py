from datetime import date
from datetime import time
from datetime import datetime

class DateTimeFormatting():
    print("This is Date Time Formatting Class")
    now=datetime.now()
    print("Current Date Time : ",now)

def main():
    print("Start of main")
    d=DateTimeFormatting()
    #to format the DATE use 'strf' on the return string of now()
    # use control codes-
    # %y/%Y = year, %a/%A=weeday, %b/%B=month, %d=day of month
    print("\n"*2)
    
    print(d.now.strftime("The current Year is : %Y"))
    #above is exactly same as-
    print(datetime.now().strftime("The current Year is : %Y"))
    print(datetime.now().strftime("Full use of formatting- Year %Y, Day %A, Month %B, Date of month is %B %d"))
    print("\n"*2)
    
    #Now, for Locale specific information-
    # %c=locale's date and time, %x=locale's date, %X=locale's time
    print(d.now.strftime("The locale date and time : %c"))
    print(d.now.strftime("The locale date : %x"))
    print(d.now.strftime("The locale time : %X"))
    print("\n"*2)
    
    #TIME FORMATTING
    #%I/%H=12/24 Hour, %M=minutes, %S=seconds, %p=locale's AM/PM
    print(d.now.strftime("The locale time- %I:%M:%S %p"))
    print(d.now.strftime("The locale 24 Hour time- %H:%M:%S"))
    
    
    
if __name__=="__main__":
    main()