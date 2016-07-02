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

