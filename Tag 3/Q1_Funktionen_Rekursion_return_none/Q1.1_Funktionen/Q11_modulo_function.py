def strange_function_none(n):
    if n % 2 == 0:  # Prüft, ob n ohne Rest durch 2 teilbar ist
        return True
    
print(strange_function_none(2))
print(strange_function_none(1))
#--------------------------------------------------------------------------------------------------------

import webbrowser  # Modul zum Öffnen von Webseiten

def strange_function(n):
    if n % 2 == 0:  # Prüft, ob n ohne Rest durch 2 teilbar ist
        print("Modulo 0 erkannt – starte Musik 🎵")
        webbrowser.open("https://www.youtube.com/watch?v=-O8Y9X2Z2fA")
        return True

# Beispielaufrufe
strange_function(4)  # Öffnet YouTube
strange_function(5)  # Gibt nur Text aus

#--------------------------------------------------------------------------------------------------------
