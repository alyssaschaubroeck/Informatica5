def verzamel(aangekocht, stickerboek, dubbels):
    if {aangekocht}.issubset(stickerboek) is True:
        if {aangekocht} in dubbels.values():
            dubbels[aangekocht]
        else:
            dubbels[1] = {aangekocht}
    else:
        stickerboek.add(aangekocht)
    return (stickerboek, dubbels)

print(verzamel('Bosmans',{'Weber', 'Bosmans'},{}))