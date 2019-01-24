def ontdubbelen(woord):

    nieuw_woord = woord[0]

    for i in range(1, len(woord)):

        if woord[i] != woord[i - 1]:
            nieuw_woord += woord[i]

    return nieuw_woord