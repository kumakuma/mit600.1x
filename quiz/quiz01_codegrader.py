# filename:     quiz01_codegrader
# author:       dan.smith.me@gmail.com
# date:         23/07/2016
# version:      1.0
# =====================================================================================================================

def flatten(aList):
    """
    aList: a list
    return: a copy of aList, which is a flattened version of aList
    """
    if aList == []:
        return aList
    elif isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    else:
        return aList[:1] + flatten(aList[1:])

# print(flatten([[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]))


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    # Your function implementation here
    listCopy = L[:]
    for i in listCopy:
        if not f(i):
            L.remove(i)
    return len(L)

# run_satisfiesF(L, satisfiesF)

# testing
def f(s):
    return 'a' in s

L = ['a', 'b', 'a']
print satisfiesF(L)
print L