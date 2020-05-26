from time import time
from collections import deque

vales = deque()

while True:
    n = int(input('Input number: '))
    t = int(1000 * time())
    vales.append((n, t))
    while len(vales):
        val = vales[0]
        if t - val[1] < 30000:
            break
        vales.popleft()
    print(list(map(lambda x: x[0], vales)))
