x = int(input('Geef een geheel getal: '))

if x % 2 == 0: # kan heel lang worden
    print(x, 'is een even getal') # 1 tab ingesprongen dan moet het voldoen worden

print('tot ziens!') # hier tab gebruikt dan bij even getal niets meer
# zonder tab doet hij het altijd

# andere oefening
x = int(input('Geef een geheel getal: '))

if x % 2 == 0: # als
 print(x,'is een veelvoud van 2')

elif x % 3 == 0: # als anders
 print(x, 'is een veelvoud van 3')

else: # anders
 print(x, 'is geen veelvoud van 2 of 3')

 # met elif: eerste blokje uitvoeren dus het eerste blokje dat waar is wordt uitgevoerd
 # als de elif if wordt dan doet hij wel beide


# andere oefening
leeftijd = int(input('leeftijd: '))

if leeftijd > 21:
    print('Drink met mate.')
elif leeftijd > 16:
    print('Wel pintje, geen sterke drank')
else:
    print('Alcohol verboden!')
# let op logisch denken, van oud naar jonger hier
