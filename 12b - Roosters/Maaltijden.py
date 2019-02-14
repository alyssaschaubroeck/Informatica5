def maaltijdprijs(maaltijdtype, aantal):

    maaltijdprijs = 0

    if maaltijdtype == 'middagmaal':
        maaltijdprijs = aantal * 5.3
    elif maaltijdtype == 'soep':
        maaltijdprijs = aantal * 1.7
    elif maaltijdtype == 'vieruurtje':
        maaltijdprijs = aantal * 2.3

    return maaltijdprijs

def dagprijs(bestelling):
    dagprijs = 0
    for i in range(0, len(bestelling), 2):
        dagprijs += maaltijdprijs(bestelling[i], bestelling[i + 1])
    return dagprijs

def weekprijs(lijst):
    weekprijs = 0
    for dag in lijst:
        weekprijs += dagprijs(dag)
    return weekprijs
print(dagprijs(('middagmaal', 2, 'soep', 2, 'vieruurtje', 2)))