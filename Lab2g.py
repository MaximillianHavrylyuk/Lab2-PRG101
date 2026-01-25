#Author:Maximillian Havrylyuk
#Lab2g.py
#using while loop with integers and strings to make a word scramble style of game.

count = 1  # iteration variable, while loop requires a relevant variable which is used in the loop expression
while count <= 5: # expression (evaluates to True or False)
    print(count)   # Loop body
    count = count + 1  # Loop body, count is incremented,  or else the loop will continue forever
print('loop has ended')  # This statement is not part of loop body. This statement will be executed once the loop condition becomes false.

#I obeserved that the loop identifies 0 as a valid number and that count < 5 will not include 5 in the loop count unless the operator
#less than or equal to (<=) operator is used.


#I had some fun and decided to create a word scramble game.
#number of attempts the user has before the loop breaks and tells the user that they lose.
attempts=5
#the word that the user has to guess.
Hangman=str("fact")
#input to tell the user what letters they have to unscramble
guess=str(input("spell the correct word given the letters: t, f, c, a: "))
#while loop with the condition to keep running while var:guess is not equal to the word which is the hangman variable.
while guess!=Hangman:
    #a print() statement to tell the user how many attempts they have remaining.
    print("You have",attempts,"attempts remaining!")
    #an input for the user to guess the word
    guess=str(input("Oops wrong again! Spell the correct word given the letters: t, f, c, a "))
    #function for the attempts to count down
    attempts= attempts - 1
    #if statement that will break the loop when attempts reaches 0
    if attempts == 0:
        print("You LOSE!")
        break
        #elif statement that tells the user they win and breaks loop if they guess the right word within their attempts
    elif guess==Hangman:
        print("YOU WIN!!!")
        break
