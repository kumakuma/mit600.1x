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

def FancyDivide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception, e:
        print e

FancyDivide([0,2,4], 0)