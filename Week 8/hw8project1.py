# Exercise No.   1
# File Name:     hw8project1.py
# Programmer:    Chris Adkins
# Date:          Apr. 7, 2020
#
# Problem Statement: This program calculates and outputs the Fibonacci sequence a number of times as dictated by the user.
#
# Overall Plan:
# 1. Get input from the user.
# 2. Create a method to calculate the Fibonacci sequence.
#   a. Define three integers, one for the first number, the second, and a temp.
#   b. Set the first and second ints equal to one.
#   c. Print the first number to the user prior to beginning a for loop.
#   d. Inside the loop, set temp = first + second. Then set the first number = second.
#   e. Set the second number equal to the temp value. Then print the first number once again.
# 3. Use the user's input as an argument when calling the Fibonacci method.
# 4. Use the main method to call the Fibonacci method with the user's input.
#
# Import the necessary python libraries.
# None needed.

def getInput():  # Method for getting and returning an int from the user.
    numbers = eval(input("Enter the number of Fibonacci numbers you'd like me to calculate: "))
    return numbers

def fibonacci(num):  # Method for calculating and outputting the fibonacci sequence to the user.
    firstNumber = 1
    secondNumber = 1
    temp = 0  # This is a variable used to keep track of the sum of the two ints when swapping numbers.
    print(firstNumber)  # This statement gives us the initial "1" that we would miss had this not been here.
    for i in range (num):
        temp = firstNumber + secondNumber  # Setting aside some memory for the sum of the two numbers.
        firstNumber = secondNumber
        secondNumber = temp
        print(firstNumber)
        
def main():
    fibonacci(getInput())  # Calling fibonacci() with the getInput() method as an argument.

main()