def prime_checker(number):
    if number == 0 or number == 1:
        print(f'{number} is not prime')
    elif number == 2:
        print(f'{number} is prime.')
    else:
        for digit in range(2, number):
            if number % digit != 0:
                print(f'{number} is prime.')
                break
            if number % digit == 0:
                print(f'{number} is not prime:')
                break


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

