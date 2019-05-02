def vergeten_woorden(tekst, verplicht):
    woorden = set(tekst.split())
    verplichte_woorden = len(verplicht)
    gebruikte_woorden = woorden.intersection(verplicht)
    # vergeten_woorden = verplichte_woorden - len(gebruikte_woorden)
    vergeten_woorden = verplicht.difference(woorden)
    return (verplichte_woorden, vergeten_woorden, len(gebruikte_woorden))

print(vergeten_woorden('hello world world world',{'python', 'world', 'hello', 'java'}))