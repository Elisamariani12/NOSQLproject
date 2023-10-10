import random
import resources.locationNames as LocationNames

from utility import DBDataType

class Location(DBDataType):
    def __init__(self, city : str, address:str, latitude : float, longitude : float):
        self.city = city
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
    @classmethod
    def random(cls):
        city = random.choice(LocationNames.cities)
        streetName = random.choice(LocationNames.addresses)
        streetNumber = random.randint(1, 80)
        lat = random.randint(-90, 90) + random.random()
        lon = random.randint(-180, 180) + random.random()
        return cls(city, f"{streetName}, {streetNumber}", lat, lon)
