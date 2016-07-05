# - Python likes fruits - 4th July 2016

def nfruits(fruits, eatingPattern):
    """
    :param fruits: a non empty dictionary with less than 10 keys
    :param eatingPattern: string pattern of the fruits eaten by Python
    :return: int - the maximum quantity of any one type of fruit
    """
    #  iterate through each letter representing a fruit in eatingPattern
    for i in range(len(eatingPattern)):
        #  set eatenFruit to the fruit's letter
        eatenFruit = eatingPattern[i]
        #  decrement the quantity of the eaten fruit
        fruits[eatenFruit] -= 1

        #  iterate through each fruit in fruits
        for aFruit in fruits:
            #  guard to 1 - ignore the last letter as that is when python
            #  reaches the campus.
            #  2 - to only apply the increent to aFruit that is not the eaten fruit
            if i < len(eatingPattern) - 1 and aFruit != eatenFruit:
                fruits[aFruit] += 1

    #  set the result to the max of all values in the dictionary
    result = max(fruits.values())

    return result


# Test Case
# print(nfruits({'A': 10, 'R': 7, 'B': 5, 'K': 7, 'L': 7}, 'BLAL'))

