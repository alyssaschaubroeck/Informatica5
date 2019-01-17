def is_palindroom(woord):
    uitk = True
    if len(woord) == 1:
        uitk = True
    else:
        for i in range(0, len(woord)//2):
            if woord[i] == woord[len(woord)-1-i] and uitk != False:
                uitk = True
            else:
                uitk = False
    return uitk

print(is_palindroom('tarwerat'))

