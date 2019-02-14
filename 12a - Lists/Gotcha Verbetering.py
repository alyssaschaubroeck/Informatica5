def ik_heb_gemoord(lijst, moordenaar):
    #slachtoffer schrappen
    index_moordenaar = lijst.index(moordenaar)
    index_slachtoffer = (index_moordenaar + 1) % len(lijst)
    #index_slachtoffer = (lijst.index(moordenaar) + 1) % len(lijst)
    # modulo = de rest na deling door lengte lijst
    lijst[index_slachtoffer: index_slachtoffer + 1] = []

    #nieuw doel aan de moordenaar geven
    index_moordenaar = lijst.index(moordenaar)
    index_nieuw_doel = (index_moordenaar + 1) % len(lijst)

    return lijst, lijst[index_nieuw_doel]

