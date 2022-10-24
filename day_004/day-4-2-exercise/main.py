# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
count = len(names)
# -1 because list starts at 0 but count starts at 1
# last index is 1 less than total number of items
bingo = random.randint(0, count - 1)
print(count)
print(bingo)
print(names[bingo])
print(f"{names[bingo]} is going to buy the meal today!")


