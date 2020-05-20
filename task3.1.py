a = []

print("If u think that your list is big enough input ' '")

while True:
    i = input('Input some number: ')

    if i == ' ':
        break

    a.append(int(i))

a.sort()
print('Your list: ', a)
numb = int(input('Input the number whose index you want to know: '))
print('Index: ', a.index(numb))
