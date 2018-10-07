#input
a = float(input('Getal a is '))
b = float(input('Getal b is '))

i = 1

#berekening
linkerlid_1 = (10 ** i) * a
linkerlid_2 = (10 ** i) * b
rechterlid = (10 ** i) * a  + (10 ** i) * b


berekening = '{:>6.0f} + {:<6.0f} = {:<6.0f}'.format(linkerlid_1, linkerlid_2, rechterlid)

