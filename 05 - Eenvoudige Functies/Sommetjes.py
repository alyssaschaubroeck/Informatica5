#input
a = float(input('Getal a is '))
b = float(input('Getal b is '))

i = 0
berekening = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((10 ** i) * a, (10 ** i) * b, (10 ** i) * a  + (10 ** i) * b)

i = 1
berekening_2 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((10 ** i) * a, (10 ** i) * b, (10 ** i) * a  + (10 ** i) * b)

i = 2
berekening_3 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((10 ** i) * a, (10 ** i) * b, (10 ** i) * a  + (10 ** i) * b)

i = 3
berekening_4 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((10 ** i) * a, (10 ** i) * b, (10 ** i) * a  + (10 ** i) * b)

i = 4
berekening_5 = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format((10 ** i) * a, (10 ** i) * b, (10 ** i) * a  + (10 ** i) * b)

print(berekening)
print(berekening_2)
print(berekening_3)
print(berekening_4)
print(berekening_5)