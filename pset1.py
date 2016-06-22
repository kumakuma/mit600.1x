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
    h_count = 0
    w_count = 0
    s_count = 0

    for letter in order:
        if letter == 'h':
            h_count += 1
        elif letter == 's':
            s_count += 1
        elif letter == 'w':
            w_count += 1

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