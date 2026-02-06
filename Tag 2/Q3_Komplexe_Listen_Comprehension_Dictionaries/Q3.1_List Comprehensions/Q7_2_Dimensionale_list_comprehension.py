# 2 Dimensionale list comprehension:
"""
| i | 3 - i |
| - | ----- |
| 0 | 3     |
| 1 | 2     |
| 2 | 1     |
--------------------------------------------------
diagonale aufsummieren!
[index 2D:   0  1  2
        0   [3, 2, 1],
        1   [3, 2, 1],
        2   [3, 2, 1]
]
--------------------------------------------------
Wir nehmen immer das Element auf Position [i][i].

➤ i = 0

t[0][0] = 3
s = 3

➤ i = 1

t[1][1] = 2
s = 3 + 2 = 5

➤ i = 2

t[2][2] = 1
s = 5 + 1 = 6
--------------------------------------------------
"""

t = [[3-i for i in range(3)] for j in range(3)]
s = 0

for i in range(3):
    s += t[i][i]
print(s)
