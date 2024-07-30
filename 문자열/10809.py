S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
arr = [-1] * len(alphabet)

for i in alphabet:
    print(S.find(i), end=' ')