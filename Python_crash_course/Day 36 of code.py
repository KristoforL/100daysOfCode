#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

#This is not my custom code but I have an understnading of how I should have gone about this

#Created a string of all password option possiblities
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#Ask how long the user wants their password to be and cast that to ta integer
passlen = input("How long do you want your password?\n")
passlen = int(passlen)
#Join random samples from the list until thelength requirement is met
p =  "".join(random.sample(s,passlen))
#Prints the password for the user
print(p)


#Here is another way
import string

#literally does the same thing as above but combines all the numbers, letters and punction using the one variable:chars, with import string
def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    #joins a random choice which is similar to sample for the size the default 8 character length
	return ''.join(random.choice(chars) for _ in range(size))

#This overwrites the default password length being 8 since there is an input in this string
print(pw_gen(int(input('How many characters in your password?\n'))))
print(pw_gen())