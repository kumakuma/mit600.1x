# functions in python


def iterative_power(x, p):
    """
    :param x: int or float
    :param p: int or float - the power we want to raise x to
    :return: result of x ^ p
    """
    result = 1
    for i in range(p):
        result = result * x
        print('Iteration: ' + str(i + 1) + ' current result: ' + str(result))
    return result


def square(x):
    """
    :param x: int or float
    :return: the value of x squared
    """
    return x * x


def evalQuadratic(a, b, c, x):
    """
    :param a, b, c: numerical values for the coefficients of a quadratic equation
    :param x: numerical value at which to evaluate the quadratic
    :return: the value of the quadratic
    """

    value = (a * x*x) + (b * x) + c

    return value
