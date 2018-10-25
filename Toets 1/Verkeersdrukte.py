#input
d_vracht = float(input('d vrachtvervoer: '))
v_vracht = int(input('v vrachtverkeer: '))
d_persoon = float(input('d personenvervoer: '))
v_persoon = int(input('v personenwagens: '))

#bewerking
pv = min(((v_vracht * d_vracht) / 40), 1)
pa = min(((v_persoon * d_persoon) / 40), 1)
min = min(pv, pa)
max = max(pv, pa)
verschil = max - min

#kleur bepalen
if min > 0.7:
    antw = 'zwart'
elif max > 0.7 and verschil < 0.2:
    antw = 'rood'
elif verschil > 0.7:
    antw = 'geel'
else:
    antw = 'groen'

#output
print(antw)