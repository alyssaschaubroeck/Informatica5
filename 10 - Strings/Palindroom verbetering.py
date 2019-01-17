#je moet eigenlijk niet het volledige woord overlopen
#controleren tot je een verschil tegenkomt
def palindroom(woord):
    i = 0
    while woord[i] == woord[-i - 1] and i < len(woord) // 2:
        i += 1

    return i == (len(woord) // 2)

print(palindroom('keak'))

#of return woord == woord[::-1]