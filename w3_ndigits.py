def ndigits(x):
    """
    returns the number of digits in x
    :param x: int either positive or negative
    :return: the number of digits in x
    """
    # get the absolute value of x
    x = abs(x)

    #  set base case and check the value of x
    if x / 10 == 0:
        result = 1
    else:
        # reduce the problem each time and recursively call ndigits
        result = 1 + ndigits(x / 10)

    # return the result
    return result


