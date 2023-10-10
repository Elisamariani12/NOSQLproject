import random

from personNames import lastNames
from family import Family
from vaccine import *
from direct import *
from viraltest import ViralTest

class Population:

    def __init__(self, famCount, famSizeMin = 3, famSizeMax = 3, minDirConPerPerson = 3, maxDirContPerPerson = 6, min_tests_per_person = 0, max_tests_per_person = 5, positiveTestRate = 0.013):
        # self.families = {}
        self.familyCount = famCount
        self.families = []
        self.vaccinations = []
        self.directContacts = []
        self.tests = []
        for _ in range(famCount):
            lName = random.choice(lastNames)
            fSize = random.randint(famSizeMin, famSizeMax)
            f = Family(lName, fSize)
            # self.families[f.name] = f
            self.families.append(f)
        for f in self.families:
            for m in f.members:
                # Vaccinate person
                vn = random.choices(vaccineNames, vaccineDistr)[0]
                v = allVaccines[vn]
                shots = random.choices([0,1,2], vaccinationDistr)[0]
                vax = Vaccination(m, v, shots)
                self.vaccinations.append(vax)
                # Report direct contact for m
                dcCount = random.randint(minDirConPerPerson, maxDirContPerPerson)
                counter = 0
                while counter < dcCount:
                    rf = random.choice(self.families)
                    rm = random.choice(rf.members)
                    if rm == m: continue
                    dc = DirectContact(m, rm)
                    self.directContacts.append(dc)
                    counter += 1
                # Generate
                tCount = random.randint(min_tests_per_person, max_tests_per_person)
                for _ in range(tCount):
                    t = ViralTest.generate_random(m, positiveTestRate)
                    self.tests.append(t)


    def cypherCreateFamilies(self):
        cmd = ""
        # for _, v in self.families.items():
        #     cmd = cmd + v.cypherCreateMembers() + v.cypherGenerateRelationship()
        for f in self.families:
            cmd = cmd + f.cypherCreateMembers() + f.cypherGenerateRelationship()
        cmd = "// Population\n\n" + cmd
        return cmd
    
    def cypherCreateVaccinations(self):
        cmd = "CREATE\n"
        for v in self.vaccinations:
            if v.shots < 1: continue
            cmd = cmd + v.cypherCreateRelationship() +",\n"
        cmd = "// Population vaccinations\n" + cmd
        return cmd[:-2] + "\n"

    def cypherCreateDirectContacts(self):
        cmd = ""
        for dc in self.directContacts:
            cmd = cmd + dc.cypherCreateRelationship() + "\n"
        cmd = "// Reported direct contacts\n" + cmd
        return cmd

    def cypherCreateTests(self):
        cmd = ""
        for t in self.tests:
            cmd += "CREATE\n"
            cmd += t.cypherCreate() + ",\n"
            cmd += t.cypherCreateRelationship() + "\n"
        cmd = "// Viral tests\n" + cmd
        return cmd




    

# p = Population(10,famSizeMin=1, famSizeMax=5)
# print(p.cypherCreateFamilies())