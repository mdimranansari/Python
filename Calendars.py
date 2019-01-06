import calendar

#Creating and using a plain text calendar, using text calendar class
c= calendar.TextCalendar(calendar.SUNDAY) #it gives the day of the week when the calendar is starting on while displaying the month
print(c) #this prints the value of object c which will be <calendar.TextCalendar object at 0x03193A90> or similar
print("\n")

st= c.formatmonth(2018, 1, 0, 0) # here we use formatmonth() to format a month into a text string and then we will print the result 
print(st) 
print("\n")

c= calendar.TextCalendar(calendar.MONDAY) # here will see difference from above
st= c.formatmonth(2018, 12, 0, 0)
print(st) 
print("\n")

#Now creating an HTML formatted calendar using HTMLCalendar class
hc= calendar.HTMLCalendar(calendar.MONDAY)
st=hc.formatmonth(2017, 2, 2018)
print(st)
# This will give an HTML code format of the calendar in table format. This will also provide few 'class' attributes of HTML in the code by python calendar library
# this will help if one wants to define some CSS classes like month, sunday, monday etc it can be done using any CSS code that one wants to include this HTML in.
print("\n")

# Now to iterate or loop over days of a month
for i in c.itermonthdays(2018, 12):
    print(i) #this method will return numbers that represent the chosen month as chosen using number of the month...i.e. here '12' is of 'December'
    # in output there will be days represented by 0 only, this means there are days displayed in the calendar that belong to other month.
print("\n")
    
# Now dealing with the Calendar of a different locale.
for month_name in calendar.month_name:
    print(month_name)
print("\n")

for day_name in calendar.day_name:
    print(day_name)
    
# in English speaking country/locale above gives month and days names in English but if the locale of system is set to other format or system is in 
# some other country then the month and days will be printed in that locale's accord.

# Team meeting dates of next year, say every Friday of each month.
print("\n")

print("Team meetings will be on : ")
for m in range(1,13): #13 is non-inclusive so months will be 1 to 12
    # Now the concept is that if the day number of a particular day in week is 0 then it means that day is part of a different month since calendar sets them to 0
    # The 0 concept was displayed above when the days that are not part of current month are set to be 0 in calendar.
    # Thus, if the number of Friday or Friday value of the first week is 0 that means the Friday was in the previous month and current month started on the Saturday.
     
    cal=calendar.monthcalendar(2018,m)
    weekone=cal[0]
    weektwo=cal[1]
    
    if weekone[calendar.FRIDAY]!=0:
        meetday=weekone[calendar.FRIDAY]
    else:
        meetday=weektwo[calendar.FRIDAY]
        
    print("%35s %2d" % (calendar.month_name[m], meetday))
    