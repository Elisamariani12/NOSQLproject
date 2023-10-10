import json

from utility import DBDataType, DBCollection
from person import *
from healthServices import *
from institution import *

class Certificate(DBDataType):
    def __init__(self, registry : PersonDetailed, emergencyContacts : list[PersonContact], vaccinations : list[Vaccination], tests : list[ViralTest]):
        self.registry = registry
        self.emergency_contacts = emergencyContacts
        self.vaccination_list = vaccinations
        self.tests = tests
    def toStringDict(self, generateId=False) -> str:
        if generateId:
            self._id = self.generateId()
        # Convert lists
        vl = list()
        for v in self.vaccination_list:
            vl.append(json.loads(v.toStringDict()))
        tl = list()
        for t in self.tests:
            tl.append(json.loads(t.toStringDict()))
        # dict fields
        d = self.__dict__.copy()
        d["registry"] = self.registry.__dict__
        d["emergency_contacts"] = [json.loads(ec.toStringDict()) for ec in self.emergency_contacts]
        d["vaccination_list"] = vl
        d["tests"] = tl
        return json.dumps(d)

class PopulationMedicalData(DBCollection):
    def __init__(self, population : Population, medical_institutions : HealthServiceHubs, maxVaccineDosesPerPerson = 2, maxTestsPerPerson = 5):
        self.certificates = []
        for person in population.detailedPeople:
            mh = MedicalHistory(person, medical_institutions, population.healthServiceOperators, maxVaccineDosesPerPerson, maxTestsPerPerson)
            ec = random.choices(population.emergencyContacts, k = random.randint(1,2))
            c = Certificate(person,ec,mh.vaccinations,mh.tests)
            self.certificates.append(c)
    def documents(self) -> list[DBDataType]:
        return self.certificates

class MedicalHistory:
    def __init__(self, registry : PersonDetailed, allInstitutions : HealthServiceHubs, allOperators : list[HealthServiceOperator], maxVaccineDoses : int = 2, maxTests : int = 5):
        self.vaccineHub = allInstitutions.randomInstitution()
        self.registry = registry
        self.vaccineDoses = Vaccination.randomDoseCount()
        self.testCount = random.randint(0, maxTests)
        self.healthServiceOperators = random.choices(allOperators, k = 2)
        self.vaccinations = self.generateVaccinations()
        self.tests = self.generateTests(allInstitutions)
    def generateVaccinations(self) -> list[Vaccination]:
        vaccinations = []
        firstDate = Date.generate_random(yearMin=2021, yearMax=2022)
        vaccineIndex = Vaccine.randomVaccineIndex()
        for i in range(self.vaccineDoses):
            dn = i + 1
            d = firstDate.generate_after(Vaccination.monthOffsetFromPreviousDose(dn))
            iid = self.vaccineHub.institution_id
            se = random.random() > 0.1
            v = Vaccine.random(index = vaccineIndex, subministrationDate=d)
            os = random.choices(self.healthServiceOperators, k = 2)
            vaccinations.append(Vaccination(v,dn,d,iid,se,os))
        return vaccinations
    def generateTests(self, allInstitutions : HealthServiceHubs) -> list[ViralTest]:
        tests = []
        firstDate = Date.generate_random(yearMin=2020, yearMax=2022)
        for x in range(self.testCount):
            i = allInstitutions.randomInstitution()
            d = firstDate.generate_after(x)
            vt = ViralTest.random(institution=i)
            tests.append(vt)
        return tests



# hsb1 = HealthServiceHubs(10)
# pop1 = Population(5,5,5)
# mh1 = MedicalHistory(pop1.detailedPeople[0], hsb1, pop1.healthServiceOperators)
# for v in mh1.vaccinations:
#     print()
#     print(v.toStringDict())
# for t in mh1.tests:
#     print()
#     print(t.toStringDict())