def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend = n // 2
    else:
        volgend = (n * 3) + 1
    return volgend

def collatz(n):
    if volgend_collatz_getal(n) != 1:




#bij dodana print niet meer ingeven
#geen input meer en geen print meer in pycharm
#zolang het volgende getal niet 1 is, zoek het volgende getal
#dus while lus vragen aan volgende getal