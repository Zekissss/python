


boy = int(input("boyunuzu girin:" ))
kilo = int(input("kilonuzu girin:" ))

boy = (boy **2)/10000
indeks = kilo/boy

if indeks <= 16.0:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: starkes Untergewicht")
elif 16.0 < indeks <= 17.0:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: maßiges Untergewicht")
elif 17.0 < indeks <= 18.5:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: leichtes Untergewicht")
elif 18.5 < indeks <= 25.0:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: Normalgewicht")
elif 25.0 < indeks <= 30.0:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: Praadipositas")
elif 30.0 < indeks <= 35.0:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: Adipositas Grag I")
elif 35.0 < indeks <= 40.0:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: Adipositas Grag II")
else:
    print("Vücut kitle indeksiniz: ", indeks, "Kategorie: Adipositas Grag III")
