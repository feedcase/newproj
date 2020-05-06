import math

x = int(input('Input the number from which you want to get the cosine: '))
N = int(input('Input the degree of accuracy of the desired cosine: '))


r = 0
i = 1

for i in range(N):
    o = math.pow(x, i) // (math.factorial(i))
    if i % 2:
        o = -o
    r += o


print('cos (x) = ', r)
