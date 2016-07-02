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

# print(isPalindrome('Helen'))
# print(isPalindrome('Hannah'))
#
# print(isPalindrome('Able was I ere I saw Elba'))


# ----- L5 P6 ----- #
def lenIter(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''

    count = 0
    for c in aStr:
        count += 1

    return count

# print(lenIter('Daniel'))

# ----- L5 P7 ----- #
def lenRecur(aStr):
    """
    aStr: a string
    returns: int, the length of aStr
    """
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[0:-1])


# ----- L5 P8 ----- #
def isIn(char, aStr):
    """
    :param char: a single character
    :param aStr: an alphabetized string
    :return: True if char is in aStr; False otherwise
    """
    low = 0
    high = len(aStr)
    mid = (low + high) / 2

    if aStr == '':
        return False
    elif aStr[mid] == char:
        return True
    elif len(aStr) == 1:
        return aStr == char
    else:
        if char > aStr[mid]:
            low = mid
        else:
            high = mid
        return isIn(char, aStr[low:high])


# ----- L5 P9 ----- #
def semordnilapWrapper(str1, str2):
    # a single length string cannot be a semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)


def semordnilap(str1, str2):
    """
    :param str1: a string
    :param str2: a string
    :return:    True if str1 and str2 are semordnilap;
                False otherwise
    """
    if len(str1) != len(str2):
        return False
    # only need to check one string as both are same length
    elif len(str1) == 1:
        return str1 == str2

    elif str1[0] != str2[-1]:
            return False
    else:
        return semordnilap(str1[1:], str2[:-1])


print(semordnilapWrapper('palindromes', 'semordnilap'))
print(semordnilapWrapper('palindromes', ''))


# ----- global variables ----- #
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x - 1) + fibMetered(x - 2)

def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')


testFib(5)

