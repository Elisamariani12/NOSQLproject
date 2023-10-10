import random

from date import Date

vaccineNames = ["Pfizer", "Moderna", "AstraZeneca", "JohnsonAndJohnson"]
vaccineDistr = [ 0.720, 0.130, 0.125, 0.025 ]

# vaccinationDistr = [0.2133, 0.0315, 0.7552]
vaccinationDistr = [0.20, 0.20, 0.60]

class Vaccine:
    def __init__(self, name):
        self.name = name
        self.id = ("VAX" + self.name).upper()
    def cypherCreate(self):
        cmd = 'CREATE ({}:Vaccine{{ name: "{}"}})'.format(self.id, self.name)
        return cmd

allVaccines = {}
for vn in vaccineNames:
    v = Vaccine(vn)
    allVaccines[vn] = v


class Vaccination:
    def __init__(self, person, vaccine, shots):
        self.person = person
        self.vaccine = vaccine
        self.shots = 1 if vaccine.name == vaccineNames[3] else shots
        self.date1 = Date.generate_random(monthMin=3, monthMax=9, yearMin = 2021, yearMax=2021)
        self.date2 = self.date1.generate_after(3)
    def cypherCreateRelationship(self):
        # TODO Add hub if REALLY needed
        cmd = ""
        if self.shots > 0:
            # CREATE (a)-[r:RELTYPE {name: a.name + '<->' + b.name}]->(b)
            cmd = cmd + "({})-[:VACCINATION{{ date: {}, shot: {} }}]->({})".format(self.person.id, self.date1.cypher_string(), 1, self.vaccine.id)
        if self.shots > 1:
            cmd = cmd + ",\n" + "({})-[:VACCINATION{{ date: {}, shot: {} }}]->({})".format(self.person.id, self.date2.cypher_string(), 2, self.vaccine.id)
        return cmd
