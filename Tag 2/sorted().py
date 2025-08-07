""" 
Beispiel: sorted() - Gibt eine neue sortierte Liste zurück (Original bleibt erhalten)
"""

def neue_sortierte_liste_erstellen():
    namen = ["Lena", "Ben", "Anna", "Tom"]
    sortierte_namen = sorted(namen)  # <--- erstellt neue Liste

    print("Original:", namen)
    print("Sortiert:", sortierte_namen)

neue_sortierte_liste_erstellen()
