#Author:Maximillian Havrylyuk
#Lab2j.py
#using for loop and using basic arithmetic within the loop

#setting the original value of variable for "for" loop to one
total = 1
#creating a for loop for a new variable that only works in the range 1-100
for number in range(1, 101):
#checks if the number is even and then adds the number variable to the running total
    if number % 2 == 0:
        total += number
#prints the total after the loop has ended
print(total)
