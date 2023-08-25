rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_list=[rock, paper, scissors]
human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 fo Scissors.\n"))
print(game_list[human])
print("\nComputer Chose:")
computer = random.randint(0, 2)
print(game_list[computer])
if(human==0):
    if(computer==0):
        print("Draw!")
    elif(computer==1):
        print("You Lose!")
    else:
        print("You win!")
elif(human==1):
    if(computer==0):
        print("You Win!")
    elif(computer==1):
        print("Draw!")
    else:
        print("You Lose!")
else:
    if(computer==0):
        print("You Lose!")
    elif(computer==1):
        print("You Win!")
    else:
        print("Draw!")