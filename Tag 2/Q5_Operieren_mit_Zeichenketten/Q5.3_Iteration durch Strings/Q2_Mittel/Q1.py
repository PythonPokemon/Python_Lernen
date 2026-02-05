""" 
Iteration durch Strings (Zeichenweise durchgehen)
mit slicing [start:stop:step]
"""

name = "Anna"   # in der veraiable 'name' wird eine Zeichenkette "Anna" gespeichert

for buchstabe in name[0:3:1]:  # in der platzhalter variable 'buchstabe' werden die Werte während der Iteration zwischengespeichert die, 
                        # die referenzvariable 'name' durchgehen
    print(buchstabe)    # Ausgabe jedes einzelnen wertes die in der Platzhaltervariable 'buchstabe' zwischen gespeichert wurden
