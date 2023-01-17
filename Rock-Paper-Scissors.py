import random
import time



def throwHand():
    global computer
    global user

    print("Generating computer decision...")
    time.sleep(1)
    computer = random.randint(1,3)
    user = input("Please type in \"Rock\", \"Paper\", or \"Scissors\": ").lower()
    time.sleep(1)

    while (user != "rock") and (user != "paper") and (user != "scissors"):
        user = input("Please type either \"Rock\", \"Paper\", or \"Scissors\": ")

def compareHands():
    global computer
    global user
    global userWins
    global computerWins
    global dict
    if (computer == 1 and user == "rock") or (computer == 2 and user == "paper") or (computer == 3 and user == "scissors"):
        print("The computer chose: ", computer, " and you chose: ", user)
        print("This round is a draw")
        return "draw"
    
    elif computer == 1 and user == "paper":
        time.sleep(1)
        print("Computer chose: ", dict[computer])
        time.sleep(1)
        print("You chose: ", user)            
        userWins += 1
        print("You win!")
    elif computer == 1 and user == "scissors":
        time.sleep(1)
        print("Computer chose: ", dict[computer])
        time.sleep(1)
        print("You chose: ", user)            
        computerWins += 1
        print("The Computer won that round.")
    elif computer == 2 and user == "rock":
        time.sleep(1)
        print("Computer chose: ", dict[computer])
        time.sleep(1)
        print("You chose: ", user)        
        computerWins += 1
        print("The Computer won that round.")
    elif computer == 2 and user == "scissors":
        time.sleep(1)
        print("Computer chose: ", dict[computer])
        time.sleep(1)
        print("You chose: ", user)            
        userWins += 1
        print("You win!")
    elif computer == 3 and user == "rock":
        time.sleep(1)
        print("Computer chose: ", dict[computer])
        time.sleep(1)
        print("You chose: ", user)            
        userWins += 1
        print("You win!")
    elif computer == 3 and user == "paper":
        time.sleep(1)
        print("Computer chose: ", dict[computer])
        time.sleep(1)
        print("You chose: ", user)        
        computerWins += 1
        print("The Computer won that round.")




# 1 = rock, 2 = paper, 3 = scissors
computer = 0
user = ""
computerWins = 0
userWins = 0
playAgain = "yes"

dict = {1 : "rock", 2 : "paper", 3 : "scissors"}
print("Welcome to a game of Rock Paper Scissors!")


while playAgain == "yes":
    throwHand()
    if compareHands() == "draw":   
        continue

    time.sleep(1)
    print("You have won: ", userWins, " times!")
    time.sleep(1)
    print("The Computer has won: ", computerWins, " times.")
    time.sleep(1)
    playAgain = input("Play another round? Type \"Yes or \"No: ").lower()
    while playAgain != "yes" and playAgain != "no":
        playAgain = input("Please type \"Yes\" or \"No\": ").lower()



# if (computer == 1 and user.to == "rock") or (computer == 2 and user == "paper") or (computer == 3 and user == "scissors"):


