#invoer
r_klein = float(input('De straal van de kleine cirkel: '))
r_groot = float(input('De straal van de grote cirkel: '))

#berekening
n = (0.83 * (r_groot ** 2) / (r_klein ** 2)) - 1.9

#uitvoer
uitkomst ='{:f} kleine cirkels bedekken {:.2f}% van de grote cirkel'.format(r_klein, n)

print(uitkomst)