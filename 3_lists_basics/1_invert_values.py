nums = input()
nums_as_list = nums.split()
nums_as_int = list(map(int, nums_as_list))
revert_list = []

for num in nums_as_int:
    reversed_num = num * -1
    revert_list.append(reversed_num)

print(revert_list)
