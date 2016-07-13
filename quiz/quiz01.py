def isPalindrome(aString):
    """
    :param aString: a string
    :return boolean: True if it is the same forwards and backwards
    """
    j = len(aString)
    for i in aString:
        j -= 1
        if i != aString[j]:
            return False


    return True


def dotProduct(listA, listB):
    """
    :param listA: list of numbers
    :param listB: list of numbers with same length as listA
    :return: pairwise product
    """
    result = 0
    for i in range(len(listA)):
        result += listA[i] * listB[i]
    return result
#
# listA = [1, 2, 3]
# listB = [4, 5, 6]
#
# print(dotProduct(listA, listB))


# def flatten(aList):
#     """
#     :param aList: a list
#     :return: a copy of aList, which is a flattened version of aList
#     # """
#     def flat(item):
#         if isinstance(item, list):
#             for elem in item:
#                 return flat(elem)
#         else:
#             return item
#
#     result = []
#     for item in aList:
#         if isinstance(item, list):
#             for elem in item:
#                 result.append(flat(elem))
#         else:
#             result.append(flat(item))
#     return result

#
# def flatten(aList):
#
#     return result
# #
# # aList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
# # print(flatten(aList))
result = []

# # solution found on stackoverflow
# def flatten(aList):
#     if aList == []:
#         return aList
#     if isinstance(aList[0], list):
#         return flatten(aList[0]) + flatten(aList[1:])
#     return aList[:1] + flatten(aList[1:])


#
# def flatten(aList):
#     if aList == []:
#         return aList
#     if isinstance(aList[0], list):
#         return flatten(aList[0]) + flatten(aList[1:])
#     else:
#         return aList[:1] + flatten(aList[1:])

# def flatten(aList):
#     if aList == []:
#         return aList
#     if isinstance(aList[0], list):
#         return flatten(aList[0]) + flatten(aList[1:])
#     else:
#         return aList[:1] + flatten(aList[1:])



# # practice
# def flatten(aList):
#     if aList == []:
#         return aList
#     if isinstance(aList[0], list):
#         return flatten(aList[0]) + flatten(aList[1:])
#     else:
#         return aList[:1] + flatten(aList[1:])

def flatten(aList):
    if aList == []:
        return aList
    elif isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    else:
        return aList[:1] + flatten(aList[1:])

# failed tests
test9 = [[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]]]
test10 = [[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]
print(flatten(test9))
print(flatten(test10))

# # TODO



# problem 7
#
# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
#
# def dict_interdiff(d1, d2):
#
#     inter = {}
#     diff = {}
#
#     for key in d1.keys():
#         if key in d2.keys():
#             inter[key] = f(d1[key], d2[key])
#         else:
#             diff[key] = d1[key]
#     for key in d2.keys():
#         if key not in d1.keys():
#             diff[key] = d2[key]
#
#
#     result = (inter, diff)
#     return result
#
# print(dict_interdiff(d1, d2))

#
# def satisfiesF(L):
#     """
#     Assumes L is a list of strings
#     Assume function f is already defined for you and it maps a string to a Boolean
#     Mutates L such that it contains all of the strings, s, originally in L such
#             that f(s) returns True, and no other elements. Remaining elements in L
#             should be in the same order.
#     Returns the length of L after mutation
#     """
#     print L
#     for elem in L:
#         if isinstance(elem, str):
#             if not f(elem):
#                 L.remove(elem)
#     return len(L)
#
#
#
#
# def f(s):
#     return 'a' in s
#
#
# # L = ['a', 'b', 'a', 'c']
# L = []
# L = ['abc', 'aaa', 'bbb']
# L = [1, 2, 3]
# print satisfiesF(L)
#
# print L

# run_satisfiesF(L, satisfiesF)

