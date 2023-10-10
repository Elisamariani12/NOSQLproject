from random import randint

class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    @staticmethod
    def generate_random(time_of_day = 'any'):
        if time_of_day == 'morning':
            return Time(randint(7, 13), randint(0, 59))
        elif time_of_day == 'night':
            return Time(randint(20, 23), randint(0, 59))
        elif time_of_day == 'aftenoon':
            return Time(randint(13, 20), randint(0, 59))
        else:
            return Time(randint(0, 23), randint(0, 59))

    def cypher_string(self):
        return 'time("{:02d}:{:02d}")'.format(self.hour, self.minute)