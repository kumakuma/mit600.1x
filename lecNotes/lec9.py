# - - - Lec9 Notes - - - -
# - Efficiency and orders of growth
# dan.smith.me@gmail.com


def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

# best case is 1
# best case is L
# average sometimes useful


def fact(n):
    answer = 1          # 1 (for assignment)
    while n > 1:        # 5n    (1 for test,
        answer *= n             # 2 for second assignment
        n -= 1                  # 2 for 3rd assignment) repeat n times
    return answer       # 1 for return

# complexity = 5n + 2

# measure complexity as function of input size


# - - - L9 P2 - - -
def program1(x):
    total = 0
    for i in range(1000):
        total += i

    while x > 0:
        x -= 1
        total += x

    return total


def program2(x):
    total = 0
    for i in range(1000):
        total = i

    while x > 0:
        x /= 2
        total += x

    return total


def program3(L):
    totalSum = 0
    highestFound = None

    for x in L:
        totalSum += x

    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x

    return (totalSum, highestFound)