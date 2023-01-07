# Getting random
from random import randint

# Getting the number
randomNumber= randint(1, 100)

# Initialising moves
moves= 0

# Logic
try:   
    for i in range(1, 11):
        userAns = int(input("Enter your guess: "))
        if(userAns<0 or userAns>100):
            print("Enter a number between 1-100")
            break
        if (userAns == randomNumber):
            print("Gotcha your answer is correct!")
            print("You guessed it in {} moves".format(moves))
            break
        elif(userAns < randomNumber):
            print("Your guess is smaller!")
            print(f"You are left with {10-i} moves")
        elif(userAns > randomNumber):
            print("Your guess is bigger!")
            print(f"You are left with {10-i} moves")
        else:
            print("An error occured")
        moves = moves+1
except :
    print(Exception)