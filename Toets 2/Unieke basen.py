#input
aantal_basen = int(input('Aantal basen: '))
soorten = ''
aantal_soorten = 0

#bewerking
for i in range(aantal_basen):
    base = input('Base: ')
    if base not in soorten:
        soorten += str(base) + ' '
        aantal_soorten += 1

if aantal_soorten == 1:
    antw = 'De DNA-keting bevat {} soort base: {}'.format(aantal_soorten, soorten)
if aantal_soorten > 1:
    antw = 'De DNA-keting bevat {} verschillende soorten basen: {}'.format(aantal_soorten, soorten)

print(antw)
