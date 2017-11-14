#
# hw10pr1.py
# Name: Lawrence Mao
# Date: 11-7-17
#

# First, the class definition
# Below, we define several useful objects of type Date
#  +++ keep those and/or add your own! +++


class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    # the constructor is always named __init__ !
    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    # the "printing" function is always named __repr__ !
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s


    # here is an example of a "method" of the Date class:
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0: return True
        elif self.year % 100 == 0: return False
        elif self.year % 4 == 0: return True
        return False


    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew


    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False


    def __eq__(self, d2):
        """ Overrides the == operator so that it declares two of the same dates in history as ==
            This way , we don't need to use the awkward d.equals(d2) syntax...
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False


    def isBefore(self, d2):
        """
        Return True if the calling object is a calendar date before the argument named d2 (which 
        will always be an object of type Date). If self and d2 represent the same day, this method 
        should return False. Similarly, if self is after d2, this should return False
        """
        if d2.year != self.year:
            return self.year < d2.year
        if d2.month != self.month:
            return self.month < d2.month
        return self.day < d2.day


    def isAfter (self, d2):
        """
        This method should return True if the calling object is a calendar date after the argument 
        named d2 (which will always be an object of type Date). If self and d2 represent the same 
        day, this method should return False. Similarly, if self is before d2, this should return False.
        """
        if d2.year != self.year:
            return self.year > d2.year
        if d2.month != self.month:
            return self.month > d2.month
        return self.day > d2.day
    

    def tomorrow(self):
        """
        Change the calling object so that it represents one calendar day after the date it 
        originally represented. This means that self.day will definitely change
        """
        fdays = 28 + self.isLeapYear()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day += 1
        if self.day > DIM[self.month]:
            self.day = 1
            self.month += 1
            if self.month == 13:
                self.year += 1
                self.month = 1


    def yesterday(self):
        """
        Change the calling object so that it represents one calendar day before the date it 
        originally represented. Again, self.day will definitely change, and self.month and 
        self.year might change
        """
        fdays = 28 + self.isLeapYear()
        DIM = [0,31,fdays,31,30,31,30,31,31,30,31,30,31]
        self.day -= 1
        if self.day < 1:
            self.month -= 1
            if self.month < 1:
                self.year -= 1
                self.month = 12
            self.day = DIM[self.month]


    def addNDays(self, N):
        """
        This method only needs to handle nonnegative integer arguments N. Like the tomorrow 
        method, this method should not return anything. Rather, it should change the calling 
        object so that it represents N calendar days after the date it originally represented.
        Print all of the dates from the starting date to the finishing date, inclusive of both 
        endpoints.
        """
        for i in range(N):
            self.tomorrow()
            print(self)


    def subNDays(self, N):
        """
        This method only needs to handle nonnegative integer arguments N. Like the addNDays 
        method, this method should not return anything. Rather, it should change the calling 
        object so that it represents N calendar days before the date it originally represented. 
        Analogous to the previous case, consider using yesterday and a for loop to implement 
        this! In addition, this method should print all of the dates from the starting date to 
        the finishing date, inclusive of both endpoints. Again, this mirrors the addNDays method.
        """
        for i in range(N):
            self.yesterday()
            print(self)


    def diff(self, d2):
        """
        Return an integer representing the number of days between self and d2. You can think of 
        it as returning the integer representing
        """
        cnt = 0
        d1 = self.copy()
        d3 = d2.copy()
        while d1.isBefore(d3):
            d1.tomorrow()
            cnt -= 1
        while d1.isAfter(d3):
            d1.yesterday()
            cnt += 1
        return cnt

    
    def dow (self):
        """
        Return a string that indicates the day of the week (dow) of the object (of type Date) that 
        calls it. That is, this method returns one of the following strings: "Monday", "Tuesday", 
        "Wednesday", "Thursday", "Friday", "Saturday", or "Sunday"
        """
        weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekday[((2 + self.diff(Date(11, 12, 2014)))%7+7)%7]


#
# lots of dates to work with...
#
# The nice this about putting them here is that they get redefined with each run
#   of the software (and this is needed for testing!)
#

d = Date(11,12,2013)
ny = Date(1,1,2018)   # new year
nd = Date(1,1,2020)   # new decade
nc = Date(1,1,2100)   # new century
graduation = Date(5,16,2021)   # alter to suit!
vacation = Date(12,16,2017)    # ditto!
sm1 = Date(10,28,1929)    # stock market crash
sn2 = Date(10,19,1987)    # another s.m. crash: Mondays in Oct. are risky...


# Question 1: nycounter() computes the total amount of days of the week (monday, tuesday... sunday) 
# that a date lands on starting from 1/1/16 for 100 years

# Question 2: birthdayCounter() showed the days my next 100 birthdays land on. The results are:
# {'Sunday': 14, 'Monday': 15, 'Tuesday': 14, 'Wednesday': 14, 'Thursday': 14, 'Friday': 15, 'Saturday': 14}

# Question 3: had to go to a biotech talk by Kevin Esvelt so didn't have time to finish this lol (not to be confused with List of Lists)

def nycounter():
    """Looking ahead to 100 years of NY celebrations..."""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # live for another 100 years...
    for year in range(2016, 2116):
        d = Date(1, 1, year)   # get ny
        print('Current date is', d)
        s = d.dow()        # get day of week
        dowd[s] += 1       # count it

    print('totals are', dowd)

    # we could return dowd here
    # but we don't need to right now
    # return dowd

def birthdayCounter():
    """Looking ahead to 100 years of birthday celebrations..."""

    dowd = {}              # dowd == 'day of week dictionary'
    dowd["Sunday"] = 0     # a 0 entry for Sunday
    dowd["Monday"] = 0     # and so on...
    dowd["Tuesday"] = 0
    dowd["Wednesday"] = 0
    dowd["Thursday"] = 0
    dowd["Friday"] = 0
    dowd["Saturday"] = 0

    # live for another 100 years...
    for year in range(2017, 2117):
        d = Date(5, 4, year)   # get ny
        print('Current date is', d)
        s = d.dow()        # get day of week
        dowd[s] += 1       # count it

    print('totals are', dowd)

    # we could return dowd here
    # but we don't need to right now
    # return dowd