import random
import string
from date import Date
from fiscal_code import generate_fcode


class Person:
    def __init__(self, firstName, lastName):
        self.name = firstName + " " + lastName
        self.gender = "M" if firstName[-1] == "o" else ("F" if firstName[-1] == "a" else ("M" if random.randint(0,1) == 0 else "F"))
        self.cellphone = "+39 " + ''.join((random.choice("0123456789")) for x in range(10))
        self.bday = Date.generate_random()
        self.id = generate_fcode(self)

    def cypherCreate(self):
        # CREATE (ee:Person { name: "Emil", from: "Sweden", klout: 99 })
        return 'CREATE ({}:Person {{ name: "{}", gender: "{}", cellphone: "{}", birthday: {}, id: "{}" }} )'.format(self.id, self.name, self.gender, self.cellphone, self.bday.cypher_string(), self.id)