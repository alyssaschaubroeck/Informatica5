def dubbels(lijst):

    dubbel = []

    for item in lijst:

        if lijst.count(item) > 1 and item not in dubbel:

            dubbel.append(item)

    return dubbel

print(dubbels([(0, 1), 'joris', 4, 'korneel', (1, -1), 1, 1, 'piet', 4, 'joris']))