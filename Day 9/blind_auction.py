import auction_art as aa

print(f'{aa.logo}\nWelcome to the blind Auction')

adding = True
bids = {}

def add_bids(name, bid):
    bids[name] = bid

def winner(bids):
    winner = ''
    winning_bid = 0
    for bidder in bids:
        if bids[bidder] > winning_bid:
            winner = bidder
            winning_bid = bids[bidder]
    print(f'The winner of the auciton is {winner.title()} with a bid of ${winning_bid}')

    
while adding:
    name = input('What is your name:\n')
    bid = int(input('What is your bid:\n$'))
    add_bids(name, bid)
    another = input('Is there anther bidder? Y/N\n')
    if another.lower() == 'n':
        winner(bids)
        adding = False













