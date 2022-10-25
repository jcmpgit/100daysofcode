# https://docs.python.org/3/library/functions.html
print("Hello")
num_char = len("Hello")
print(num_char)

#creating your own functions
# define functions
def my_function():
  print("Hello")
  print("Bye")
# call function
my_function()

# reborg's world
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Draw square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()


# Hurdle challenge 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#Hurdles loop challenge 
for step in range(6):
    jump()

#using while loop instead
number_of_hurdles = 6
while number_of_hurdles > 0:
  jump()
  number_of_hurdles -= 1
  print(number_of_hurdles)

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
#Hurdles race
#Hurdles while challenge 
while at_goal() == False:
  jump()

#Teacher Solution
while at_goal != True:
  jump()
#or
while not at_goal():
  jump()


#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
#Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

#Hurdles loop challenge 
while not at_goal():
    if wall_in_front() == True and front_is_clear() == False:
        jump()
    else: move()

#Teachers solution 
while not at_goal():
    if wall_in_front():
        jump()
    else: move()

#http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#Hurdles variables heights

#hurdle 4 my solution 
# 

# Teachers soltuion
def turn_right():
    turn_left()
    turn_left()
    turn_left()
#edited jump 
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()    
    while front_is_clear():
        move()
    turn_left()
            
        
   
#Hurdles loop challenge 
while not at_goal():
    if wall_in_front():
        jump()
    else: 
        move()


# rebrogs maze 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
#Hurdles loop challenge 
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: turn_left()

#bug fix for problem worlds
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
   
#Hurdles loop challenge 
while not at_goal():
    if right_is_clear(): 
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: turn_left()