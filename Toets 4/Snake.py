def beweeg(begin, richting):
    x, y = begin
    if richting == '<':
        x += -1
    if richting == '>':
        x += 1
    if richting == 'v':
        y += -1
    if richting == '^':
        y += 1
    return x, y

def teruggekeerd(lijst):
    if lijst[0] == '^' and lijst[1] == 'v':
        antw = True
    elif lijst[0] == 'v' and lijst[1] == '^':
        antw = True
    elif lijst[0] == '>' and lijst[1] == '<':
        antw = True
    elif lijst[0] == '<' and lijst[1] == '>':
        antw = True
    else:
        antw = False
    return antw

def laatste_levende_positie(pijlen):
    i, x, y = 1, 0, 0
    x, y = beweeg((x, y), pijlen[0])
    
    while  i < len(pijlen) and not teruggekeerd([pijlen[i - 1], pijlen[i]]):
        x, y = beweeg((x, y), pijlen[i])
        i += 1

    return i, x, y

print(laatste_levende_positie(['v', '>', 'v', '<', '^', '^']))