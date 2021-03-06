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
# ----- GUESS AND CHECK ----- #
# ----- find the cube root -----
#
# x = int(raw_input('Enter an integer: '))
# ans = 0
# while ans**3 < x:
#     ans = ans + 1
# if ans**3 != x:
#     print(str(x) + " is not a pefect cube")
# else:
#     print('Cube root of ' + str(x) + ' is ' + str(ans))

# ----- find the cube root +/- numbers -----
#  exploits abs(x) function that returns absolute value of a number
#
# x = int(raw_input('Enter an integer: '))
# ans = 0
# while ans**3 < abs(x):
#     ans += 1
# if ans**3 != abs(x): # abs value of x
#     print(str(x) + ' is not a perfect cube')
# else:
#     if x < 0:
#         ans = - ans
#     print('Cube root of ' + str(x) + ' is ' + str(ans))

#
# ----- L3 P3 -----
#
# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print char
#     else:
#         numCons -= 1
#
# print 'numVowels is: ' + str(numVowels)
# print 'numCons is: ' + str(numCons)

#
# greeting = 'Hello!'
# count = 0
#
# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print letter
#     print letter
# print 'done'

# num = 10
# for num in range(5):
#     print num
# print num


# for v in range(20):
#     if v % 4 == 0:
#         print v
#     if v % 16 == 0:
#         print str(v) + 'Foo!'

# ----- L3 p5a -----#
# for i in range(0, 10, 2):
#    print(str(i + 2))
# print "Goodbye!"

# print("Hello!")
# for i in range(10, 0, -2):
#     print(str(i))

# total = 0
# for i in range(end + 1):
#     total = total + i
# print(str(total))


# ----- program to convert to binary -----
# #
# num = int(raw_input("enter a decimal number to convert: "))
# if num < 0:
#     isNeg = True
#     num = abs(num)
# else:
#     isNeg = False
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num % 2) + result
#     num = num / 2
# if isNeg:
#     result = '-' + result
# print(result)

# ----- approximation methods -----
# x = 25
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# while (abs(ans**2 - x)) >= epsilon and ans <= x:
#     ans += step
#     numGuesses += 1
# print('numGuesses = ' + str(numGuesses))
# if abs(ans**2 - x) >= epsilon:
#     print('failed on square root of ' +str(x))
# else:
#     print(str(ans) + ' is close to the square root of ' + str(x))

# ----- BISECTION SEARCH -----
# guess middle 0 to x, and then make guess smaller or larger as necessary.
# x = 25
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# ans = (high + low)/2.0
# while abs(ans**2 - x) >=epsilon:
#     print('low: ' + str(low) + ' high: ' + str(high) + ' ans: ' + str(ans))
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print('numGuesses = ' + str(numGuesses))
# print(str(ans) + ' is close to the square root of ' + str(x))

# ----- l3 P9 -----
# Guess the secret number 0 - 100
# high = 100
# low = 0
# guess = (high + low) / 2
# reply = ''
# prompt = "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter'c' to indicate I guessed correctly.  "
# print('Please think of a number between 0 and 100!')
# while reply != 'c':
#     reply = str(raw_input('Is your secret number ' + str(guess) + '?\n' + prompt))
#     if reply == 'h':
#         high = guess
#     elif reply == 'l':
#         low = guess
#     elif reply == 'c':
#         break
#     else:
#         print"Sorry I did not understand your input."
#     guess = (high + low) / 2
# print("Game over your secret number was: " + str(guess))

# ----- NEWTON RAPHSON Root Finding -----
#
#  finds the root of a polynomial ( g - p(g)/p'(g) )
#
# epsilon = 0.01
# y = 24.0
# guess = y/2.0
#
# while abs(guess*guess - y) >= epsilon:
#     guess = guess - (((guess**2) - y) / (2*guess))
# print('Square root of ' + str(y) + ' is about ' + str(guess))
