# Written by Cameron Haddock
# Submitted as a solution to Project Euler's Problem 19

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?



class Date:
    DAYS_IN_MONTH = [31,29,31,30,31,30,31,31,30,31,30,31]
    DAYS_IN_WEEK = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    def __init__(self,day,month,year,weekday):
        self.day = day
        self.month = month
        self.year = year
        self.weekday = weekday

    @staticmethod
    def is_leap_year(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False
    
    def next_day(self):
        new_day = Date(self.day,self.month,self.year,self.weekday)
        new_day.day += 1
        new_day.weekday = (new_day.weekday + 1) % 7
        if new_day.day > new_day.DAYS_IN_MONTH[new_day.month-1]:
            new_day.day = 1
            new_day.month += 1
        if new_day.day == 29 and new_day.month == 2:
            if not Date.is_leap_year(new_day.year):
                new_day.day = 1
                new_day.month += 1
        if new_day.month > 12:
            new_day.month = 1
            new_day.year += 1
        return new_day

    def __eq__(self,other):
        return self.day == other.day and self.month == other.month and self.year == other.year
    def __ne__(self,other):
        return not (self == other)
    def __le__(self,other):
        if self.year > other.year:
            return False
        if self.month > other.year:
            return False
        if self.day > other.day:
            return False
        return True
        
    
    def is_sunday(self):
        return self.weekday == 6
    def is_first(self):
        return self.day == 1

    def __str__(self):
        return str(self.year) + str(self.month).rjust(2,'0') + str(self.day).rjust(2,'0') + ' ' + self.DAYS_IN_WEEK[self.weekday]


def count_sundays():
    current_day = Date(1,1,1901,1)
    num_sundays = 0
    while current_day <= Date(31,12,2000,0):
        if current_day.is_sunday() and current_day.is_first():
            num_sundays += 1
        current_day = current_day.next_day()
    return num_sundays

print(count_sundays())