# This game was built using GitHub Copilot, but notably the code
# matches this website's version almost identically:
#   https://realpython.com/python-rock-paper-scissors/

import random

user_action = input("Enter throw (rock, paper, scissors): ")
ai_action = random.choice(["rock", "paper", "scissors"])

print(f"\nYou chose {user_action}, AI chose {ai_action}.\n")

if user_action == ai_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if ai_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":                    # BUG 1 --> ai_action == 'rock':
    if ai_action == "paper":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if ai_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")                # Misleading





# Loop Logic
# while True:
#     user_action = input("Enter throw (rock, paper, scissors) or 'quit' to exit: ").lower()
# if user_action == "quit":
#     print("Thanks for playing!" Bye!")
#     break
# while user_action not in ["rock", "paper", "scissors"]:
#     user_action = input("Invalid Choice! Please enter 'rock', 'paper', or 'scissors', or 'quit' to exit.)
#     if user_action == "quit":
#         print("Thanks for playing!" Bye!")
#         break
# if user_action == "quit":
#     break

