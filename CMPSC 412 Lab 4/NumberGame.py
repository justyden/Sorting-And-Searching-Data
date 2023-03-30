# A game that can guess the number a person is thinking of
# in a reasonable amount of time if the numer is in range.

import math
import sys


def NumberGame():
    list1 = []  # Creates an empty list that will store the numbers.
    for i in range(1, 10001):  # Fills the list with data.
        list1.append(i)
    print("This game will guess the number the player is thinking of.")
    # Calls the function that allows the game to function.
    memorySize = sys.getsizeof(binarySearch(list1))
    print("The memory size of all the variables in the function is " +
          str(memorySize) + " bytes.")


# Takes a different amount of parameters so that each call can keep
# track of how the list is being handled. For the first call
# there are default values to allow the user to just input
# the list without needing to know the size.
def binarySearch(list1, listBegin=True,  start=0, end=1, mid=1):
    if listBegin:  # Checks to see if it is the first time being called.
        start = 1
        end = len(list1)
        mid = len(list1) / 2
    if start > end:  # This is the end condition meaning the value was not in range.
        print("The number was not in the range.")
        return
    userInput = input("Is the number " + str(int(mid)) + " this time. ")
    if userInput[0] == 'Y' or userInput[0] == 'y':
        print("The number was found.")
        return  # This another stop condition which means the number was found.
    userInput = input("Is the number higher than that. ")
    if userInput[0] == 'Y' or userInput[0] == 'y':
        # This sets the new start point in the list.
        start = math.floor(mid + 1)
    else:
        end = math.floor(mid - 1)  # This starts the new end point in the list.
    return binarySearch(list1, False, start, end, ((start + end) / 2))


NumberGame()
