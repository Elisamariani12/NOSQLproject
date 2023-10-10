import os
import pathlib

directory = pathlib.Path(__file__).parent.resolve()

fNameFile = None
lNameFile = None

if os.name == 'posix':
    fNameFile = open(f"{directory}/nomi.txt")
    lNameFile = open(f"{directory}/cognomi.txt")
else:
    fNameFile = open(f"{directory}/nomi.txt", encoding='UTF-8')
    lNameFile = open(f"{directory}/cognomi.txt",  encoding='UTF-8')

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
