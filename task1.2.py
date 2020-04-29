N = int(input('Input amount of numbers(number must be > 2): '))

if N <= 2:
    print('Too small amount of numbers to be fit us list!')
    quit()

a = []

for numb in range(N):
    n = input('Input number:')
    a.append(n)

print('The largest number: ', max(a))

a.remove(max(a))
print('The second one: ', max(a))