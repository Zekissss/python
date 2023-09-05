def berechne_bonus(verkaufe):
    gesamt_verkaufe = sum(verkaufe)
    durchschnittliche_monatliche_verkaufe = gesamt_verkaufe / 12
    durchschnittliche_quartals_verkaufe = gesamt_verkaufe / 4

    if any(verkauf < 0.7 * durchschnittliche_monatliche_verkaufe for verkauf in verkaufe):
        bonus_prozentsatz = 1.8
    elif any(quartals_verkauf < 0.9 * durchschnittliche_quartals_verkaufe for quartals_verkauf in quartals_verkaufe):
        if gesamt_verkaufe < 18000:
            bonus_prozentsatz = 2
        elif gesamt_verkaufe < 20000:
            bonus_prozentsatz = 4
        else:
            bonus_prozentsatz = 5.5
    else:
        if gesamt_verkaufe < 18000:
            bonus_prozentsatz = 3
        elif gesamt_verkaufe < 20000:
            bonus_prozentsatz = 5
        else:
            bonus_prozentsatz = 6.5
    
    bonus = gesamt_verkaufe * (bonus_prozentsatz / 100)
    return bonus_prozentsatz, bonus

def verkaufe_eingeben():
    verkaufe = []
    for monat in range(1, 13):
        while True:
            try:
                monatlicher_verkauf = float(input(f"Geben Sie den Verkauf für den Monat {monat} ein: "))
                verkaufe.append(monatlicher_verkauf)
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie einen gültigen Verkaufsbetrag ein.")
    return verkaufe

def main_funktion():
    print("Geben Sie die Verkaufe für jeden Monat ein:")
    verkaufe = verkaufe_eingeben()
    
    quartals_verkaufe = [sum(verkaufe[i:i+3]) for i in range(0, len(verkaufe), 3)]
    
    bonus_prozentsatz, bonus = berechne_bonus(verkaufe)
    
    print(f"\nTotal Verkaufe: {sum(verkaufe)} €")
    print(f"Quartalsverkaufe: {quartals_verkaufe}")
    print(f"\nBonus Prozentsatz: {bonus_prozentsatz} %")
    print(f"Bonus Betrag: {round(bonus, 2)} €")

main_funktion()

