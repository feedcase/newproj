i = int(input('Input amount of numbers(number must be > 2): '))

if i < 2:
    print('Too small amount of numbers to be fit us list!')
    quit()

a = []

for numb in range(i):
    n = input('Input number:')
    a.append(n)

print('The largest number: ', max(a))

a.pop(a.index((max(a))))
print('The second one: ', max(a))