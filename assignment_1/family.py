import random
from person import Person

from personNames import firstNames, lastNames

class Family:

    def __init__(self, lastName, size):
        self.name = lastName
        self.size = size
        self.members = [Person(random.choice(firstNames), lastName) for x in range(size)]

    def cypherCreateMembers(self):
        cmd = ""
        for m in self.members:
            cmd = cmd + m.cypherCreate() + "\n"
        cmd = "// " + self.name + " family members\n" + cmd
        return cmd

    # CREATE (a)-[r:KNOWS {since: 2015}]->(b), (a)-[h:BEFRIEND]->(b)
    def cypherGenerateRelationship(self):
        if self.size < 2:
            return ""
        cmd = "CREATE\n"
        for i, m1 in enumerate(self.members):
            for x in range(self.size):
                if x == i: continue
                m2 = self.members[x]
                # cmd = cmd + 'MATCH (a:Person), (b:Person) WHERE a.id = "{}" AND b.id = "{}" CREATE (a)-[r:LIVES_TOGETHER]->(b)'.format(m1.id, m2.id) + "\n"
                cmd = cmd + "({})-[:LIVES_TOGETHER]->({}),\n".format(m1.id, m2.id)
        cmd = "// " + self.name + " family relationships\n" + cmd
        return cmd[:-2] + "\n"

    
# lastName = random.choice(lastNames)
# f = Family(lastName, 5)
# print(f.cypherCreateMembers())
# print(f.cypherGenerateRelationship())