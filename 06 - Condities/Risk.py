#input
a = int(input('De eerste dobbelsteen van de aanvaller: '))
b = int(input('De tweede dobbelsteen van de aanvaller: '))
c = int(input('De derde dobbelsteen van de aanvaller: '))
d = int(input('De eerste dobbelesteen van de verdediger: '))
e = int(input('De tweede dobbelsteen van de verdediger: '))

#sorteren
sa = max(a, max(b, c))
#sa = max (a, b, c)
sc = min(a, b, c)
sb = a + b + c - sa - sc
#print(sa, sb) = controleren
sd = max(d, e)
se = min(d, e)
#print(sd, se)
#winnar bepalen

if sa > sd:
    if sb > min(d, e) and sb > se:
        mes = 'aanvaller verliest 0 legers, verdediger verliest 2 legers'
elif sd >= sa and se >= sb:
    mes = 'aanvaller verliest 2 legers, verdediger verliest 0 legers'
else:
    mes = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

#uitvoer
print(mes)