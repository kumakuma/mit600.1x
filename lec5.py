# - Lecture 5 notes - 01/07/2016

# ----- RECURSION ----- #
# L5 P1 - iterative power

def iterPower(base, exp):
    """
    :param base: int or float
    :param exp: int >= 0
    :return: int or float to equal base^exp
    """
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1

    return result
# ----- end -----#

def rec_mul(a, b):
    """
    :param a: int or float
    :param b: int or float
    :return: int or float equal to a * b
    """
    if b == 1:
        return a
    else:
        return a + rec_mul(a, b-1)


def fact(n):
    """
    :param n: int > 0
    :return: int n!
    """
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def fact_rec(n):
    """
    :param n: int > 0
    :return: int n!
    """
    if n == 1:
        return n
    else:
        return n * fact_rec(n - 1)

# ----- L5 P2 ------ #
def recurPower(base, exp):
    """
    :param base: int or float
    :param exp: int >= 0
    :return: int or float, base^exp
    """
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

# # test cases
# print(recurPower(3, 3))
# print(recurPower(3, 1))
# print(recurPower(3, 0))
# print(recurPower(4, 2))


def recurPowerNew(base, exp):
    """
    :param base: int or float
    :param exp: int >= 0
    :return: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        return recurPowerNew(base * base, exp/2)
    else:
        return base * recurPowerNew(base, exp - 1)

# # # test cases
# print(recurPowerNew(3, 0))
# print(recurPowerNew(3, 1))
# print(recurPowerNew(3, 3))
# print(recurPowerNew(-6, 6))
# print('*' * 6)
#
# print(recurPower(3, 0))
# print(recurPower(3, 1))
# print(recurPower(3, 3))
# print(recurPower(-6, 6))