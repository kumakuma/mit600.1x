# filename:     exam_coding
# author:       dan.smith.me@gmail.com
# date:         06/08/2016
# version:      1.0
# =====================================================================================================================


# Problem 3
def dict_invert(d):
    flipped = {}

    for key in d:
        if d[key] in flipped:
            flipped[d[key]].append(key)
            flipped[d[key]].sort()
        else:
            flipped[d[key]] = [key]

    return flipped

d = {1: 10, 2: 20, 3: 30}
e = {1: 10, 2: 20, 3: 30, 4: 30}
f = {4: True, 2: True, 0: True}

# print(dict_invert(d))
# print(dict_invert(e))
# print(dict_invert(f))
# print(dict_invert({8: 6, 2: 6, 4: 6, 6: 6}))


# problem 4 - get sublists
def getSublists(L, n):
    if len(L) == n:
        return [L]
    else:
        return getSublists(L[:n], n) + getSublists(L[1:], n)

# L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
# n = 4
# print(getSublists(L, n))


# problem 5 - longest runs
def longestRun(L):
    longest = 0

    def testRun(list):
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                return False
        return True

    for i in range(len(L), 0, -1):
        testList = getSublists(L, i)
        for run in testList:
            if testRun(run):
                if len(run) > longest:
                    longest = len(run)

    return longest


L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print(longestRun(L))