balance = 10000

while True:
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance =", balance)
    else:
        print("Insufficient balance!")

    choice = input("Do you want to withdraw again? (yes/no): ")

    if choice == "no":
        print("Thank you!")
        break
