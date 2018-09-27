k = 8.99 * (10 ** 9)
q1 = 1.0 * (10 ** -6)
q2 = 2.0 * (10 ** -6)

#invoer
r = float(input('Straal is: '))
r *= 10**-2

#berekening
fc = k * ((q1 * q2) / (r ** 2))

#uitvoer
resultaat = str(fc)

print(resultaat)