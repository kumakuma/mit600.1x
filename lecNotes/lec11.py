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


# L11 problem 4
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    # - write __eq__ and __repr__
    def __eq__(self, other):
        return (self.getX() == other.getX()) and (self.getY() == other.getY())

    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.getY()) + ')'


# Example set of integers
class IntSet(object):
    """
    An IntSet is a set of integers
    The value is represented by a list of ints. self.vals.
    Each Int in the set occurs in set.vals exactly once.
    """

    def __init__(self):
        """ Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '(' + ','.join([str(e) for e in self.vals]) + ')'

    def member(self, e):
        """Assumes e is an integer
        returns True if e is in self, False otherwise"""
        return e in self.vals

    def remove(self, e):
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        """Assumes other is an IntSet.
        Returns a new IntSet containing elements that appear in both sets."""
        result = IntSet()
        for e in self.vals:
            if other.member(e):
                result.insert(e)
        return result

    def __len__(self):
        :return:
        """Returns the length of the set.
        This method is called by the 'len' built in function"""
        return len(self.vals)


# L11 - Problem 6
class Queue(object):

    def __init__(self):
        """Create an empty list for elements"""
        self.elements = []

    def insert(self, element):
        """Adds element to the list of elements"""
        self.elements.append(element)


    def remove(self):
        """Removes the first item from elements,
        Raises ValueError if no items left"""
        try:
            return self.elements.pop(0)
        except:
            raise ValueError()
