# s = "rxrxjkzpulmw"
#
# count = 0
# vowels = ['a','e','i','o','u']
#
# for letter in s:
#   for vowel in vowels:
#     if letter == vowel:
#       count += 1
#
# print("Number of vowels: " + str(count))

# s = 'azcbobobegghakl'
#
# count = 0
# target = "bob"
#
# for i in range(len(s)):
#     if i < (len(s) - 3):
#       if (s[i] + s[i+1] + s[i+2]) == 'bob':
#           count += 1
# print str(count)

# Problem 3:
# I noticed that the first letter of each item is different for each

def item_order(order):
    hamburger = 0
    salad = 0
    water = 0

    startspace = 0
    space = 0

    while space > -1:
        space  = order.find(' ', startspace)
        if space == -1:
            word = order[startspace:]
        else:
            word = order[startspace:space]
        if word == "salad":
            salad += 1
        if word == "hamburger":
            hamburger += 1
        if word == "water":
            water += 1
        startspace += 1
    neworder = "salad:" + str(salad) + " hamburger:" + str(hamburger) + " water:" + str(water)
    return neworder



    print("salad:"+str(s_count)+" hamburger:"+str(h_count)+" water:"+str(w_count))

def item_order2(order):
    h_count = 0
    w_count = 0
    s_count = 0

    words = []

    
    for letter in order:
        if letter == ' '


# test case:
# order = "hamburger water hamburger salad water"
# item_order(order)