#Author:Maximillian Havrylyuk
#Lab2h.py
#using simple while loop with user inputs

#creating user input to put in a PIN
pin=int(input("Please type in your PIN: "))
#variable for the password
password=1234
#while loop that runs until the user puts in 1234 and prints when they are wrong and right.
while pin!=password:
    print("Incorrect... try again ")
    pin=int(input("Please type in your PIN: "))
print("Correct PIN, You can enter!")
