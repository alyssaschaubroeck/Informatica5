def doe_maar_gewoon(woord):
    for i in range(0, len(woord)-2):
        if woord[i].lower() == woord[i+1]:
            woord = woord[:i] + woord[i].lower() + woord[i+1:]
    return woord

print(doe_maar_gewoon('stresSsymptOom'))