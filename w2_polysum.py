# Complete Programming Experience:
#
# POLYSUM

import math


def polysum(n, s):
    """
    :param n: number of sides
    :param s: int or float length of each side
    :return: the sum of the area of the polygon and its perimeter squared
    """
    perim = n * s
    area = (0.25 * n * s ** 2) / math.tan(math.pi/n)

    return round((area + perim ** 2), 4)


print(polysum(4, 4))