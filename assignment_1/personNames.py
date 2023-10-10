fNameFile = open("./resources/nomi.txt")
lNameFile = open("./resources/cognomi.txt")

firstNames = []
lastNames = []

for line in fNameFile:
    name = line.split()[0].replace("\n", "").capitalize()
    firstNames.append(name)
for line in lNameFile:
    name = line.split()[0].replace("\n", "").capitalize()
    lastNames.append(name)

fNameFile.close()
lNameFile.close()
