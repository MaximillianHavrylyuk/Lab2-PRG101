#Author:Maximillian Havrylyuk
#Lab2b.py
#using the 'if' statement to print if the boolean value is true and the else to print another statement
#if the 'if' statement doesnt return a TRUE value.

#creating a user input and telling the user to input a four digit number and leaving it as a string
#because there is no arithemetic required with the value
num = input('Enter a four digit number ')

#creating an 'if' statement to print 'George Orwell' if num is equal to 1984 and an else statement to 
#print 'Not quite right!' if the value is not equal to 1984
if num == str(1984):
    print('George Orwell')
else:
    print('Not quite right!')
