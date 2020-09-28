#Day 11 of Code

### Blocks printed with hyphens between are seperate lessons and will have comments for what is covered in the space ###

###--Users input, manipulating user input, loops with user input, storing user input--###

#Album: functions make_album builds a dictionary describing music album. Takes in artist and an albun returning rhose 2 pieces of information. Call 3x

def artist_album(artist, album):
    """Returns artist and album"""
    info = {'Artistt': artist, 'Album': album}
    return info

jcole = artist_album('jcole', 'KOD')
drake = artist_album('drake', 'take care')
flobots = artist_album('flobots', 'platypus')

print(jcole)
print(drake)
print(flobots)

#User Albums: Use above code. Write while loop that allows user to enter artist and album. Call funtions and print

while True:
    artist = input("Give me an artist: ")
    album = input("Give me an album by that artist: ")
    user_input = artist_album(artist, album)
    print(user_input)
    again = input("Want to do that again? y/n:\n")
    if again.lower() == 'n':
        break

#Messaages: Function that takes in a list and returns every item in the list:
da_list =['a','b','c','d']
def in_list(lists):
    """Prints everything in list"""
    for item in lists:
        print(item)

in_list(da_list)

#sending messages: function sendmessages()

dalist = ['a','b','c','d']
sent = []

def sendmessages(lists):
    """Send messages"""
    for message in lists:
        print(f"Sending message: {message}")
        removed = lists.pop()
        sent.append(removed)

    print(lists)
    print(sent)

sendmessages(dalist)

#Mmodel above code from the code in previous practice:

# #This is an emepty list to append to while we remove items list argument
# sent_messages = []
# #This is the list of strings that we will be pulling from.
# text = ['I like pie', 'I only wish I could have some red velvet cake',
#         'I am not good at warzone']

# def show_messages(messages):
#     """Prints all the messages in a list"""
#     print(messages)
#     print("Printing messsages:")

#     #Used while instead of for loop because the for loop will pop the items and then leave us with 2 items printed at the end 
#     while messages:
#         removed = messages.pop()
#         print(f"{removed}")
#         sent_messages.append(removed)

#     print("\n")
#     print(sent_messages)
#     print("All messsages printed!")



# show_messages(text)




#Archived messages: Do the same thing as above but with a copy of the list:
sendmessages(dalist[:])
