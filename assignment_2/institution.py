import random
import json

from utility import DBCollection, DBDataType
from location import Location
from person import Person
import resources.locationNames as LocationNames
import resources.personNames as PersonNames

class Institution(DBDataType):
    def __init__(self, name : str, location : Location, entityType : str, supervisor : Person, vaccineIssuingDepartment : str):
        self.name = name
        self.location = location
        self.entity_type = entityType
        self.supervisor = supervisor
        self.vaccine_issuing_department = vaccineIssuingDepartment
        self.institution_id = name.replace(" ", "") + "".join(random.choice("1234567890") for _ in range(5))
    @classmethod
    def random(cls, supervisor : Person = None, vaccineIssuingDepartment : str = "Dipartimento Sanitario"):
        l = Location.random()
        et = random.choice(LocationNames.institutionTypes)
        n = f"{random.choice(PersonNames.firstNames)} {random.choice(PersonNames.lastNames)}"
        if supervisor == None:
            supervisor = Person.random()
        return cls(f"{et} {n}", l, et, supervisor, vaccineIssuingDepartment)
    def toStringDict(self, generateId=False) -> str:
        if generateId:
            self._id = self.generateId()
        d = self.__dict__.copy()
        d["supervisor"] = self.supervisor.__dict__
        d["location"] = self.location.__dict__
        return json.dumps(d)

# i1 = Institution.random()
# i2 = Institution.random()

# print(i1.toStringDict())
# print(i2.toStringDict())

class HealthServiceHubs(DBCollection):

    def __init__(self, hubCount = 10):
        self.hubs = [Institution.random() for _ in range(hubCount)]
    def documents(self) -> list[DBDataType]:
        return self.hubs
    def randomInstitution(self) -> Institution:
        return random.choice(self.hubs)
