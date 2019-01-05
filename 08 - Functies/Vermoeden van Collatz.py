#volgend collatz getal
def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend = n // 2
    else:
        volgend = (n * 3) + 1
    return volgend

#cyclelengte
def collatz(n):
    lengte = 1
    if n == 1:
        lengte = 1
    else:
        while volgend_collatz_getal(n) != 1:
            lengte += 1
            n = volgend_collatz_getal(n)
        if volgend_collatz_getal(n) == 1:
            lengte += 1
    return lengte