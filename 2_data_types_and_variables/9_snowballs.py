count_of_snowballs = int(input())

snowball_snow = 0
snowball_time = 0
snowball_quality = 0
snowball_value = 0

snowball_value_max = None
snowball_snow_max = None
snowball_time_max = None
snowball_quality_max = None

for curr_snowball in range(count_of_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_snow / snowball_time) ** snowball_quality)
    if snowball_value > snowball_value_max:
        snowball_value_max = snowball_value
        snowball_snow_max = snowball_snow
        snowball_time_max = snowball_time
        snowball_quality_max = snowball_quality

print(f"{snowball_snow_max} : {snowball_time_max} = {snowball_value_max} ({snowball_quality_max})")
