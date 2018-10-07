from math import sqrt

#input
a = float(input('a: '))
b = float(input('b: '))

#bewerking
c = sqrt((a ** 2) + (b ** 2))

uitkomst = 'In een rechthoekige driehoek met rechthoekszijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'.format(a, b, c)

print(uitkomst)