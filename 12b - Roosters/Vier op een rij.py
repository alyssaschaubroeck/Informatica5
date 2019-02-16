def printbaar_rek(lijst):
    rek = ''
    for i in range(1, len(lijst[-1])):
        for b in range((len(lijst[-i]))):
            rek += lijst[-i][b]
        if i < len(lijst):
            rek += '\n'
    return rek

def speel(kleur, kolom, rek):
    i = 0
    while rek[i][kolom] != 'O' and i in range(len(rek)):
        i += 1
    if rek[i][kolom] == 'O':
        rek[i][kolom] = kleur
    return rek


print(speel('G',3,[['R', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]))