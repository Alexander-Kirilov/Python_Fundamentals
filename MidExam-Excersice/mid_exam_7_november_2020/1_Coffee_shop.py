orders = int(input())
total_price = 0

for order in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price = ((days * capsule_count) * price_per_capsule)
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
