import random

choice = input("Enter your choice (rock, paper, scissors): ").lower()

ia = random.choice(["rock", "paper", "scissors"])

if choice == ia:
    print(f"Both players selected {choice}. It's a tie!")
elif choice == "rock":
    if ia == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")   
elif choice == "paper":
    if ia == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif choice == "scissors":
    if ia == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")