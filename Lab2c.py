#Author:Maximillian Havrylyuk
#Lab2c.py
#using the if, elif and else functions to see if the len() of the user's inputs are < or > or = and
#printing different statements to display which user inputs are longer than eachother or equal to eachother.

#creating two variables and making them inputs and displaying the string to the user to ask them to make
#sentences.
str1 = input('Make your first sentence ')
str2 = input('Make your second sentence ')

#checking the len() of both user inputs to then print whichever sentence has more characters or if both
#if and elif statements return false then I used the else statement to return a print() to tell the user
#that both user input's are of equal length
if len(str1) > len(str2):
    print(str1,'is longer than', str2,'!')
elif len(str1) < len(str2):
    print(str2,'is longer than',str1,'!')
else:
    print(str1,'and', str2, 'are of equal length.')
