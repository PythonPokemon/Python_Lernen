# Schleifen – for, while, break, continue

# for-Schleife: Zähle von 0 bis 4
for i in range(5):
    print("Zähler:", i)

# while-Schleife: Zähle bis 3
z = 0
while z < 4:
    print("While:", z)
    z += 1

# continue und break
for i in range(10):
    if i == 5:
        break  # Stoppt die Schleife
    if i % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print("Ungerade Zahl:", i)
