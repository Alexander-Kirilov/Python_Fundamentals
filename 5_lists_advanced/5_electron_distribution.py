count_electrons = int(input())
result = []

for electron in range(1, count_electrons+1):
    curr_shell = electron**2*2
    if curr_shell <= count_electrons:
        result.append(curr_shell)
    else:
        result.append(count_electrons)
    count_electrons -= curr_shell
    if count_electrons <= 0:
        break

print(result)