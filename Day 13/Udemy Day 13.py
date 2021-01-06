#Focusing on Debugging code

#To really start debugging the proble you have to describe the problem

############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

#The above bug is that this is using range 1, 20 and 20 will not reach 20 because 20 is omitted. The below should work when executed
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

#This above is a once every few times error where it is index out of range. The problem is that the range is 1 to 6 but because the list index starts at 0 6 is out of range. The below shuold never fail:
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

#Looking at the above, I can tell right away that the 1994 will not have an output. So one of the conditions should be equal to 1994. The below should work after looking up what year gen z starts
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")



# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

#The above I can see the syntax error that is above will be the print statment not being an f string. The below will work just fine
# age = input("How old are you?")
# if age > 18:
# print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Looking at the above I see the that there is a double equal sign which is comparison and not setting the words per page to input. The below will work
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#I know that in the code above the append statement will only append the last item and not every item. I am not sure if this is the intent. To my knowledge the real problem is that the b_list.append() is not in the for loop so there is a logic error in here. It should look like below:
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])



#Day 13 Challenge 1 wants me to debug odd or even exercise

# number = int(input("Which number do you want to check?"))

# if number % 2 = 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
  
#Looking at the above I see this is supposed to check if number is even or odd and the first line is setting number equal to 0 instead of comparing it to value 0. That will resolve the issue

# number = int(input("Which number do you want to check?\n"))

# if number % 2 == 0:
#   print("This is an even number.")
# else:
#   print("This is an odd number.")
  

#Day 13 Challenge 2 wants me to debug leap year function

# year = input("Which year do you want to check?")

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

#Function should take in year and tell us if it is a leap year or not
#Noticed that the input was not set to an integer so it cannot be used in math functions or comparisons

year = int(input("Which year do you want to check?\n"))

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
