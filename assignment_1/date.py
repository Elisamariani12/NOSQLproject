from random import randint
from datetime import date

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.year = year
        self.month = month

    def __str__(self):
        return "{:02d}/{:02d}/{:04d}".format(self.day, self.month, self.year)

    @staticmethod
    def generate_random(monthMin = 1, monthMax = 12, yearMin = 1900, yearMax = 2020):
        return Date(randint(1, 28), randint(monthMin,monthMax), randint(yearMin, yearMax))

    def generate_after(self, months):
        m = self.month + months
        yIncr = 0
        if m > 12:
            m -= 12
            yIncr = 1
        return Date(randint(1, 28), m, self.year + yIncr)

    def cypher_string(self):
        return 'date("{:04d}-{:02d}-{:02d}")'.format(self.year, self.month, self.day)

    @staticmethod
    def distance(d1, d2):
        _d1 = date(d1.year, d1.month, d1.day)
        _d2 = date(d2.year, d2.month, d2.day)
        return (_d2 - _d1).days
    def within_two_weeks(self, _from):
        return Date.distance(self, _from) <= 14