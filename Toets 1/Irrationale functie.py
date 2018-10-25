from math import sqrt

#invoer
a = float(input('x: '))

#oplossing
if a < 2:
    antw = '{:.2f} ∉ dom(f)'.format(a)
elif sqrt(a-2) == 0:
    antw = '{:.2f} is nulpunt van f'.format(a)
else:
    antw = 'f({:.2f}) = {:.2f}'.format(a, sqrt(a-2))

#output
print(antw)