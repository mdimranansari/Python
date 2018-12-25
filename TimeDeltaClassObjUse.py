from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

class TimeDeltaClassObjUse():
    print("This is use of TimeDelta Class's use")
    
    #A timedelta is a span of time not a particular date or time
    # Used to do time based calculations
    print(timedelta(days=365, hours=5, minutes=4))
    timedel=timedelta(days=365, hours=5, minutes=4)
    print("\n")
    
    now=datetime.now()
    print("Today is : ",now)
    print("\n")
    
    #now, to find today's date one year from now
    print("One year from now will be : ",now+timedelta(days=365))
    print("The timedelta from now will be: ", now+timedel)
    print("\n")
    
    #Now, calculate using more than one argument
    print("2 weeks 3 days from now will be :",now+timedelta(weeks=2,days=3))
    print("2 weeks 3 days from now was :",now-timedelta(weeks=2,days=3))
    print("\n")
    
    #with strftime formatting of time
    t=now-timedelta(weeks=2,days=3)
    s=t.strftime("%A %B %d, %Y")
    print("2 weeks 3 days ago was :",s)
    print("\n")
    
    #how many days till next april fool's date
    today=date.today()
    print("Today is : ",today)
    afd=date(today.year, 4, 1)  #creating a date
    print("April Fool's day is on :",afd)
    print("\n")
    
    if(today>afd):
        print("April Fool's day of this year is already gone by %d days ago"%((today-afd).days))
        afd=afd.replace(year=today.year+1) #since april fool's day is already gone thus we are changing it to next year
        
        #now calculate to next april fool day
    print("\n")
    time_to_afd=afd-today
    print("It's just ",time_to_afd.days,"days until April Fool's Day")
    print("\n")
    
    #or you can write-
    print("It's just %d days to next April Fool's day"%time_to_afd.days)
    