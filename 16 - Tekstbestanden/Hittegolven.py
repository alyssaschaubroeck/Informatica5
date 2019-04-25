def to_int_temp(lijn):
    int_lijn = []
    lijn = lijnen[1].split()

    for t in lijn:
        int_lijn.append(int(t))

    return int_lijn

lijnen = []

with open('temperaturen.txt') as bestand:
    lijnen = bestand.readlines()

dag = 0
aantal_25_plus = 0
aantal_30_plus = 0
hittegolven = []

for lijn in lijnen:
    temp = to_int_temp(lijn)

    for i in range(len(temp)):

        #hoger dan 30
        if temp[i] >= 30:
            aantal_30_plus += 1
            aantal_25_plus += 1

        #hoger dan 2(
        elif temp[i] >= 25:
            aantal_25_plus += 1

        #lager dan 25
        else:
            if aantal_25_plus >= 5 and aantal_30_plus >= 3:
            #was vorige periode hittegolg --> ja sla op
                hittegolven.append((dag - aantal_25_plus, dag-1))
            #periode op nul zetten
            aantal_30_plus = 0
            aantal_25_plus = 0
    dag += 1
print(hittegolven)
