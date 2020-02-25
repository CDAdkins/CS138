# Exercise No.   4
# File Name:     hw5project1.py
# Programmer:    Chris Adkins
# Date:          Feb. 25, 2020
#
# Problem Statement: This program takes input from the user and creates an acronym from it.
#
# Overall Plan:
# 1. Create two strings, one to hold the input from the user and one to hold the acronym.
# 2. Iterate through the phrase with a for loop.
# 3. For each loop, if it is the first character, add it to the acronym variable.
# 4. If we aren't on the first character, check for a space before the current character.
# 5. If there is a space, then add the following character to the acronym.
# 6. Print the acronym to the user.
#
# Import the necessary python libraries.
# None needed.


def main():
    phrase = input("Enter a phrase: ")  # Get our phrase from the user.
    acronym = ""  # What will become our acronym.
    for i in range(len(phrase)):  # For every character in 'phrase'.
        if (i == 0):  # If we're looking at the first character.
            acronym += phrase[i].upper()  # Capitalize the character and add it to the acronym.
        elif (phrase[i] == " "):  # If we find an empty space character.
            acronym += phrase[i + 1].upper()  # Capitalize and add the following character to the acronym.
    print(acronym)  # Print our acronym.


main()
