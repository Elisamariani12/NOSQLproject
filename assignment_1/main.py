from population import Population
from city import City
from vaccine import allVaccines
import random

output_directory = "./output"
output_filename = "test_fiscal_code.txt"

# Population: People
population_family_count = 5
min_family_size = 3
max_family_size = 6
# Population: Direct Contacts
min_direct_contacts_per_person = 3
max_direct_contacts_per_person = 6
# Population: Tests
min_viral_tests_per_person = 0
max_viral_tests_per_person = 5
test_positive_rate = 0.5
# City
city_location_count = 10
min_visits_per_location = 10
max_visits_per_location = 20

random.seed(1)

# ACTUAL DATA
population = Population(population_family_count, min_family_size, max_family_size, 
                        min_direct_contacts_per_person, max_direct_contacts_per_person,
                        min_viral_tests_per_person, max_viral_tests_per_person, test_positive_rate)
city = City(city_location_count, population, min_visits_per_location, max_visits_per_location)

# CYPHER FILE GENERATION
f = open(output_directory + "/" + output_filename, "w")

pf = population.cypherCreateFamilies()
pv = population.cypherCreateVaccinations()
pdc = population.cypherCreateDirectContacts()
pvt = population.cypherCreateTests()
cl = city.cypherCreateLocations()
clv = city.cypherCreateVisits()

# Write population to file
f.write(pf + "\n")

# Write direct contacts
f.write(pdc + "\n")

# Write vaccines to file
f.write("// Vaccines\n")
for k, v in allVaccines.items():
    f.write(v.cypherCreate() + "\n")

# Write vaccinations to file
f.write("\n" + pv + "\n")

# Write viral tests to file
f.write(pvt + "\n")

# Write city locations to file
f.write(cl + "\n")

# Write city location visits to file
f.write(clv + "\n")

f.close()



