# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#My Solutions 
# pos_as_string = str(position)
# pos1 = int(pos_as_string[0])
# pos2 = int(pos_as_string[1])
# map[pos2 -1][pos1 -1] = "X"

#Teachers solution 
horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")