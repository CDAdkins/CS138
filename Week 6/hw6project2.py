# Exercise No.   3
# File Name:     hw6project1.py
# Programmer:    Chris Adkins
# Date:          Mar. 3, 2020
#
# Problem Statement: This program calculates the sum of ints in an array.
#
# Overall Plan:
# 1. Create an array full of ints.
# 2. Create a function and pass the array as an argument.
# 3. Use a for loop to iterate over the array.
# 4. For each element in the array, add the value to the total.
# 5. Once the final total has been calculated, print it to the user.
#
# Import the necessary python libraries.
# None needed.


def main():
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Our array.
    print(numList)  # Printing the array to our user.
    sumList(numList)  # Calling our function with numList as an argument.


def sumList(numList):  # Our sumList function.
    total = 0  # This will increase each time we iterate over the array.
    for i in range(len(numList)):  # This loops over our array once per item.
        total += numList[i]  # Adding the value of the current item to our total.

    print("Total:", total)  # Printing the total sum to our user.


main()  # Calling our main function.
