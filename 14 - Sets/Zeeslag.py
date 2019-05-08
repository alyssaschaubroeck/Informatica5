def boot_overlappend(nieuw, boten):
    return not nieuw.isdisjoint(boten)

def boot_toevoegen(nieuw, boten):
    if boot_overlappend(nieuw, boten) is False:
        resultaat = boten.union(nieuw)
    else:
        resultaat = boten
    return resultaat

def vuur(gok, boten):
    if boot_overlappend({gok}, boten) is True:
        boten.discard(gok)
        antwoord = True
    else:
        antwoord = False
    return (antwoord, boten)

