x = 'x'
fx = '2(x - 3)^2 + 4'

#invoer
a = float(input('a = '))
b = float(input('b = '))

#berekening
gx = '2' + '(x - ' + str(int( 3 + a)) + ')^2 + ' + str(int(+4+b))


#uitvoer
resultaat = str(gx)

print('f(x) = ' + fx)
print('g(x) = ' + gx)