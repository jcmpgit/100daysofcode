# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#my solution cheated using sort
# hi = 0
# i = 0
# # items = len(student_scores)
# # print(student_scores[0:items -1])
# student_scores.sort()
# for score in student_scores:
#     if score > hi:
#         i = score
# print(score)
print(f"The highest score in the class is: {highest_score}")

#Teachers solution 
highest_score = 0
#student_scores.sort()
for score in student_scores:
    if score > highest_score:
        highest_score = score
    #elif score > i:
# print(score)
print(f"The highest score in the class is: {highest_score}")





