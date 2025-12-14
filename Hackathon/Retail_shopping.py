# Challenge 26: Multiple Items and Grand Total

items = []
grand_total = 0

while True:
    item_code = input("\nEnter Item Code: ")
    description = input("Enter Item Description: ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("Enter Price per Item: "))

    item_total = quantity * price
    print(f"Item Total: ₹{item_total:.2f}")

    items.append(item_total)
    grand_total += item_total

    choice = input("Add another item? (y/n): ").lower()
    if choice != 'y':
        break

print(f"\nGrand Total: ₹{grand_total:.2f}")
