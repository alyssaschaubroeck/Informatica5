from math import sqrt
def binnen_of_buiten(m, c, co):
    x1, y1 = m
    x2, y2 = c
    x3, y3 = co

    #straal: d(m,c)
    r = sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

    #punt: d(m,co)
    punt = sqrt(((x1 - x3)**2) + ((y1 - y3)**2))

    if r == punt:
        antw = 'op'

    elif r < punt:
        antw = 'buiten'

    else:
        antw = 'binnen'

    return antw, round(punt, 4)

print(binnen_of_buiten((7, -1),(-9, -32),(12, -48)))
