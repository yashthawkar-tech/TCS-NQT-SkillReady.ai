#HackerRank Leap Year Question

#An extra day is added to the calendar almost 
# every four years as February 29, and the day is called a leap day.
#It corrects the calendar for the fact that our planet takes
#approximately 365.25 days to orbit the sun. A leap year contains a leap day.

#In the Gregorian calendar, three conditions are used to identify leap years:
#Condition 1: The year can be evenly divided by 4, is a leap year, unless:
#Condition 2: The year can be evenly divided by 100, it is NOT a leap year, unless:
#Condition 3: The year is also evenly divisible by 400. Then it is a leap year.


def is_leap(year):
    leap = False
    
    return (year%4==0) and(year%100!=0) or (year%400==0) 
    # if year%400==0:
    #     return True
    # elif year %100==0:
    #     return False
    # elif year % 4==0:
    #     return True
    # else:
    #     return False
    return leap

year = int(input())
print(is_leap(year))