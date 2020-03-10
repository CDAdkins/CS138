# Exercise No.   1
# File Name:     hw7project1.py
# Programmer:    Chris Adkins
# Date:          Mar. 9, 2020
#
# Problem Statement: This program takes a number between 0 and 100 and returns the proper letter grade
#                    in accordance with the CS 138 grading scale.
#
# Overall Plan:
# 1. Create a function to receive input from the user.
# 2. Use the user's input for the second function, numToGrade()
# 3. NumToGrade will be a series of if-else statements that check the input against the grade scale.
# 4. Depending on the user input, print a letter grade to the user.
#
# Import the necessary python libraries.
# None needed.

def getInput():  # Function to get input from our user.
    percentage = eval(input("What percentage of the points did you get? "))
    return percentage  # Returning whatever the user typed in.

def numToGrade(num):
    if (num < 60):  # If we have a number that is less than 60.
        print("F")  # Any number under 60 is an F, so we print f.
    elif (num < 70):
        print("D")
    elif (num < 80):
        print("C")
    elif (num < 90):
        print("B")
    elif (num <= 100):  # If the number is less than, or equal to 100.
        print("A")
    else:  # This point is only reached if the user enters a number over 100.
        print("Invalid Input")

def main():
    numToGrade(getInput())  # Calling our numToGrade function with getInput() as the argument.

main()