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
sented = []

def sendmessages(lists, sent):
    """Send messages"""
    while lists:
        gone = lists.pop()
        print(f"Sending message: {gone}")
        sent.append(gone)

    print(dalist)
    print(sent)

sendmessages(dalist, sented)


#Archived messages: Do the same thing as above but with a copy of the list:
sendmessages(dalist[:], sented)
