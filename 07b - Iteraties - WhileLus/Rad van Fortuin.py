woord = input('Woord: ')
gedraaide_bedrag = int(input('Bedrag: '))
letter = input('Letter: ')
bedrag = 0
algemeen = ' '

while letter in woord and letter not in algemeen:
    bedrag += gedraaide_bedrag
    algemeen += letter
    letter = input('Letter: ')

if letter not in woord:
    bedrag == 0

print(bedrag)
