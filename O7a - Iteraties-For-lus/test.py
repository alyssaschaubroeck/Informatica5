#for i in range(350):
    #print('beep, beep, papier komt uit printer, beep, stop')
#regeltjescode die herhaalt wordt
#range (350) = collectie= 0 tot 349

#fruit = input('Lievelingsfruit? ')
#m = ' m'
#for letter in fruit:
    #print(letter + m)
    #m += 'm'
#collectie kun je opvragen

#for i in range(10):
    #print(i)
#range(10) geef je 10 getallen

#for _ in range(9, 11, 1):
    #print('k')
# 1 is optioneel
# i mag ook _ als niet gebruikt wordt
# i is een teller

woord = input('woord: ')

klinkers, medeklinkers = 0, 0

for letter in woord:
    if letter in 'aeoui':
    # if letter == 'a', or letter == ...
        klinkers += 1
    else:
        medeklinkers += 1

print('kl: {}\n\tmkl: {}'.format(klinkers, medeklinkers))
#\n = new line
#\t = een tab

