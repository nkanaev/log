lines = open('glyphs.txt').readlines()
lines = [l.rstrip() for l in lines]

encoded = []
for idx, o in enumerate(range(0, len(lines), 6)):
    n = 0
    for r in range(5):
        for c in range(3):
            n |= int((lines[o+r]+'___')[c] == '*') << (r*3+c)
    encoded.append(n)
print(repr(encoded).replace(' ', ''))
print(''.join(map(chr, encoded)))
from numpy import base_repr
print(''.join([base_repr(n,36) for n in encoded]))
