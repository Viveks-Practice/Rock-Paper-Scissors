import random
import time



def throwHand():
    computer = random.randint(1,3)
    user = input("Please type in \"Rock\", \"Paper\", or \"Scissors\": ").lower()

    while (user != "rock") and (user != "paper") and (user != "scissors"):
        user = input("Please type either \"Rock\", \"Paper\", or \"Scissors\": ")

def compareHands():
    if (computer == 1 and user.to == "rock") or (computer == 2 and user == "paper") or (computer == 3 and user == "scissors"):
        print("the computer chose: ", computer, " and you chose: ", user)
        print("This round is a draw")
    else:
        print("Computer chose: ", computer)
        print("You chose: ", user)







print("Welcome to a game of Rock Paper Scissors!")
time.sleep(1)

# 1 = rock, 2 = paper, 3 = scissors
computer = 0
user = ""

throwHand()
compareHands()



# if (computer == 1 and user.to == "rock") or (computer == 2 and user == "paper") or (computer == 3 and user == "scissors"):


