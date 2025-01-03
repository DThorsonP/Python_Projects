import random

options = ["rock", "paper", "scissors"]

user_choice = input("What do you choose? rock, paper or scissors\n")
computer_choice = random.choice(options)

print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)

if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")