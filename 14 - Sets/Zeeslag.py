def boot_overlappend(nieuw, boten):
    return not nieuw.isdisjoint(boten)

def boot_toevoegen(nieuw, boten):


print(boot_overlappend({'B4', 'A4', 'C4'},{'C4', 'D4', 'E4', 'A2', 'I8', 'F8', 'H8', 'A3', 'G8'}))