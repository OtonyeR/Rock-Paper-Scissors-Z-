import random

while True:
    moves = ["R", "P", "S"]
    user_action = input("Enter a choice (R, P, S): ").upper()
    computer_action = random.choice(moves)

    if user_action in moves:

        if user_action == computer_action:
            print(f"Player(Rock) \nCPU(Scissors)\nIt's a tie!")
        elif user_action == "R" and computer_action == "S":
            print(f"Player(Rock) \nCPU(Scissors)  \nRock smashes Scissors! You win!")
            break
        elif user_action == "R" and computer_action == "P":
            print(f"Player(Rock) \nCPU(Paper)  \nPaper covers Rock! You lose!")  
            break               
        elif user_action == "P" and computer_action == "R":
            print(f"Player(Paper) \nCPU(Rock)  \nPaper covers Rock! You win!")
            break
        elif user_action == "P" and computer_action == "S":
            print(f"Player(Paper) \nCPU(Scissors)  \nScissors cuts Paper! You lose!")
            break
        elif user_action == "S" and computer_action == "R":
            print(f"Player(Scissors) \nCPU(Rock)  \nRock smashes Scissors! You lose!")
            break
        elif user_action == "S" and computer_action == "P":
            print(f"Player(Scissors) \nCPU(Paper)  \nScissors cuts Paper! You win!")
            break
    else:
        print("Wrong move, pick again")

            

    




   
    

