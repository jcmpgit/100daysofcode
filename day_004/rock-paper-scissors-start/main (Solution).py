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
# * How you will store the user's input.
p1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# list for diaplyer user state index varible is player choice
shape = [rock, paper, scissors]
print(f"{shape[p1]}")
# * How you will generate a random choice for the computer.
print("Computer chose:")
p2 = random.randint(0, 2)
print(f"{shape[p2]}")

# * How you will compare the user's and the computer's choice to determine the winner (or a draw).
if p1 == 0 and p2 == 2:
  print("You win!")
  #print(rock, scissors)
elif p1 == 2 and p2 == 1:
  print("You win!")
  #print(scissors, paper)
elif p1 == 1 and p2 == 0:
  print("You win!")
  #print(paper, rock)
elif p1 == p2:
  print("Draw")
else:
  print("You lose!")

 
