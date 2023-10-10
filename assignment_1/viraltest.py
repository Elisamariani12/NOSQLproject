import random
import string

from date import Date

class ViralTest:
    def __init__(self, date, isPositive, person):
        self.date = date
        self.isPositive = isPositive
        self.person = person
        self.id = "VIRTEST" + "".join([random.choice(string.digits) for _ in range(3)]) + "".join([random.choice(string.ascii_uppercase) for _ in range(5)] )
    
    @staticmethod
    def generate_random(person, positiveRate = 0.013):
        return ViralTest(Date.generate_random(yearMin=2020, yearMax=2021), (random.random() <= positiveRate), person)

    def cypherCreate(self):
        cmd = "({}:ViralTest{{ date: {}, is_positive: {} }})".format(self.id, self.date.cypher_string(), str(self.isPositive).lower())
        return cmd

    def cypherCreateRelationship(self):
        cmd = "({})-[:TESTED]->({})".format(self.person.id, self.id)
        return cmd

# for _ in range(15):
#     d = Date.generate_random()
#     p = random.random() > 0.5
#     vt = ViralTest(d, p)
#     print(vt.cypherCreate())
