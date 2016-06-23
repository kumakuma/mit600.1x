# functions in python


def iterative_power(x, n):
    """
    :param x: int or float
    :param n: int or float - the power we want to raise x to
    :return: result of x ^ n
    """
    result = 1
    for i in range(n):
        result = result * x
        print('Iteration: ' + str(i + 1) + ' current result: ' + str(result))
    return result


def square(x):
    """
    :param x: int or float
    :return: the value of x squared
    """
    return x * x


def two_power(x, n):
    """
    :param x: int or float
    :param n: int or float - the power where n is a power of 2
    :return: the result of x ^ n
    """
    while n > 1:
        x = square(x)
        n = n/2
    return x

# L4 problem 5
def clip(lo, x, hi):
    """
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    """
    return min(max(lo, x), hi)


# bi-sectional root finder
def find_root(x, power, epsilon):
    """
    :param x: int or float
    :param power: int, >= 1
    :param epsilon: int or float > 0
    :return: float such that y**power is within epsilon of x
            if no such float exists it returns None
    """
    # can't find even powered root of negative number so avoid it
    if x < 0 and power % 2 ==0:
        return None
    low = min(-1, x)  # keeps correct min even if negative or fractional
    high = max(1, x)
    ans = (high + low) / 2.0
    while abs(ans ** power - x) > epsilon:
        if ans ** power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans


# ----- L4 P8 -----
#  fourth power
def fourth_power(x):
    """
    :param x: int or float
    :return: int or float - x raised to the fourth power
    """
    return square(square(x))


# ----- L4 P9 -----
def odd(x):
    """
    :param x: int or float
    :return: True if x is odd, False otherwise
    """
    return x % 2 != 0


# ----- L4 P10 -----
def is_vowel(char):
    """
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    """
    result = False
    vowels = 'aeiouAEIOU'
    x = 0
    while x < len(vowels):
        if char == vowels[x]:
            result = True
            break
        x += 1
    return result


#  ----- L4 P11 -----
def is_vowel_2(char):
    """
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    """
    # Your code here
    vowels = 'aeiouAEIOU'
    for v in vowels:
        if char == v:
            return True
    return False
