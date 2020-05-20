a = []

print("If u think that your list is big enough input ' '")

while True:
    i = input('Input some number: ')

    if i == ' ':
        break

    a.append(int(i))

a_set = set(a)
cmn = None
cmn_cnt = 0

for numb in a_set:
    cnt = a.count(numb)

    if cnt > cmn_cnt:
        cmn_cnt = cnt
        cmn = numb

print('Your list: ', a)
print('Most common number:', cmn)
