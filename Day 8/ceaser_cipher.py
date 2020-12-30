
#Creating the caesar cipher

import art as a


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(f'{a.logo}')


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    if shift > 26:
        shift = shift % 25

    cipher_text = ''
    if direction == 'encode':
        for letter in text:
            if letter == ' ':
                cipher_text += letter
            else:
                location = alphabet.index(letter) + shift
                cipher_text += alphabet[location]
            
    elif direction == 'decode':
        for letter in text:
            if letter == ' ':
                cipher_text += letter
            else:
                location = alphabet.index(letter) - shift
                cipher_text += alphabet[location]

    print(cipher_text)


keep_going = True

while keep_going:
    if direction.lower() == 'encode':
        caesar(text, shift, direction = 'encode')
    elif direction.lower() == 'decode':
        caesar(text, shift, direction = 'decode')
    again = input('Want to continue? Y/N\n')
    if again.lower() == 'n':
        keep_going == False 
        print('Good Bye')
