def vlag(richting, kleuren):
    if richting == 'verticaal' and len(kleuren) == 3:
        antw = kleuren[0] + ' | ' + kleuren[1] + ' | ' + kleuren[2]
    elif richting == 'verticaal' and len(kleuren) == 2:
        antw = kleuren[0] + ' | ' + kleuren[1]
    elif richting == 'horizontaal' and len(kleuren) == 3:
        antw = kleuren[0] + ''