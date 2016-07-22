# filename:     lec11 - classes
# author:       dan.smith.me@gmail.com
# date:         22/07/2016
# version:      1.0
# =====================================================================================================================
import math


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def distance(self, other):
        return math.sqrt(pow((self.x - other.x), 2) + pow((self.y + other.y), 2))


london = Coordinate(51.5074, 0.1278)
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
# print london.x, origin.x
# print london
# print c.distance(origin)


# # L11 - problem 2
class Clock(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        time = '6:30'
        print self.time

# clock = Clock('5:30')
# clock.print_time(


class Clock2(object):
    def __init__(self, time):
        self.time = time

    def print_time(self, time):
        print time

# clock = Clock2('5:30')
# clock.print_time('10:30')


class Clock3(object):
    def __init__(self, time):
        self.time = time

    def print_time(self):
        print self.time


# boston_clock = Clock3('5:30')
# paris_clock = boston_clock
# paris_clock.time = '10:30'
# boston_clock.print_time()


# L11 problem 3
