from random import randint
from datetime import date
import json

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.year = year
        self.month = month

    def __str__(self):
        return "{:02d}/{:02d}/{:04d}".format(self.day, self.month, self.year)

    def toJSON(self):
        return json.dumps(self, default=lambda o: f"ISODate('{o.isoString()}')")

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

    def generate_before(self, monthMin = 1, yearMin = 2020):
        maxMonth = self.month - 1 if self.month > 1 else 12
        maxYear = self.year if self.month > 1 else self.year - 1
        return Date.generate_random(monthMax=maxMonth, yearMax=maxYear, monthMin=monthMin, yearMin=yearMin)

    def cypher_string(self):
        return 'date("{:04d}-{:02d}-{:02d}")'.format(self.year, self.month, self.day)

    @staticmethod
    def distance(d1, d2):
        _d1 = date(d1.year, d1.month, d1.day)
        _d2 = date(d2.year, d2.month, d2.day)
        return (_d2 - _d1).days
    def within_two_weeks(self, _from):
        return Date.distance(self, _from) <= 14

    def isoString(self) -> str:
        d = date(self.year, self.month, self.day)
        iso = d.isoformat()
        # return f"ISODate('{iso}')"
        return iso
    
    def mongoDBObject(self) -> dict:
        return {"$date":"{:04d}-{:02d}-{:02d}T00:00:00.000Z".format(self.year, self.month, self.day)}