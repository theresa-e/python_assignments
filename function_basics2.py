# 1. Countdown
def countdown(num):
    numList = []
    for count in range(0, num+1):
        numList.append(count)
    print(numList)
    print(len(numList))

# 2. Print and Return 
def printAndReturn(num1, num2):
    print(num1)
    return num2

# 3. First Plus Length
def firstPlusLength(list):
    firstVal = list[0]
    listLength = len(list)
    print('First Value is:', firstVal, 'List length is: ', listLength)


# 4. Values Greater than Second - Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value.  Print how many values this is.  If the array is only element long, have the function return false

def valuesGreaterThanSecond(list):
    newList = []
    if len(list) <= 1:
        return False
    else:
        secondVal = list[1]
        count = 0
        for count in list:
            if count > secondVal:
                newList.append(count)
    print('New List - ', newList)
    print('How many - ', len(newList))

# This Length, That Value - Given two numbers, return array of length num1 with each value num2.  Print "Jinx!" if they are same.

def lengthValue(num1, num2):
    if num1 == num2:
        print('Jinx!')
    else:
        newList = []
        for i in range(0, num1):
            newList.append(num2)
    return newList
