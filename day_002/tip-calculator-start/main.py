#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")

total = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

tip_as_float = (tip / 100 + 1) 

people = int(input("How many people to split the bill? "))

amount = round((total / people) * tip_as_float , 2)

# floats ending in 0 e.g 10.60 will be displayed as 10.6 this is a format issue not a math issue. use {:.2f}
# amount = "{:.2f}".format(amount)
#print(amount)


print(f"Each person should pay: ${amount}")