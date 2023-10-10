import random
import string

import personNames
from date import Date
from timeh import Time
from person import Person
from population import Population

addressFile = open("./resources/indirizzi.txt")
locationTypesFile = open("./resources/tipi_luoghi.txt")

addresses = []
locTypes = []
locStayTimes = []
locationTypeCount = 0

for line in addressFile:
    name = line.replace("\n", "")
    addresses.append(name)
for line in locationTypesFile:
    line = line.replace("\n", "")
    name = line.split()[0].capitalize()
    time = float(line.split()[1])
    locTypes.append(name)
    locStayTimes.append(time)

locationTypeCount = len(locTypes)

addressFile.close()
locationTypesFile.close()

# print("---------------\n")
# print(addresses)
# print("---------------\n")

# for x in range(locationTypeCount):
#     print("Durata media della rimanenza in", locTypes[x], ":", locStayTimes[x],"ore")
# print("---------------\n")

class Location:
    def __init__(self, name, _type, stay, addr):
        self.name = _type + " " + name 
        self._type = _type
        self.stayTime = int(stay * 60)
        self.address = addr + ", " + str(random.randint(1,99))
        self.id = (name[:3] + _type[:3] + self.address.replace(", ", "")[-5:] + "".join(random.choice(string.ascii_uppercase) for _ in range(5))).upper().replace(" ", random.choice(string.ascii_uppercase))
    def cypherCreate(self):
        # CREATE (ee:Person { name: "Emil", from: "Sweden", klout: 99 })
        return 'CREATE ({}:Location {{ name: "{}", stay_time: {}, address: "{}", id: "{}" }} )'.format(self.id, self.name, self.stayTime, self.address, self.id)

# import personNames
# for x in range(10):
#     l = Location(personNames.lastNames[x], locTypes[x], locStayTimes[x], addresses[x])
#     print(l.cypherCreate())

class LocationVisit:
    def __init__(self, person, location):
        self.person = person
        self.location = location
        self.date = Date.generate_random(yearMin=2020, yearMax=2021)
        self.time = Time.generate_random('any')
    def cypherCreate(self):
        # CREATE (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix)
        # CREATE (a)-[r:RELTYPE {name: a.name + '<->' + b.name}]->(b)
        return 'CREATE ({})-[:VISITED {{date: {}, time: {} }}]->({})'.format(self.person.id, self.date.cypher_string(), self.time.cypher_string(), self.location.id)

# pop = Population(3)
# loc = Location("Oldani", "Pizzeria", 2.5, "Via Marconi")
# per = pop.families[0].members[0]
# lv = LocationVisit(per, loc)
# print(lv.cypherCreate())


