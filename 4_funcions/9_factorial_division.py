def calc_factorial(n):
    res = 1
    for num in range(1, n+1):
        res *= num
    return res


number_a = int(input())
number_b = int(input())

factorial_num_a = calc_factorial(number_a)
factorial_num_b = calc_factorial(number_b)

result = factorial_num_a / factorial_num_b
print(f"{result:.2f}")