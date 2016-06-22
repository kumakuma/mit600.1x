# - Lecture 3 notes - 22/06/2016

# ----- L3 2a -----
# - while loop to print 2, 4, 6, 8, 10
#
#
# x = 2
# while x <= 10:
#     if x % 2 == 0:
#         print(str(x))
#     x += 2
# print("Goodbye!")

#
#  ----- L3 2b -----
#
#
# x = 10
# print("Hello!")
# while x >= 2:
#     print(str(x))
#     x -= 2

#
# ----- L3 2c -----
#
# while loop that sums up to and including a pre-defined *end
# given by the test code
#
# x = 0
# total = 0
# while x <= end:
#     total += x
#     x += 1
# print(str(total))


#
# ----- GUESS AND CHECK -----
#
#  ----- find the cube root -----

x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) + " is not a pefect cube")
else:
    print('Cube root of ' + str(x) + ' is ' + str(ans))
