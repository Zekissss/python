import tkinter as tk

fenster = tk.Tk()

fenster.title("Himmelsrichtung")

fenster.geometry("500x500")

fenster.configure(bg="orange")

himmelsrichtungen = ["Norden", "Süden", "Osten", "Westen"]
zwischenrichtungen = ["Nordosten", "Nordwesten", "Südosten", "Südwesten"]
mittel = ["Mittel"]


for richtung, x_position, y_position in [("Norden", 200, 50), ("Süden", 200, 350), ("Osten", 350, 200), ("Westen", 50, 200)]:
    label = tk.Label(fenster, text=richtung, bg="orange", fg="black")
    label.place(x=x_position, y=y_position)

for zwischenrichtung, x_position, y_position in [("Nordosten", 300, 100), ("Nordwesten", 100, 100), ("Südosten", 300, 300), ("Südwesten", 100, 300)]:
    zwischenrichtung_label = tk.Label(fenster, text=zwischenrichtung, bg="orange", fg="black")
    zwischenrichtung_label.place(x=x_position, y=y_position)

for center, x_position, y_position in [("Mittel", 200, 200)]:
    center_label = tk.Label(fenster, text=center, bg="orange", fg="black")
    center_label.place(x=x_position, y=y_position)


fenster.mainloop()
