total = 0

n = int(input("Enter number of items: "))

for i in range(n):
    print("\nItem", i + 1)
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity
    total = total + amount

    print("Amount =", amount)

print("\nTotal Bill =", total)
