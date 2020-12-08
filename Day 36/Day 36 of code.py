#This is further practive bfore the test on Sunday. I will be reading the chapters again from the pcep website and having some of the practice executed here

###--Practice and review questions before PCEP--###
#Same as from the 21st day of code practice
# I have gotten some of these practice problems from https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

import random

#Currently thinking about how to go about this
#Do I create multiple list for the the character combinations or can I use the hexidemcials in some way to generate a random password

#First method will be to create a list of all characters possible and ask the user for a length they want the password to be and they do no provide it, then it will be 8 by default

#I will try this out later tonight