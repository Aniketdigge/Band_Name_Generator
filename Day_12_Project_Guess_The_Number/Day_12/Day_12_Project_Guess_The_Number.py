#https://replit.com/@appbrewery/guess-the-number-start#main.py 
#https://replit.com/@appbrewery/guess-the-number-final?v=1
#http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_num = random.randint(1, 100)
print(f"Pssst, the correct answer is {computer_num}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

user_num = 0
chances = 0

if difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
    chances = 5
    while chances > 0:
        user_num = int(input("Make a guess: "))
        if user_num == computer_num:
            print("You guess correct, you win")
            chances -= 1
            print(f"You have {chances} chances left")
        elif user_num > computer_num:
            print("Too High")
            chances -= 1
            print(f"You have {chances} chances left")
        else:
            print("Too Low")
            chances -= 1
            print(f"You have {chances} chances left")
    print("Out of chances, you lose")

elif difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
    chances = 10
    while chances > 0:
        user_num = int(input("Make a guess: "))
        if user_num == computer_num:
            print("You guess correct, you win")
            chances -= 1
            print(f"You have {chances} chances left")
        elif user_num > computer_num:
            print("Too High")
            chances -= 1
            print(f"You have {chances} chances left")
        else:
            print("Too Low")
            chances -= 1
            print(f"You have {chances} chances left")
    print("Out of chances, you lose")

else:
    print("Wrong input")
    



