word = input().upper()
list_word = list(set(word)) 

arr = []

for i in list_word:
    arr.append(word.count(i))

if(arr.count(max(arr)) > 1):
    print("?")
else:
    print(list_word[arr.index(max(arr))])