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
    except KeyboardInterrupt:
        print("wurde abgefangen")
        break
