getal = int(input('getal: '))

#zolang je het niet kan delen door 2, 3, 4 is het allicht een priemgetal
#ergens 2, 3, 4 bijhouden

deler = 2

#zolang ... != verschillend
#while getal % deler != 0 and getal != 1:
#while getal / deler != getal // deler:
# eigenlijk testen tot wortel van het getal
while getal % deler != 0 and getal != 1:
    deler += 1

#wanneer stopt die lus?
#tussendoor print(deler)
#als deler  gelijk is aan getal dan

if deler == getal:
    print('priemgetal')
else:
    print('geen priemgetal')

#als je 1 ingeeft blijft het doorgaan dus and
#tussendoor mes =  en dan vanonder print(mes)