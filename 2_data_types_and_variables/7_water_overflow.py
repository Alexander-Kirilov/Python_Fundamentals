numbers_of_pours = int(input())
water_in_tank = 0
curr_pour = 1

for curr_pour in range(numbers_of_pours):
    water = int(input())
    curr_pour += 1
    water_in_tank += water
    if water_in_tank > 255:
        print("Insufficient capacity!")
        water_in_tank -= water


print(water_in_tank)