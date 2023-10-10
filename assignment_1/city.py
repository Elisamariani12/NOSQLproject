import random
import string

import personNames
from location import *
from person import Person
from population import Population


class City:
    def __init__(self, locationCount, population, minVisPerLoc = 2, maxVisPerLoc = 4):
        self.locationCount = locationCount
        self.population = population
        self.locations = []
        self.visits = []
        for _ in range(locationCount):
            # Generate Location
            lIndex = random.randrange(locationTypeCount)
            lType = locTypes[lIndex]
            lStay = locStayTimes[lIndex]
            lName = random.choice(personNames.lastNames)
            lAddr = random.choice(addresses)
            l = Location(lName, lType, lStay, lAddr)
            self.locations.append(l)
            # Generate Visits per Location
            visitCount = random.randint(minVisPerLoc, maxVisPerLoc)
            for __ in range(visitCount):
                fIndex = random.randrange(0, self.population.familyCount)
                f = self.population.families[fIndex]
                mIndex = random.randrange(0, f.size)
                m = f.members[mIndex]
                # Get positive test dates
                ptDates = [ t.date for t in self.population.tests if (t.isPositive and t.person.id == m.id) ]
                visit = LocationVisit(m, l)
                
                # Only add not quarantined visits
                valid = True
                for d in ptDates:
                    if visit.date.within_two_weeks(d):
                        print("AAA")
                        valid = False
                        break
                if valid:
                    print("BBB")
                    self.visits.append(visit)



    
    def cypherCreateLocations(self):
        cmd = ""
        for l in self.locations:
            cmd = cmd + l.cypherCreate() + "\n"
        cmd = "// City locations\n" + cmd
        return cmd

    def cypherCreateVisits(self):
        cmd = ""
        for v in self.visits:
            cmd = cmd + v.cypherCreate() + "\n"
        cmd = "// Visits to the city's locations\n" + cmd
        return cmd


# pop = Population(5, 3, 6)
# c = City(10, pop)

# f = open("cypherCode2.txt", "w")
# pf = pop.cypherCreateFamilies()
# cl = c.cypherCreateLocations()
# clv = c.cypherCreateVisits()
# f.write(pf + "\n")
# f.write(cl + "\n")
# f.write(clv + "\n")
# f.close()



