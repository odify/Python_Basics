# xyz

import random

game_status = "alive"

age = -1

gender = ""

name = ""

cause_death = ""

name_male_list = ['F']



name_female_list = ['M']

causes_death_list = ['x','y', 'z']


low_chance = 1
high_chance = 75

learn_python_message = False

learn_c = False
sad_message = False
job_message = False



#????????????????????????????????????????

## Functions

# def it_lives():
#     life_index = chance_dice(0,1)
#     if life_index == 0:
#         print("From out of the blue, a new life is created. \n One cell. Infinite possibilities.")
#         print("\n0\n")
#         print("00\n")
#         print("00000000\n00000000\n")
#         print("some time later...")
#     elif life_index == 1:
#         print("Welcome to life as you are now a single cell")
#         print("\n0\n")
#         print("00\n")
#         print("00000000\n00000000\n")
#         print("A while later...")

# def set_gender():
#     gender_dice = random.randint(0,1)
#     if gender_dice == 0:
#         return "female"
#     elif gender_dice == 1:
#         return "male"
#     gender_print()
    
# def gender_print():
#     print("... a large group of awesome cells is around...\n")
#     print("...then a coin is flipped and a gender is chosen. \nThe cromossomes responsible for this task looks like this:")
#     if gender == "female":
#         print("\nXX")
#     else:
#         print("\nXY")
#     print("\n ...so your gender is " + gender + ".")   
# def set_name():
#     if gender == "male":
#         name_index_male = random.randint(0 , int(len(name_male_list)) -1 )
#         return name_male_list[int(name_index_male)]
        
#     if gender == "female":
#         name_index_female = int(random.randint(0 , int(len(name_female_list))) -1 )
#         return name_female_list[int(name_index_female)]

# def name_print():
#     print("Some super fun python puzzle returns a name:")
#     print("The name given to you is \"" + str(name) + "\".")
#     print("\nAnd here goes your yearbook:")
 
# def get_death():
#     cause_index = int(random.randint(0, int(len(causes_death_list))) -1 )
#     cause_death = str(causes_death_list[int(cause_index)])
#     return cause_death

# def death():
#     print("\n======== R.I.P ========")
#     print("\"" + str(name) + "\"" +" just passed away. \nCause of death: " + get_death() + ".")
#     if age <=18:
#         print("So sad it had to go so soon...just kiddin, ITS JUST A GAME!")
#     print("\nOne last wish: PRESS THE RUN BUTTON AGAIN!\n")
    
# def natural_death():
#     print("\n======== R.I.P ========")
#     print("\"" + str(name) + "\"" +" just passed away by natural causes, had great fun and a long life.")
#     print("Oh, one last wish: PRESS THE RUN BUTTON AGAIN!")
   
    
# def chance_dice(a,b):
#     return int(random.randint(a,b))
    
# # BREAK