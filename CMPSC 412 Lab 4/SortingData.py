# This program takes a text file of student data and orgainzes it
# while returning a new text file. The user may indicate how the
# data is to be organized.

import StudentData
import time
import sys

# The function used to call all other functions and allow the application
# to work. Can specify how the data is to be organized. The orgainzeData
# is what it will be sorted by. This function uses getattr which allows
# the user to input a string in the arguement of the function that
# will allow it to call methods of a class depending on what was input.
# This means this function can orgainze data by just knowing the name
# of an attribute in the data.


def sortFileID(inputFile, sortType, orgainzeData):
    tempListData = []  # Create a list that will hold all the information.
    with open(inputFile, 'r') as file:  # Opens a file.
        for line in file.readlines():  # Reads each line in the file.
            tempInformation = line.split()
            # This creates a new student object for each line in the file.
            tempStudent = StudentData.Student(int(tempInformation[0]),
                                              tempInformation[1], tempInformation[2],
                                              tempInformation[3], tempInformation[4])
            tempListData.append(tempStudent)
        file.close()

    # The checkTime variable is used to determine how long the sorting takes.
    checkTime = time.perf_counter()
    # All these check the arguments given to the function
    # and makes it behave depending on what was input.
    if sortType == 's':
        memorySize = sys.getsizeof(selectionSort(tempListData, orgainzeData))
        checkTime = time.perf_counter() - checkTime
        print("Using selection sort took " + str(checkTime) + " seconds.")
        print("The memory size was " + str(memorySize) + " bytes.")

    elif sortType == 'i':
        memorySize = sys.getsizeof(insertionSort(tempListData, orgainzeData))
        checkTime = time.perf_counter() - checkTime
        print("Using insertion sort took " + str(checkTime) + " seconds.")
        print("The memory size was " + str(memorySize) + " bytes.")

    elif sortType == 'b':
        memorySize = sys.getsizeof(bubbleSort(tempListData, orgainzeData))
        checkTime = time.perf_counter() - checkTime
        print("Using bubble sort took " + str(checkTime) + " seconds.")
        print("The memory size was " + str(memorySize) + " bytes.")

    elif sortType == 'm':
        # For this tempListData has to be set equal to the
        # the function since it returns a new organized list.
        tempListData = mergeSort(tempListData, orgainzeData)
        checkTime = time.perf_counter() - checkTime
        print("Using merge sort took " + str(checkTime) + " seconds.")
        memorySize = sys.getsizeof(mergeSort(tempListData, orgainzeData))
        print("The memory size was " + str(memorySize) + " bytes.")

    else:
        return

    userInput = input("Please enter the name of the new file to create. ")
    createFile(tempListData, userInput)
    print("The file has been created.")


# Takes a list and an input position that does
# not have to be given by the user.
def selectionSort(inputList, inputType, inputPosition=0):
    # This means that the list is fully sorted.
    if inputPosition == len(inputList):
        return
    else:
        # Saves a new position that will be edited depending how
        # the data needs to be organized.
        tempPosition = inputPosition
        tempSpot = getattr(inputList[inputPosition], inputType)
        indexSpot = inputPosition
        # Checks to make sure the tempPosition does not exceed the length
        # of the list.
        while tempPosition < len(inputList):
            if getattr(inputList[tempPosition], inputType) < tempSpot:
                tempSpot = getattr(inputList[tempPosition], inputType)
                indexSpot = tempPosition
            tempPosition = tempPosition + 1
        # This does the swapping of data if it needs to happen.
        tempData = inputList[inputPosition]
        inputList[inputPosition] = inputList[indexSpot]
        inputList[indexSpot] = tempData
        # Does the recursive call to allow it to work on the entire list.
        return selectionSort(inputList, inputType, inputPosition + 1)


