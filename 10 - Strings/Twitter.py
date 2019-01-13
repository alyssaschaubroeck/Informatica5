# invoer
tweet = str(input('Tweet: '))
antw = ''

#bewerkingen
for i in range(0, len(tweet)):
    if tweet[i] == '#':
        b = tweet[i:].find(' ')
        if (b + i) > i:
            antw = tweet[i + 1:i + b]
            print(antw)


