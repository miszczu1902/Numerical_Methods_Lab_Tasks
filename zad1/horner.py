def horner(wartosc, wsp, len):
    wynik = wsp[0]
    print(wartosc,"wsp",wsp,len)
    for i in range(1, len):

        wynik = wynik * wartosc + wsp[i]

    return wynik