# Takes a list and the input position that does not have to be
# given by the user.
def insertionSort(inputList, inputType, inputPostition=0):
    if inputPostition == len(inputList):  # The list is sorted.
        return
    else:
        # This is the last condition before the list is returned.
        if (inputPostition + 1) == len(inputList):
            return insertionSort(inputList, inputType, inputPostition + 1)
        # If the data is sorted it calls the function again and keeps checking the
        # next element in the list.
        if getattr(inputList[inputPostition], inputType) < getattr(inputList[inputPostition + 1], inputType):
            return insertionSort(inputList, inputType, inputPostition + 1)
        # This means it found an element that is not in order and it orgainze
        # it according to where it should be.
        else:
            # The tempTest variable is used to figure out if a
            # spot has been found to insert the element.
            tempTest = True
            tempPosition = inputPostition + 1
            tempData = inputList[inputPostition + 1]
            while tempTest:
                # This means the element should placed at the start
                # of the list.
                if tempPosition < 0:
                    tempTest = False
                    del inputList[inputPostition + 1]
                    inputList.insert(0, tempData)
                    break
                elif getattr(inputList[inputPostition + 1], inputType) <= getattr(inputList[tempPosition], inputType):
                    # This moves the tempPosition to search in the next element location.
                    tempPosition = tempPosition - 1
                # This means the spot was found for the element.
                else:
                    tempTest = False
                    del inputList[inputPostition + 1]
                    inputList.insert(tempPosition + 1, tempData)
            # Calls the function again to start orgainzing the rest of the elements.
            return insertionSort(inputList, inputType, inputPostition + 1)


# Takes a list as input as well as an input position and start.
# The input position and start do not have to be given by the user.
def bubbleSort(inputList, inputType, inputPosition=0, inputStart=True):
    # Checks to see if the function was called before.
    if inputStart:
        # This sets the length of the list so the function knows when it is sorted.
        inputPosition = len(inputList) - 1
        inputStart = False
    # The checkStatus variable is used to determine if an element was found that
    # is not in the correct spot.
    checkStatus = True
    for i in range(len(inputList)):
        # This means no out of place elements were found.
        if i == inputPosition:
            break
        # This means an element that was out of place was found.
        if getattr(inputList[i], inputType) > getattr(inputList[i + 1], inputType):
            checkStatus = False
            tempData = inputList[i + 1]
            inputList[i + 1] = inputList[i]
            inputList[i] = tempData
    # The list is sorted so it returns it.
    if checkStatus:
        return
    # This list is not sorted so it goes and sorts the data with another function call.
    else:
        return bubbleSort(inputList, inputType, inputPosition, inputStart)


# This function takes a list and returns a new list. It is important to
# note that the list passed is not edited since a new list is returned.
def mergeSort(inputList, inputType):
    # This means the list is sorted since there is nothing in it.
    if len(inputList) == 1:
        return inputList
    # The list is made into new lists.
    else:
        # Gets the middle point of the list.
        mid = int(len(inputList) / 2)
        tempList1 = inputList[: mid]
        tempList2 = inputList[mid:]
        # This returns the sorted list but also calls the functions
        # in a recursive way since the function calls itself in the
        # the parameter.
        return mergeSortHelper(mergeSort(tempList1, inputType), mergeSort(tempList2, inputType), inputType)


# A helper function for merge sort since it needs a way to
# organize the data. This takes multiple list and returns a new
# list that is orgainzed.
def mergeSortHelper(inputList1, inputList2, inputType):
    tempList = []
    # Makes sure the lists are not empty.
    while inputList1 != [] and inputList2 != []:
        # Compares the elements.
        if getattr(inputList1[0], inputType) <= getattr(inputList2[0], inputType):
            tempList.append(inputList1[0])
            del inputList1[0]
        else:
            tempList.append(inputList2[0])
            del inputList2[0]
    # These add the remaining elements to the new list since
    # there is nothing left to be compared for organizing.
    if inputList1 != []:
        for i in range(len(inputList1)):
            tempList.append(inputList1[i])
        del inputList1
    if inputList2 != []:
        for i in range(len(inputList2)):
            tempList.append(inputList2[i])
        del inputList2
    # This returns the new list.
    return tempList


# Creates a file inputs data into it.
def createFile(inputList, outputFile):
    with open(outputFile, 'w') as file:
        for i in range(len(inputList)):
            file.write(str(inputList[i]) + "\n")
        file.close()


sortFileID("Information.txt", 'm', "first_Name")
