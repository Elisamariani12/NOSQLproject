import json
import random
from types import ClassMethodDescriptorType
from string import *

from utility import DBDataType
from date import Date
from person import HealthServiceOperator, Person, PersonDetailed
from institution import Institution

class ViralTest(DBDataType):
    def __init__(self, date : Date, result : bool, operator : HealthServiceOperator, institutionId : str):
        self.date = date.mongoDBObject()
        self.result = 1 if result else 0
        self.operator = operator
        self.institution_id = institutionId
    def toStringDict(self, generateId=False) -> str:
        if generateId:
            self._id = self.generateId()
        d = self.__dict__.copy()
        d["operator"] = self.operator.__dict__
        return json.dumps(d)
    @classmethod
    def random(cls, date : Date = None, institution : Institution = None):
        d = Date.generate_random(yearMin=2020, yearMax=2022) if date == None else date
        r = random.random() > 0.5
        o = HealthServiceOperator.random()
        i = Institution.random().institution_id if institution == None else institution.institution_id
        return cls(d, r, o, i)

class Vaccine(DBDataType):
    
    brands = ["Pfizer", "Moderna", "AstraZeneca", "JohnsonAndJohnson"]
    types = ["mRNA", "mRNA", "adenovirus_vector", "recombinant_adenovirus_vector"]
    brandDistribution = [ 0.720, 0.130, 0.125, 0.025 ]

    def __init__(self, brand : str, type : str, lot : str, vialId : str, productionDate : Date):
        self.brand = brand
        self.type = type
        self.lot = lot
        self.vial_id = vialId
        self.production_date = productionDate.mongoDBObject()
    @classmethod
    def random(cls, index : int = -1, subministrationDate : Date = None):
        i = Vaccine.randomVaccineIndex() if index < 0 else index
        b = cls.brands[i]
        t = cls.types[i]
        l = "".join(random.choices(ascii_uppercase, k=3)) + "".join(random.choices(digits, k=4))
        v = "".join(random.choices(digits, k=9))
        d = Date.generate_random() if subministrationDate == None else subministrationDate.generate_before()
        return cls(b, t, l, v, d)
    @staticmethod
    def randomVaccineIndex() -> int:
        return random.choices([0,1,2,3], weights=Vaccine.brandDistribution, k = 1)[0]

class Vaccination(DBDataType):

    doseDistribution = [0.15, 0.20, 0.60, 0.05]

    def __init__(self, vaccine : Vaccine, doseNumber : int, date: Date, institutionId : str, sideEffects : bool, operators : list[HealthServiceOperator]):
        self.vaccine = vaccine
        self.date = date.mongoDBObject()
        self.side_effects = 1 if sideEffects else 0
        self.dose_number = doseNumber
        self.institution_id = institutionId
        self.operators = operators
    def toStringDict(self, generateId=False) -> str:
        if generateId:
            self._id = self.generateId()
        # Convert list
        ol = list()
        for o in self.operators:
            ol.append(o.__dict__)
        d = self.__dict__.copy()
        d["vaccine"] = self.vaccine.__dict__
        d["operators"] = ol
        return json.dumps(d)
    @staticmethod
    def monthOffsetFromPreviousDose(dose : int) -> int:
        if dose == 1:
            return 0
        elif dose == 2:
            return 1
        elif dose == 3:
            return 9
        else:
            return 12
    @staticmethod
    def randomDoseCount() -> int:
        return random.choices([0,1,2,3], weights=Vaccination.doseDistribution, k=1)[0]