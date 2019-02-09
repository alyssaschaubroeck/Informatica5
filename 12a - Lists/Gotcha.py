def ik_heb_gemoord(lijst, uitvoerder):
    opdracht = []
    nummer = lijst.index(uitvoerder)
    if len(lijst) == 1:
        opdracht = lijst[0]
    elif len(lijst) > 1:
        if nummer + 1 < len(lijst):
            lijst.pop(nummer + 1)
        else:
            lijst.pop(0)

        if nummer + 1 < len(lijst):
            opdracht = lijst[nummer + 1]
        else:
            opdracht = lijst[0]
    return opdracht, lijst

def ik_ben_vermoord(opdrachtenlijst, slachtoffer):


print(ik_heb_gemoord(['jan', 'piet', 'joris', 'korneel'],'joris'))