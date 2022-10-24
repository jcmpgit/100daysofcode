# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Write your code below this line 👇
# if year % 4 == 0:
#     print("Leap year.")
#     if year % 100 == 0:
#         print("Not leap year.")
#     elif year % 400 == 0:
#         print("Leap year.")
# else:
#     print("Not leap year.")
#
#cheated slightly 
#forget to close if statment so for some answers i was not geting answer
#
#

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")



