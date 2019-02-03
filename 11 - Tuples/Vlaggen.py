def vlag(richting, kleuren):
    antw = ''
    for i in range(0, len(kleuren)):
        if richting == 'verticaal':
            antw += kleuren[i]
            if i != len(kleuren) - 1:
                antw += ' | '
        elif richting == 'horizontaal':
            antw += kleuren[i]
            if i != len(kleuren) - 1:
                antw += '\n' + '-' + '\n'
    return antw

print(vlag('horizontaal',('rood', 'wit', 'blauw')))