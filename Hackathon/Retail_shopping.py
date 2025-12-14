#  Basic Item Entry and Item Total

item_code = input("Enter Item Code: ")
description = input("Enter Item Description: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Item: "))

item_total = quantity * price

print(f"Item Total: ₹{item_total:.2f}")
