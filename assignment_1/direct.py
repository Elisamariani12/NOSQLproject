import random
from date import Date
from timeh import Time

sistemi = ["Scuola", "Immuni", "Università", "CIA"]

# persona -> contatto diretto/esplicito (app/device/sistema) {data, ora} <- persona
class DirectContact:
    def __init__(self, p1, p2):
        self.person1 = p1
        self.person2 = p2
        self.date = Date.generate_random(yearMin=2020, yearMax=2021)
        self.time = Time.generate_random()
    def cypherCreateRelationship(self):
        cmd = "CREATE\n"
        cmd += "({0})-[:DIRECT_CONTACT{{ date: {1}, time: {2} }}]->({3})".format(self.person1.id, self.date.cypher_string(), self.time.cypher_string(), self.person2.id) + ",\n"
        cmd += "({3})-[:DIRECT_CONTACT{{ date: {1}, time: {2} }}]->({0})".format(self.person1.id, self.date.cypher_string(), self.time.cypher_string(), self.person2.id)
        return cmd
