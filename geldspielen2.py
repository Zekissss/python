import random

symbole = ['✿', '☻', '♛', '☼', '・❥・', '🌟', '💖', '💜', '💚', '💙']
punkte = 0

def spiele_slot_maschine():
    global punkte
    
    ergebnisse = [random.choice(symbole) for _ in range(3)]
    print("Ergebnisse:", ergebnisse)
    
    if ergebnisse[0] == ergebnisse[1] == ergebnisse[2]:
        punkte += 1000
        print("Glückwunsch! Sie haben 1000 Punkte gewonnen!")
    elif ergebnisse[0] == ergebnisse[1] or ergebnisse[0] == ergebnisse[2] or ergebnisse[1] == ergebnisse[2]:
        punkte += 50
        print("Glückwunsch! Sie haben 50 Punkte gewonnen!")
    else:
        punkte -= 10
        print("Es tut mir leid! Sie haben 10 Punkte verloren.")
    
    print("Ihr aktueller Punktestand:", punkte)


while True:
    
    
    choice = input("Möchten Sie fortfahren? (Ja/Nein): ")
    choice = choice.lower()
    if choice == "ja":
        spiele_slot_maschine()    
    elif choice == "nein":
        break
    else:
        print("Ungültige Eingabe! Bitte geben Sie 'Ja' oder 'Nein' ein.")
        continue



