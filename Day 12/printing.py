

def printing(unprinted, printed):
    """printing models"""
    while unprinted:
        done = unprinted.pop()
        print(f"Printing {done}")
        printed.append(done)
    print(f"unprinted: {unprinted}")
    print(f"printed: {printed}")


