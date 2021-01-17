string = input().split(',')
beggars = int(input())
result = [0] * beggars

for i in range(len(string)):
    string[i] = int(string[i])

for i in range(len(string)):
    index = i % beggars
    result[index] += string[i]
print(result)