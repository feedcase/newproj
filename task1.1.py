N = input('Input ur string: ')
l = len(N)//2
for letter in range(l):
    if N[letter] != N[-1 - letter]:
        print('Not palindrome')
        quit()
print('Its palindrome')