#Day 5 will be focusing on Python Loops

fruits = ['Apple', 'Peach', 'Pair']
#This for loop will go through each item in the list assign the item to the fruit variable and then print that fruit and then again with the next item in the list until there are not more items in the lis to print
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

#Being inside a for loop and outside the for loop is important. Indentation will be important when performing task in the loop. See above.

#Day 5 Challenge 1 wants me to calculate the average height and round it to the nearest whole number

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
count  = 0
total = 0
for n in student_heights:
    count += 1
    total += n

avg = total/count

print(f'Average height of the heights you have given is {round(avg)}')


#Day 5 Challenge 2 wants me to make a highscore checker

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highscore  = 0
for score in student_scores:
    if score > highscore:
        highscore = score

print(f'The highest score is  {highscore}!!')

#Could utilize the max() min() len() and so in the above challenges but to be creative with numbers you

#For loops with range function
#Range will include the first variable and not the second 
for number in range(1,10):
    print(number)
#This range includes 10 but not 11
for number in range(1,11):
    print(number)
#This will cycle through the range by 2
for number in range(1,11,2):
    print(number)
total = 0
for number in range(1,101):
    total+=number


#Day 5 Challenge 3 wants me to add evens
total = 0
for number in range(1, 101, 2):
    total += number

print(f'Sum of all the even numbers from {total}')


#Day 5 Challenge 4 wants me to create the fizzbuzz game

#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz". When the number is divisible by 5, then instead of printing the number it should print "Buzz". And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1,101):
    if number % 3  == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)