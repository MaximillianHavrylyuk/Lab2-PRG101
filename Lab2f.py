#Author:Maximillian Havrylyuk
#Lab2f.py
#using nested if statements and practicing using arithemetic operators.

#requesting input for annual income and marital status
income=int(input("print your annual income: $"))
status=input('enter your marital status: ')

#seeing if input is single with multiple variations using in() in case user thinks of different words for single
if status in("single","Single","Alone","alone","unmarried","Unmarried"):
    
#checking if income is less than $32,000 and printing the taxed income with a rate of 10%
    if income <=int(32000):
        TakeHome=income * 0.9
        print("$",TakeHome)
#checking if income > $32000 and then calculating the taxed income after 32000 with a tax rate of 25%.
#I subtract 3200 before multiplication as thats the maximum taxable rate for 32000 at 10%
    elif income >= int(32001):
        TakeHome= (((income -32000) - 3200) * 0.75) + 32000
        print("$",TakeHome)
#checking if income is less than $64,000 and printing the taxed income with a rate of 10%
elif status in("married","Married","taken","Taken"):
    if income <= int(64000):
        TakeHome=income * 0.9
        print("$",TakeHome)
#checking if income > $64000 and then calculating the taxed income after 64000 with a tax rate of 25%.
#I subtract 6400 before multiplication as thats the maximum taxable rate for 64000 at 10%
    elif income >=int(64000):
        TakeHome= (((income - 64000) - 6400) * 0.75) + 64000
        print("$",TakeHome)
