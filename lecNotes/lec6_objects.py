#
# -----MIT 6.00x - Lec6 notes -----
#
# by Dan Smith - 27/6/2016
# dan.smith.me@gmail.com
#

# ----- TUPLES ----- #

# t1 = (1, 'two', 3)
# print(t1)
#
# t2 = (t1, 'four')
# print(t2)
#
# # concatenation
# print(t1 + t2)
# # indexing
# print((t1 + t2)[3])
# # slicing
# print((t1 + t2)[2:5])
#
# print(len(t1))
# # singleton - needs comma to differentiate from regular ( )
# t3 = ('five',)


def findDivisors(n1, n2):
    """
    :param n1: positive int
    :param n2: positive int
    :return: tuple containing divisors of n1 and n2
    """
    divisors = ()  # empty tuple
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            divisors = divisors + (i,)
    return divisors


# divs = findDivisors(20, 100)
# print(divs)
# total = 0
# for d in divs:
#     total += d
# print(total)

# ----- L6 P2 ----- #
def oddTuples(aTup):
    """
    :param aTup: a tuple
    :return: tuple, every other element of aTup
    """
    result = ()
    for i in range(len(aTup)):

        if i % 2 == 0:
            result = result + (aTup[i], )
    return result

# print(oddTuples((3, )))
# print(oddTuples((18, 3, 4, 0, 2, 0, 3)))
# print(oddTuples(()))
# print(oddTuples((11, 18, 16, 9, 10, 13, 16, 8)))

# ----- LISTS ----- #
"""
lists are mutable
more flexible - BUT can lead to problems as flexible
"""
# alist = [1, 2, 3, 4]
# techs = ['MIT', 'Cal Tech']
# ivys = ['Harvard', 'Yale', 'Brown']
# techs.append('RPI')


def applyToEach(L, f):
    """
    :param L: is a List
    :param f: is a funtions
    :return: mulates L by replacing each element e, of L by f(e)
    """
#     for i in range(len(L)):
#         L[i] = f(L[i])
#
#
# L = [1, -2, 3.4]
# applyToEach(L, abs)
# print(L)
#
# applyToEach(L, int)
# print(L)

# applyToEach(L, fact)
# print(L)
#
# applyToEach(L, fib)
# print(L)

#
# def square(a):
#     return a * a
#
#
# def halve(a):
#     return a / 2
#
#
# def inc(a):
#     return a + 1
#
#
# def applyEachTo(L, x):
#     result = []
#     for i in range(len(L)):
#         result.append(L[i](x))
#     return result
#
# print(applyEachTo([inc, square, halve, abs], 3.0))


# #  ----- DICTIONARIES ----- #
# monthNumbers = {1: 'Jan', 2: 'Feb', 'Mar': 3, 'Feb': 2, 'Apr': 4, 'Jan': 1, 3: 'Mar'}
# print(monthNumbers)
# print(monthNumbers['Jan'])
#
# print(monthNumbers[3])


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(animals['d'])

def howMany(aDict):
    """
    :param aDict: A dictionary where all the values are lists
    :return: int, how many values there are in the dictionary
    """
    result = 0
    for k in aDict:
        result += len(aDict[k])
    return result

print(howMany(animals))

def biggest(aDict):
    """
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    """
    biggestValue = None
    result = None
    for k in aDict:
        if len(aDict[k]) > biggestValue:
            biggestValue = len(aDict[k])
            result = k
    return result


print(biggest({'b': []}))