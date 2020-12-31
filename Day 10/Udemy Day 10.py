#This is more about function and outputs

#Functions can have inputs or not and can also have outputs or not
def my_function():
    result = 3 * 2
    #Return bascially sets the function equal to the return result
    return result

#In order to print this out though you will have assign the function to a variable 
output =  my_function()
print(output)
#Or print the fuction itself.
print(my_function())


def format_name(first, last):
    formatted = f'{first.title()} {last.title()}'
    print(formatted) 

format_name('jacquawn', 'lockhart')


def return_format(first, last):
    formatted = f'{first.title()} {last.title()}'
    return formatted

my_name = return_format('jacquawn', 'lockhart')
print(my_name)
print(return_format('jacquawn','lockhart'))

output = len('Jacquawn lockhart')
print(output)


#Multiple return statements in a function
def return_format(first, last):
    if first == '' or last == '':
        return 'You did not input full name.'

    formatted = f'{first.title()} {last.title()}'
    return formatted
    #This will not get executed because the return keyword ends the fuction
    print('Goodbye')

print(return_format('jacquawn', ''))


#Day 10 Challenge 1 wants me to recreate leap year with return statements

year = int(input("Which year do you want to check? "))
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False        
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if year == '' or month  == '':
        return 'There is not enough information'

    if leap_year(year) == True:
        month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

    days = month_days[month-1]
    return days


print(leap_year(year))
year = int(input('What year:\n'))
month = int(input('What number month:\n'))
print(days_in_month(year, month))

#Why return over print? Sometimes you do not need to print anything and rather store it 

#Docstrings are the 3 quotation mark statement after the function declaration








