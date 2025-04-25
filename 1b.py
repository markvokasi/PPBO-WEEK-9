from collections import namedtuple

# a
Koordinat = namedtuple("Koordinat", "x y")

# b
titik1 = Koordinat(2, 4)

# c
print("indeks:", titik1[0], titik1[1])
print("nama field:", titik1.x, titik1.y)
print("getattr():", getattr(titik1, 'x'), getattr(titik1, 'y'))
