#invoer
t = float(input('T is '))
w = float(input('W is '))

#berekening
gevoelstemperatuur = 13.12 + (0.6215 * t) + (((0.3965 * t) - 11.37) * ((3.6 * w) ** 0.16))

print(gevoelstemperatuur)