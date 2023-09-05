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


runden = int(input("Wie viele Runden möchten Sie spielen? "))
for _ in range(runden):
    spiele_slot_maschine()

print("Das Spiel ist beendet. Ihr endgültiger Punktestand:", punkte)



