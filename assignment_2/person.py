import resources.personNames as PersonNames
import random
from string import ascii_uppercase, digits

from utility import DBDataType
from date import Date
from fiscal_code import generate_fcode

class Person(DBDataType):
    def __init__(self, firstName : str, lastName: str):
        self.first_name = firstName
        self.last_name = lastName
    @classmethod
    def random(cls):
        fn = random.choice(PersonNames.firstNames)
        ln = random.choice(PersonNames.lastNames)
        return cls(fn, ln)


class PersonContact(Person):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str):
        super().__init__(firstName, lastName)
        self.phone_number = phoneNumber
    @classmethod
    def random(cls):
        p = Person.random()
        n = "+39 " + ''.join((random.choice(digits)) for x in range(10))
        return cls(p.first_name, p.last_name, n)

class PersonDetailed(PersonContact):
    def __init__(self, firstName: str, lastName: str, phoneNumber: str, birthday : Date):
        super().__init__(firstName, lastName, phoneNumber)
        self.birthday = birthday.mongoDBObject()
        self.gender = 'M' if firstName[-1] != 'a' else 'F'
        self.fiscal_code = generate_fcode(self, birthday)
    @classmethod
    def random(cls):
        pc = PersonContact.random()
        bd = Date.generate_random()
        return cls(pc.first_name, pc.last_name, pc.phone_number, bd)

class HealthServiceOperator(Person):
    def __init__(self, firstName: str, lastName: str, operatorId : str):
        super().__init__(firstName, lastName)
        self.operator_id = operatorId
    @classmethod
    def random(cls):
        p = Person.random()
        id = ''.join((random.choice(ascii_uppercase)) for x in range(3)) + ''.join((random.choice(digits)) for x in range(5))
        return cls(p.first_name, p.last_name, id)


class Population:
    def __init__(self, peopleCount : int = 100, contactCount : int = 100, operatorCount : int = 50):
        self.detailedPeople = [PersonDetailed.random() for _ in range(peopleCount)]
        self.emergencyContacts = [PersonContact.random() for _ in range(contactCount)]
        self.healthServiceOperators = [HealthServiceOperator.random() for _ in range(operatorCount)]
    