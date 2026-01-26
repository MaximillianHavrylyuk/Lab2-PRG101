#Author:Maximillian Havrylyuk
#Lab2i.py
#importing modules and using a while loop with if statements and using continue and break commands on the loop.

#importing the math module for square root function
import math
#creating while loop
while True:
#asking user for a number input
    num = int(input("Please type in a number: "))
#setting the condition if the number is negative to print out invalid number and to continue the loop.
    if num <=-1:
        print("Invalid number.")
        continue
#setting the condition if the number is zero to exit the while loop and printing exiting so the user knows the loop has ended
    if num == 0:
        print("Exiting ...")
        break
#calculating the square root of any postive number that the loop recieves
    sqrt_num = math.sqrt(num)
    print(sqrt_num)
