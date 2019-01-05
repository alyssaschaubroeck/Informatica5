#input
snelheid_s = int(input('De snelheid van Stijn (in m/s): '))
snelheid_k = int(input('De snelheid van Kaat (in m/s): '))
afstand = int(input('De afstand tussen beide huizen (in m): '))
tijdstip = 1

#bewerking
originele_som = snelheid_s + snelheid_k
som = snelheid_s + snelheid_k

while som < afstand and tijdstip < 100000:
    tijdstip += 1
    som += originele_som
    antw = tijdstip

if som == afstand:
    antw = tijdstip

besluit = 'Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(antw)

print(besluit)