import random


def comp_choice():
    return random.choice(["stone", "paper", "scissors"])

def check(user, comp):
    if user == comp:
        return "Draw"
    elif (user == "stone" and comp == "scissors") or (user == "paper" and comp == "stone") or (user == "scissors" and comp == "paper"):
        return "You Win :)"
    else:
        return "You Lose :("

def play_game():  
    user_score = 0
    comp_score = 0
    while True:
        user = input("Enter stone/paper/scissors: \nEnter exit to stop:").lower()

        if user not in ["stone", "paper", "scissors","exit"]:
            print("Invalid input!")
        
        elif user=="exit":
            break    
        else:
            comp = comp_choice()

            print("Computer chose:", comp)
            result = check(user, comp)

            print("Result:", result)
            if result == "You Win :)":
                user_score += 1
            elif result == "You Lose :(":
             comp_score += 1

            print("Score -> You:", user_score, "| Computer:", comp_score)

        