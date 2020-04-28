i = input("Input ur string: ")
l = len(i)//2
for letter in range(l):
    if i[letter] != i[-1]:
        print('Not palindrome')
        quit()
print('Its palindrome')