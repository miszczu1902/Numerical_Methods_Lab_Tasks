def horner(wartosc, wsp, len):
    wynik = wsp[0]
    # if len == 1:
    #     wynik *= wartosc
    # else:
    for i in range(1, len):
        wynik = wynik * wartosc + wsp[i]

    return wynik
