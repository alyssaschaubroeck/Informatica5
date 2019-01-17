tweet = input('geef tweet: ')

i_hashtag = tweet.find('#')
#dat is zolang er geen gevonden zijn)

while i_hashtag != -1:

    #tweet afknippen net na het #-teken
    tweet = tweet[i_hashtag + 1:]
    i_spatie = tweet.find(' ')

    #hahstag uitknippen en printen
    print(tweet[:i_spatie]) #moet niet min 1 want laatste rekent het niet meer mee
    #tweet inkorten is niet meer nodig
    #terug op zoekn naar een # gaan
    i_hashtag = tweet.find('#')


