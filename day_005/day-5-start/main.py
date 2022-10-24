fruits =["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")

#For Loop with Range
for number in range(1, 10):
  print(number)

# will print up to but not including last number in range so +1 to range to include the number you want to end the range at
for number in range(1, 11):
  print(number)

# range with step and a comma and the number of steps you want it to skip
for number in range(1, 11, 3):
  print(number)

# add all number from 1 - 100
total = 0
for number in range(1, 101):
  total += number
print(total)