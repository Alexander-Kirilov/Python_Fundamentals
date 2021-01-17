command = input()

price = 0

while not (command == "special" or command == "regular"):
    current_price = float(command)
    if current_price <= 0:
        print("Invalid price!")
    else:
        price += current_price
    command = input()

if price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price:.2f}$")
    taxes = price * 0.2
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    total_price = price + taxes
    if command == "special":
        total_price -= total_price * 0.1
    print(f"Total price: {total_price:.2f}$")