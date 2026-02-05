""" 
Beispiel: sorted() - Gibt eine neue sortierte Liste zurück (Original bleibt erhalten)


| Zeichen | R | e | g | e | n | s | c | h | a | u | e  | r  |
| Index   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

"""



text = "Regenschauer"
position = text.rfind("e")  #  rfind() sucht von rechts nach links – zählt aber von links nach rechts

print("Letztes 'e' bei Index:", position)   # 10

