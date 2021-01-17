numbers = input().split()

numbers.sort(reverse=True)
final_result = ''.join(numbers)

print(final_result)