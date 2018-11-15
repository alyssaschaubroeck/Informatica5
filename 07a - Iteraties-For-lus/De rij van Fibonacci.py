#input
n = int(input('Hoeveelste getal van Fibonacci: '))

#denkwerk: weten wat vorige en huidige is en dan kan je volgende berekenen
#vorige = 1
#huidige = 1
vorige, huidige = 1, 1

#denkwerk: wat zal het nieuwe huidige en nieuwe vorige zijn
#for i in range(n-2):
    #hulp = vorige
    #vorige = huidige
    #huidige = huidige + hulp
    #print(vorige, huidige)

for i in range(n-2):
    vorige, huidige = huidige, huidige + vorige

print(huidige)

