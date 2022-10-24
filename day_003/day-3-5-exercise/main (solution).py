# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
name_to_lower = name.lower()
count_t = name_to_lower.count("t")
count_u = name_to_lower.count("u")
count_r = name_to_lower.count("r")
count_e = name_to_lower.count("e")
# print(f"T count{count_t}")
# print(f"R count{count_r}")
# print(f"U count{count_u}")
# print(f"E count{count_e}")
true_count = str(count_t + count_r + count_u + count_e)
# print(f"true count is {true_count}")

count_l = name_to_lower.count("l")
count_o = name_to_lower.count("o")
count_v = name_to_lower.count("v")
count_ee = name_to_lower.count("e")
# print(f"L count{count_l}")
# print(f"O count{count_o}")
# print(f"V count{count_v}")
# print(f"E count{count_ee}")
love_count = str(count_l + count_o + count_v + count_ee)
# print(f"love count is {love_count}")

score = true_count + love_count
# Teachers difference instead of converting to string then to int she did it in one line, mine was spread out.
# score = int(str(true_count) + str(love_count))
# print(score)

score_as_int = int(score)
if score_as_int < 10 or score_as_int > 90:
    print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int >= 40 and score_as_int <= 50:
    print(f"Your score is {score_as_int}, you are alright together.")
else:
    print(f"Your score is {score_as_int}.")

