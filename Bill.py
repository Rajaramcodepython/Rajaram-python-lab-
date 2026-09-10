units = int(input("Enter the units consumed: "))

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 2.35
elif units <= 500:
    bill = (100 * 2.35) + (units - 200) * 4.70
else:
    bill = (100 * 2.35) + (300 * 4.70) + (units - 500) * 6.25

print("EB Bill Amount = Rs.", bill)
