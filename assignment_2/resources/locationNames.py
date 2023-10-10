import os
import pathlib

directory = pathlib.Path(__file__).parent.resolve()

institutionsFile = None
addressFile = None
cityFile = None

if os.name == 'posix':
    institutionsFile = open(f"{directory}/tipi_istituzioni.txt")
    addressFile = open(f"{directory}/indirizzi.txt")
    cityFile = open(f"{directory}/citta.txt")
else:
    institutionsFile = open(f"{directory}/tipi_istituzioni.txt", encoding='UTF-8')
    addressFile = open(f"{directory}/indirizzi.txt", encoding='UTF-8')
    cityFile = open(f"{directory}/citta.txt", encoding='UTF-8')

addresses = []
institutionTypes = []
cities = []

for line in addressFile:
    name = line.replace("\n", "")
    addresses.append(name)
for line in institutionsFile:
    name = line.replace("\n", "")
    institutionTypes.append(name)
for line in cityFile:
    name = line.replace("\n","")
    cities.append(name)

addressFile.close()
institutionsFile.close()
cityFile.close()



