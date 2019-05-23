from random import randint

def bubble_sort(rij):
    for i in range(0, len(rij) - 1):
        for j in range(len(rij) - 1, i, -1):
            if rij[j] < rij[j - 1]:
                rij[j], rij[j - 1] = rij[j - 1], rij[j]
        print(rij)
    return rij

def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij

rij = genereer_rij(10)
print(bubble_sort(rij))
