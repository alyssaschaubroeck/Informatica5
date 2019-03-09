def verlaat_ploeg(verlaten, ploeg, totaal):
    if len(totaal[ploeg]) > 1:
        totaal[ploeg].remove(verlaten)
    else:
        totaal.pop(ploeg)
    return totaal

def vervoegt_ploeg(toegevoegd, ploeg, totaal):
    if ploeg in totaal:
        totaal[ploeg].append(toegevoegd)
    else:
        totaal[ploeg] = [toegevoegd]
    return totaal

print( verlaat_ploeg('Tom','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))