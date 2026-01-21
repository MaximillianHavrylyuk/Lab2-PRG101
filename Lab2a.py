#Author:Maximillian Havrylyuk
#Lab2a.py
#learning to write if statements and practicing my logic with relational and boolean operators.

#creating a variable that takes a user input also with the string 'enter a number' so the user knows
#what to input and also changing the input of the user to a integer.
x = int(input('Enter a number '))

#checking the data type of x to make sure its an integer.
print(type(x))

#creating an if statement to check if x is greater than or equal to 6 and if the expression is true,
#then printing the string 'x is greater than 6'.
if x >= int(6):
    print('x is greater than 6')

#creating an if statement to print the string in the print statement below and is only true when
# x is greater than or equal to 4 and x is less than 2. This statement is purely logic and will
#never be true.
if x >= 4 and x < 2:
    print('x is greater than or equal to 4 OR less than or equal to 2')
