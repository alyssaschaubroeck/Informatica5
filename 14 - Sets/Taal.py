def behoort_tot_taal(bericht, taal):
    uitgesplit = set(bericht)
    uitgesplit.discard(' ')
    return uitgesplit.issubset(taal) and len(uitgesplit) > 0

def is_onleesbaar(bericht, taal):
    uitgesplit = set(bericht)
    uitgesplit.discard(' ')
    return uitgesplit.isdisjoint(taal)

def perfect_woord(bericht, taal):
    uitgesplit = set(bericht)
    uitgesplit.discard(' ')
    return taal.issubset(uitgesplit)


print(is_onleesbaar('ambigu',{'o', 'd', 'e', 'l', 'w', 'r', 'h'}))