verliezer = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

#input
dobbel_a1 = int(input('De eerste dobbelsteen van de aanvaller: '))
dobbel_a2 = int(input('De tweede dobbelsteen van de aanvaller: '))
dobbel_a3 = int(input('De derde dobbelsteen van de aanvaller: '))
dobbel_v1 = int(input('De eerste dobbelesteen van de verdediger: '))
dobbel_v2 = int(input('De tweede dobbelsteen van de verdediger: '))

#berekening
if dobbel_a1 > dobbel_v1:
    if dobbel_a2 > dobbel_v2:
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    else:
        print(verliezer)
elif dobbel_a1 < dobbel_v1:
    if dobbel_a2 < dobbel_v2:
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    else:
        print(verliezer)
else: print(verliezer)