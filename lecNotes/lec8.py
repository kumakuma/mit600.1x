# ----- L8 notes ----- #
#
# try:
#     f = open('grades.txt')
#     # ... code to read and process grades
#
# except IOError, e:
#     print("Can't open grades file: " + str(e))
#     sys.exit(0)
#
# except ArithmeticError, e:
#     raise ValueError("Bug in grades calculation " + str(e))
#
# else:
#     # when try completes without exceptions
#
# finally:
#     # executed after try, else and except
#     # useful for clean up code that should always be run


def divide(x, y):
    try:
        result = x / y

    except ZeroDivisionError, e:
        print("division by zero! " + str(e))

    except TypeError:
        divide(int(x), int(y))

    else:
        print("result is ", result)

    finally:
        print("executing finally clause")


# divide('3', '4')


# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#
#     except IndexError, e:
#         print("-1")
#
#     else:
#         print("1")
#
#     finally:
#         print("0")


# def FancyDivide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError, e:
#         FancyDivide(numbers, len(numbers) - 1)
#     except ZeroDivisionError, e:
#         print "-2"
#     else:
#         print "1"
#     finally:
#         print "0"


# def FancyDivide(numbers, index):
#     try:
#         try:
#             denom = numbers[index]
#             for i in range(len(numbers)):
#                 numbers[i] /= denom
#         except IndexError, e:
#             FancyDivide(numbers, len(numbers) - 1)
#         else:
#             print "1"
#         finally:
#             print "0"
#     except ZeroDivisionError, e:
#         print "-2"

# def FancyDivide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception, e:
#         print e

# def FancyDivide(list_of_numbers, index):
#     try:
#         try:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#         finally:
#             raise Exception("0")
#     except Exception, e:
#         print e
#
# FancyDivide([0,2,4], 0)

# ----- error handling example ----- #
def getSubjectStats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)] for elt in subject]


def dotProcuct(a, b):
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def avg(grades, weights):
    try:
        return dotProcuct(grades, weights) / len(grades)
    except ZeroDivisionError:
        print("No grades")
        return 0.0


# ----- Exceptions as control flow -----#
def getRatios(v1, v2):
    """
    :param v1: list of numbers
    :param v2: list of numbers
    both v1 & v2 are of equal length
    :return: a list containing meaningful values of v1[i] / v2[i]
    """
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index] / float(v2[index]))
        except ZeroDivisionError:
            ratios.append(float("NaN")) # NaN = Not a Number
        except:
            raise ValueError("getRatios called with bad arg")
    return ratios


# ----- Assertions ----- #
def avg(grades, weights):
    assert not len(grades) == 0, "no grades data"
    assert len(grades) == len(weights), "wrong number of grades"

    newgr = [convertLetterGrade(elt) for elt in grades]
    result = dotProduct(newgr, weights) / len(newgr)
    assert 0.0 <= result <= 100.0
    return result


