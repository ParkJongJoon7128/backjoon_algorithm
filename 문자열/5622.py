str = input()
split_str = list(str)

number = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
default_n = 2
result = 0 

for i in range(len(number)):
    for j in range(len(split_str)):
        if split_str[j] in number[i]:
            result += default_n + i + 1

print(result)