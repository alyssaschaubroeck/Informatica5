woord = input('Woord: ')
gedraaide_bedrag = int(input('Bedrag: '))
bedrag = 0
letter = input('Letter: ')

while letter in woord:
    letter = input('Letter: ')
    bedrag += gedraaide_bedrag


else:
    bedrag == 0

print(bedrag)
