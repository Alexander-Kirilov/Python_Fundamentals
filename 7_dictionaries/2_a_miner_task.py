product = input()

resource = {}

while not product == "stop":
    quantity = int(input())

    if product not in resource:
        resource[product] = 0
    resource[product] += quantity

    product = input()

for key, value in resource.items():
    print(f"{key} -> {value}")