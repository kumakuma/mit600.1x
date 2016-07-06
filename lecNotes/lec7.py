# ----- lecture 7 notes ----- #

def isBigger(x, y):
    """
    :param x: int
    :param y: int
    :return: True if x less than y, False otherwise
    Input space is all pairs of integers
    Possible partitions: x positive, y positive
                         x negative, y negative
                         x positive, y negative
                         x negative, y positive
                         x = 0, y positive
                         x = 0, y negative
                         y = 0, x positive
                         y = 0, x negative
                         x = 0, y = 0
    """
    return x > y


# black box

def sqrt(x, eps):
    """
    :param x: float >= 0
    :param eps: float > 0
    :return: returns res such that
                x-eps <= res*res <= x+eps

    Paths through the specification:
                check that x & y >
    """

# glass box
def abs(x):
    """
    :param x: int
    :return: x if x >= 0, -x otherwise
    """
    if x < -1:
        return - x
    else:
        return x

#  test suite
# {-2, 2}
# abs(-1) # identifies the bug in the code


# ----- L7 P3 ----- #
def max_of_three(a, b, c):
    """
    :param a: number
    :param b: number
    :param c: number
    :return: maximum of a, b, and c
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger

# Path complete test suite
# max_of_three(2, -10, 100)
# max_of_three(7, 9, 10)
# max_of_three(6, 1, 5)
# max_of_three(0, 40, 20)


# ----- L7 P4 ----- #
def union(set1, set2):
    """
    :param set1: collection of objects, possibly empty
    :param set2: collection of objects, possibly empty
    each set has no duplicates within itself, but there may be objects that are in both sets
    objects are assumed to be the same type

    :return: one set containing all elements from both sets, but with no duplicates
    """
    if len(set1) == 0:
        return set2
    elif set1[0] in set2:
        return union(set1[1:], set2)
    else:
        return set1[0] + union(set1[1:], set2)

#  path compete glass box test suite
# union('', 'abc')
# union('a', 'abc')
# union('ab', 'abc')
# union('d', 'abc')


# ----- L7 P5 ----- #
def foo(x, a):
    """
    :param x: a positive integer
    :param a: a positive integer
    :return: an integer
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

#  path complete glass box test suite
foo(10,3)
foo(1, 4)
foo(10, 6)

# aliasing bug
# x = [1, 2, 3]
#  temp = x (aliasing)
temp = x[:] # makes a copy
