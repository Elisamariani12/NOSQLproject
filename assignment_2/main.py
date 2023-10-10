from certificate import *
from person import *
from healthServices import *
from utility import *

# population = Population(peopleCount=100, contactCount=100, operatorCount=50)
# healthServiceHubs = HealthServiceHubs(hubCount=35)
# populationMedicalData = PopulationMedicalData(population, healthServiceHubs,
#                             maxVaccineDosesPerPerson=2, maxTestsPerPerson= 5)

# DBJsonWriter.collectionToFile("medical_institutions.json", healthServiceHubs, "datasets/")
# DBJsonWriter.collectionToFile("certificates.json", populationMedicalData, "datasets/")

population = Population(peopleCount=600, contactCount=300, operatorCount=100)
healthServiceHubs = HealthServiceHubs(hubCount=80)
populationMedicalData = PopulationMedicalData(population, healthServiceHubs,
                            maxVaccineDosesPerPerson=2, maxTestsPerPerson= 10)

DBJsonWriter.collectionToFile("medical_institutions_larger.json", healthServiceHubs, "datasets/")
DBJsonWriter.collectionToFile("certificates_larger.json", populationMedicalData, "datasets/")