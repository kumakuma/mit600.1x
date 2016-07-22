# - - - L10 Notes - - - #

#
# Indirection
"""
arbitrary length lists
represent a list as a combination of length
and a sequence of fixed size pointers
"""


# def foo(num):
#     L = [2, 0, 1, 5, 3, 4]
#     val = 0
#     for i in range(0, num):
#         val = L[L[val]]
#
#     print val
#
# pass1 = L[L[0]] = L[2] = 1
# pass2 = L[L[1]] = L[0] = 2
# pass3 = L[L[2]] = L[1]

# - infinite loop (?)
# def foo(L):
#     val = L[0]
#     while (True):
#         val = L[val]
#     return val
#
# a = [1, 2, 3, 4, 0]
# b = [3, 0, 2, 4, 1]
# c = [3, 2, 4, 1, 5]
#
# print(foo(c))

# - Binary search - #
"""
divide and conquer - cut in half each time
so O(log n)
"""


def search(L, e):
    def bSearch(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = low + int((high - low) / 2)
        if L[mid] > e:
            return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)

    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)


def rBinarySearch(list, element):
    if len(list) == 1:
        return element == list[0]
    mid = len(list) / 2
    if list[mid] > element:
        return rBinarySearch(list[:mid], element)
    if list[mid] < element:
        return rBinarySearch(list[mid:], element)
    return True


# Selection Sort
def selection_sort(list):
    for i in range(len(list) - 1):
        min_index = i
        min_value = list[i]
        j = i + 1
        while j in len(list):
            if min_value > list[j]:
                min_index = j
                min_value = list[j]
            j += 1
        temp = list[i]
        list[i] = list[min_index]
        list[min_index] = temp


# merge sort
import operator

def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def mergesort(L, compare = operator.lt):
    if len(L) < 2:
        return list[:]
    else:
        middle = int(len(L) / 2)
        left = mergeSort(L[:middle], compare)
        right = mergesort(L[middle:], compare)
        return merge(left, right, compare)



def swapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L


def modSwapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "Final L: ", L


# alist = [1, 12, 5, 3, 2, 6, 8, 0, 12, 24]
# swapSort(alist)
# print('*****')
# alist = [1, 12, 5, 3, 2, 6, 8, 0, 12, 24]
#
# modSwapSort(alist)
#


def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size - i - 1] == e:
            return True
        if L[i] < e:
            return False
    return False


list0 = []
e = 1

print(search(list0, e), newsearch(list0, e))
