#bestand = open('Klas.txt')

#lijn = bestand.readline()

#while lijn != '':
    #print(lijn)
    #lijn = bestand.readline()

#bestand.close()

# lijnen = []
#
# with open('Klas.txt') as bestand:
#     lijnen = bestand.readlines()

#for naam in lijnen:
    #print(naam[::-1])

# print('Er zitten ' + str(len(lijnen)) + ' personen in de klas.')

# nieuwe_leerlingen = ['Alice', 'Baptiste']
#
# with open('Klas.txt', 'a') as bestand:
#     bestand.write('\n' + '\n'.join(nieuwe_leerlingen))

#w in plaats van a is write, en r is lees

nieuwe_leerlingen = ['Alice\n', 'Baptiste']

with open('Klas.txt', 'w') as bestand:
    bestand.write(nieuwe_leerlingen)
