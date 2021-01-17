factor = int(input())
length_of_list = int(input())

multiples_list = []

for num in range(1, length_of_list+1):
    multiples_list.append(num * factor)

print(multiples_list)
