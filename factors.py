# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/16/2022

# Description: Write a program that asks the user to enter a positive integer,then prints a list of all positive
# integers that divide that number evenly, including itself and 1, in ascending order.

# asking the user to enter a positive integer.
print("Please enter a positive integer: ")
# variable number takes the value of entered number.
number = int(input())
# display message.
print("The factors of ", number, "are:")
# proceed to obtain every factor for which entered number is divisible.
for i in range(1, number+1):
    # variable x takes the value of number and divides it for every single
    # value of i within specified range.
    x = number % i
    # condition to print factors.
    if x == 0:
        # printing factors
        print(i)
