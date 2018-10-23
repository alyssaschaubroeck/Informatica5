verliezer = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

#input
a = int(input('De eerste dobbelsteen van de aanvaller: '))
b = int(input('De tweede dobbelsteen van de aanvaller: '))
c = int(input('De derde dobbelsteen van de aanvaller: '))
d = int(input('De eerste dobbelesteen van de verdediger: '))
e = int(input('De tweede dobbelsteen van de verdediger: '))

getal_2 = (a + b + c) - max(a, b, c) - min(a, b, c)

#berekening
if max(a, b, c) > max(d, e):
    if getal_2 > min(d, e):
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif getal_2 <= min(d, e):
        print(verliezer)
elif max(a, b, c) <= max(d, e):
    if getal_2 <= min(d, e):
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    elif getal_2 > min(d, e):
        print(verliezer)
