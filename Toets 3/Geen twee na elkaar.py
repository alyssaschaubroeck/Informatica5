def ontdubbelen(woord):
    for i in range(1, len(woord) - 2):
        if woord[i] == woord[i-1]:
            woord = woord[:i-1] + woord[i:]
    return woord

print(ontdubbelen('grootte'))