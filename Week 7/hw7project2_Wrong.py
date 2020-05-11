# Exercise No.   2
# File Name:     hw7project2.py
# Programmer:    Chris Adkins
# Date:          Mar. 9, 2020
#
# Problem Statement: This program takes a date in MM/DD/YYYY
#
# Overall Plan:
# 1. Get input from the user.
# 2. Use the user's input and check it against our array of days in a month.
# 3. If the date is within the acceptable range for the month, it is valid, otherwise it is invalid.
# 4. Print whether or not the date is valid back to the user.
#
# Import the necessary python libraries.
# None needed.

# Array of ints that correlate with the number of days in each month.
daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getInput():  # Function used to get input from the user.
    month = eval(input("Enter the month number EG. January = 1: "))
    day = eval(input("Enter the day: "))
    year = eval(input("Enter the year: "))
    checkDate(month, day, year)  # Calling our checkDate() function with the inputs from the user.

def checkDate(month, day, year):  # Function to verify if a date is valid
    if (day > daysInMonths[month - 1] or day < 1):  # If there are too many or too few days for that month.
        print(printDate(month, day, year), "is not a valid date.")
    else:  # If the number of days is valid for the given month.
        print(printDate(month, day, year), "is a valid date.")

def printDate(month, day, year):  # Function to print the date given by the user in proper format.
    date = str(month) + "/" + str(day) + "/" + str(year)
    return(date)

def main():
    getInput()  # We only have to call the getInput() function because we will call the rest from within our functions.


main()