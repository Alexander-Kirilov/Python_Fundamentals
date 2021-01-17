received_nums = list(map(int, input().split()))
nums_to_remove = int(input())
received_nums_copy = received_nums.copy()

sorted_nums = received_nums.copy()
sorted_nums.sort(reverse=True)


for remove_num in range(nums_to_remove):
    sorted_nums.pop()

for el in received_nums_copy:
    if el not in sorted_nums:
        received_nums.remove(el)

print(received_nums)
