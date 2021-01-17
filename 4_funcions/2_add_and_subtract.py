def sum_numbers(a, b):
    return a + b


def subtract(c):
    return c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b) - subtract(c)
    return result


a = int(input())
b = int(input())
c = int(input())

print(add_and_subtract(a, b, c))
