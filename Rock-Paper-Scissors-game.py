from random import randint
x = randint(0,2)
choices = ["Paper", "Rock", "Scissors"]
Computer_choice = choices[x]


def Game():
    Player_choice = input ("Your choice: ")
    Player_choice = Player_choice[0].upper() + Player_choice[1:].lower()
    print("You chose to play : ", Player_choice , "\n","Computer chose to play: ", Computer_choice)
    if Player_choice == Computer_choice:
        print("It's a tie")
    elif (
        Player_choice == "Rock"
        and Computer_choice == "Scissors"
        or Player_choice == "Paper"
        and Computer_choice == "Rock"
        or Player_choice == "Scissors"
        and Computer_choice == "Paper"
    ):
        print("PLayer won")
    else:
        print("The computer won")
    
    
        
Game()