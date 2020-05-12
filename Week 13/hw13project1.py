# Exercise No.   5
# File Name:     hw13project2.py
# Programmer:    Chris Adkins
# Date:          May. 12, 2020
#
# Problem Statement: This program determines whether or not a user-entered string is a palindrome. (case-insensitive)
#
# Overall Plan:
# 1. Get input from the user. Create a variable for the string and for a copy of the string.
# 2. Create a normalize function to remove any punctuation from the string.
#       a. For each char in the string, if it is in ascii_letters, add it to a new string.
#       b. Use lower() to return the new string in all lowercase.
# 3. Create a palindrome function to check all of the characters against eachother.
#       a. Iterate over the string and compare the first char to the last char.
#       b. If they are the same, compare the second char to the second to last char, and so on.
#       c. If two chars don't match, return false, if they all match, return true.
#
# Import the necessary python libraries.
# ascii_letters - To detect punctuation in the strings.

from string import ascii_letters

def main():
    for i in range(2):
        word = input("Enter a string: ")
        original = word  # Keeping track of the original string.
        if (isPalindrome(word)):
            print(original, "is a palindrome!")
        else:
            print(original, "is not a palindrome!")

def normalize(aWord):  # Function to remove any spaces, punctuation or capitalization.
    newString = ""
    for i in aWord:  # Iterate over every char in the string.
        if (i in ascii_letters):  # If the char is alphanumeric. (isalpha / isalnum weren't removing punctuation)
            newString += i  # Add the char to our new string.
    return newString.lower()  # Convert the string to lowercase before returning it.

def isPalindrome(aWord):  # Returns true if palindrome, false if not.
    aWord = normalize(aWord)  # MAking sure the word received is normalized.
    index = 0  # Index used to count back from the end of the string.
    for i in aWord:  # For each char in this string.
        if (i != aWord[len(aWord) - index - 1]):  # If the current char is not equal to the char opposite.
            return False
        index += 1  # Increment the index.
    return True

main()