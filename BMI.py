


Körpergröße = float(input("Geben Sie Ihre Körpergröße ein (cm):" ))
Gewicht = int(input("Geben Sie Ihr Gewicht ein:" ))

## Körpergröße = (Körpergröße**2)/10000
index = Gewicht/(Körpergröße**2)

if index <= 16.0:
    print("Ihr Body Mass Index: ", index, "Kategorie: starkes Untergewicht")
elif 16.0 < index <= 17.0:
    print("Ihr Body-Mass-Index: ", index, "Kategorie: maßiges Untergewicht")
elif 17.0 < index <= 18.5:
    print("Ihr Body-Mass-Index: ", index, "Kategorie: leichtes Untergewicht")
elif 18.5 < index <= 25.0:
    print("Ihr Body-Mass-Index: ", index, "Kategorie: Normalgewicht")
elif 25.0 < index <= 30.0:
    print("Ihr Body-Mass-Index: ", index, "Kategorie: Praadipositas")
elif 30.0 < index <= 35.0:
    print("Ihr Body-Mass-Index: ", index, "Kategorie: Adipositas Grag I")
elif 35.0 < index <= 40.0:
    print("Ihr Body-Mass-Index: ", index, "Kategorie: Adipositas Grag II")
else:
    print("Ihr Körpermassenindex: ", index, "Kategorie: Adipositas Grag III")