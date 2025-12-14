
items = []
grand_total = 0
total_quantity = 0

while True:
    item_code = input("\nEnter Item Code: ")
    description = input("Enter Item Description: ")
    quantity = int(input("Enter Quantity: "))
    total_quantity += quantity
    price = float(input("Enter Price per Item: "))

    item_total = quantity * price
    print(f"Item Total: ₹{item_total:.2f}")

    items.append(item_total)
    grand_total += item_total

    choice = input("Add another item? (y/n): ").lower()
    if choice != 'y':
        break

print(f"\nGrand Total: ₹{grand_total:.2f}")


#  Discounts

discount = 0

if grand_total > 10000:
    discount = grand_total * 0.10
    print(f"10% Discount Applied: ₹{discount:.2f}")

grand_total -= discount

if total_quantity > 20:
    qty_discount = grand_total * 0.05
    grand_total -= qty_discount
    print(f"5% Quantity Discount Applied: ₹{qty_discount:.2f}")

print(f"Grand Total after Discounts: ₹{grand_total:.2f}")


#  Membership Discount

member = input("\nis he/she a member? (y/n): ").lower()

if member == 'y':
    member_discount = grand_total * 0.02
    grand_total -= member_discount
    print(f"Membership Discount (2%): ₹{member_discount:.2f}")

print(f"Grand Total after Membership Discount: ₹{grand_total:.2f}")


