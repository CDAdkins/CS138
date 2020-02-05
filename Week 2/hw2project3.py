#! /usr/bin/python
# Exercise No.   3
# File Name:     hw2project3.py
# Programmer:    Chris Adkins
# Date:          Feb. 4, 2020
#
# Problem Statement: A program to average a user-defined number of test scores.
#
# Overall Plan:
# 1. Print a welcome message to the user.
# 2. Create an int to hold the number of tests that will be averaged called numberOfTests.
# 3. Use input() to receive the number of tests to be averaged.
# 4. Create an int called average to hold the average test score.
#    (It will also be used to hold the total prior to averaging.)
# 5. Create a for-loop that loops a number of times based on the numberOfTests int.
# 6. Every loop ask the user to input the test score.
# 7. Add the user's input to the "average" variable until done.
# 8. Set the average variable to itself divided by numberOfTests.
#
# Import the necessary python libraries
# For this example none are needed


def main():
    print("This program takes a user-defined number of test scores and averages them.")
    numberOfTests = eval(input("How many tests are there? "))
    average = 0  # This will first represent the total, but will eventually be the average.

    for i in range(numberOfTests):  # Loop once for every test score.
        average += eval(input("Enter Test Score " + str(i + 1) + ": "))  # Add the test score to the total.

    average /= numberOfTests  # Dividing the total by the number of tests gives us the average.
    print("The average test score is", average)  # Print the average back to the user.


main()
