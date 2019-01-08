def splits(getal):
    g1 = getal // 1000
    g2 = (getal - (1000 * g1)) // 100
    g3 = (getal - (1000 * g1) - (100 * g2)) // 10
    g4 = (getal - (1000 * g1) - (100 * g2) - (10 * g3))
    return g1, g2, g3, g4

def oplopende_cijfers(a, b, c, d):
    getal_1 = min(a, b, c, d)
    getal_4 = max(a, b, c, d)
    getal_2 = max(min(a, b, c), min(a, b, d), min(a, c, d), min(b, c, d))
    getal_3 = min(max(a, b, c), max(a, b, d), max(a, c, d), max(b, c, d))
    return getal_1, getal_2, getal_3, getal_4

def op_af_getallen(e, f, g, h):
    op, af = '', ''
    op += str(e) + str(f) + str(g) + str(h)
    af += str(h) + str(g) + str(f) + str(e)
    return op, af

def verschil(op, af):
    verschil = op - af
    antw = '{} - {} = {}'.format(op, af, verschil)
    return antw





