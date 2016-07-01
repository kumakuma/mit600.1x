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


# ----- L5 P4 ----- #
def gcdIter(a, b):
    """
    :param a: positive integer
    :param b: positive integer
    :return: a positive integer, the greatest common divisor
    """
    result = a
    while True:
        if a % result == 0 and b % result == 0:
            return result
        else:
            result -= 1
            if result == 1:
                return result


# ----- L5 P5 ----- #
def gcdRecur(a, b):
    """
    :param a: positive integer
    :param b: positive integer
    :return: a positive integer, the greatest common divisor
    """
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
#
# # test cases
# print(gcdIter(2,12))
# print(gcdIter(6,12))
# print(gcdIter(9,12))
# print(gcdIter(17,12))
#
# print('-'*10)
#
# print(gcdRecur(2,12))
# print(gcdRecur(6,12))
# print(gcdRecur(9,12))
# print(gcdRecur(17,12))

# ----- END ----- #

# Towers of Hanoi
def print_move(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))


def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        towers(n - 1, fr, spare, to)
        towers(1, fr, to, spare)
        towers(n - 1, spare, to, fr)

# ----- Fibonacci ----- #
def fibonacci(x):
    """
    :param x: int > 0
    :return: fibonacci of x
    """
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

# ----- End ----- #

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

print(isPalindrome('Helen'))
print(isPalindrome('Hannah'))

print(isPalindrome('Able was I ere I saw Elba'))