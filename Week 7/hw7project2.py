# Exercise No.   2
# File Name:     hw7project2.py
# Programmer:    Chris Adkins
# Date:          May. 11, 2020
#
# Problem Statement: This program generates a speeding ticket given the limit and the speed.
#
# Overall Plan:
# 1. Get input from the user and initialize a speed and limit variable.
# 2. If the limit is greater than the speed then the user didn't break the law.
# 3. Otherwise add $50 to the fine and find how much they broke the speed limit by. Multiply that by 5 and add it to the fine.
# 4. If the speed was > 90, add $200, if not add nothing and print the result to the user.
#
# Import the necessary python libraries.
# None needed.

def main():
    limit = eval(input("Enter the speed limit: "))  # Getting the speed limit.
    speed = eval(input("Enter the speed you were going: "))  # Getting the speed.
    if (limit > speed):  # If the user was not speeding.
        print("You did nothing wrong")
        return 0
    else:  # If the user was speeding.
        mphOver = speed - limit  # How many mph over the speed limit were you.
        fine = 50  # Base amount of $50.
        fine += (mphOver * 5)  # Adding $5 for every mph over the limit.
        if (speed > 90):  # If the speed was greater than 90.
            fine += 200  # Add the extra $200 for breaking 90mph.

    print("Your fine is $", fine)  # Print the fine to the user.

main()