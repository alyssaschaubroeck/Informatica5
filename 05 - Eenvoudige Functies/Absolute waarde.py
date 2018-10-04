# input
x = float(input('x: '))
y = float(input('y: '))

# bewerking
rechter_lid = abs(abs(x)- abs(y))
linker_lid = abs(x-y)

print('{:.4f} ≤ {:.4f}'.format(linker_lid, rechter_lid))