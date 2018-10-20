hendel_trekken = input('Trek aan de hendel van de wissel? (ja/nee) ')
man_duwen = input('Man van de brug duwen? (ja/nee) ')


if hendel_trekken == 'ja' and man_duwen == 'ja':
    doden = 2
elif hendel_trekken == 'nee' and man_duwen == 'nee':
    doden = 5
else:
    doden = 1

print(doden)

#moeilijkste naar else verschuiven
# elif (hendel_trekken == 'nee' and man_duwen == 'ja') or (hendel_trekken == 'ja' and man_duwen == 'nee')
# elif hendel_trekken != mand_duwen :