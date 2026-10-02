"""
KeyboardInterrupt auslösen: Strg + c
in der Konsole
bps. Endlosschleife
"""




counter = 0

while True:
    try:
        counter +=1
        print(counter)
    except KeyboardInterrupt:           # Unterbricht die Entlosschleife in der Konsole!
        print("wurde abgefangen")
        break
