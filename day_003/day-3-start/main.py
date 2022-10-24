print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# Other comparison Operators
# Greater than or equals to >=
# Equal to ==
# not equal to !=

# if height >= 120:
#   print("You can ride the rollercoaster!")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# Nested if statment
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age <= 18:
#     print("please pay $7.")
#   else:
#     print("Please pay $12.")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# # elif statment
# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#     print("please pay $5.")
#   elif age <= 18:
#     print("please pay $7.")
#   else:
#     print("Please pay $12.")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# # multiple if's statment
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age?"))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")

#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo =="Y":
#     #Add $3 to thier bill
#     bill += 3
#   print(f"Your final bill is {bill}")
    
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# Logical operators
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    bill = 0
    print("Special midlife crisis discount!!! you go free")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo =="Y":
    #Add $3 to thier bill
    bill += 3
  print(f"Your final bill is {bill}")
    
else:
  print("Sorry, you have to grow taller before you can ride.")