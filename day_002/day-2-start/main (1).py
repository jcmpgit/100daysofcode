#Data Types

#String

print("Hello"[4])

#Integer - whole numbers not decimals

print(123 + 345)

#Float decimal places
3.14159

#Boolean True or False
True
False


a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))

a = int(123)
print(type(a))

#substring and conversion
a = int("123"[1])
print(type(a))

#Maths in python
3 + 5
7 - 4
3 * 2
6 / 3

#divsion always results in a floating point
print(type(6 / 3))

#** is an exponent so squared numbers
2 ** 2

# PEMDAS - order of operation left most is done first if same order
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)

# change print(3 * 3 + 3 / 3 - 3) to get 3
print(3 * 3 / 3 + 3 - 3)
# actual answer
print(3 * (3 + 3) / 3 - 3)

# rounding
print(round(2.666666))

# rounding to a decimal place
print(round(2.666666 , 2))

# divsion without floating point answer
print(8 // 3)

#continue calculations on a variable 
score = 0
score += 1
print(score)

# F strings to mix data types
score = 0
height = 1.8
isWinning = True
#f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

print(12 / 100 + 1) 