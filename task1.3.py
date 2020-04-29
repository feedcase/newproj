i = int(input('Input amount of numbers: '))
bum = 0
a = []

for numb in range(i):
    n = int(input('Input number:'))
    a.append(n)

from collections import Counter
c = Counter(a)

for numb in range(c[0]):
    a.remove(0)

for numb in range(c[0]):
    a.insert(0,0)

print(a)