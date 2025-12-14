
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

    items.append({
    "code": item_code,
    "desc": description,
    "qty": quantity,
    "price": price,
    "total": item_total
})

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

member = input("\n are you a member? (y/n): ").lower()

if member == 'y':
    member_discount = grand_total * 0.02
    grand_total -= member_discount
    print(f"Membership Discount (2%): ₹{member_discount:.2f}")

print(f"Grand Total after Membership Discount: ₹{grand_total:.2f}")


# Tax Calculation

if grand_total < 5000:
    tax_rate = 0.05
elif grand_total <= 20000:
    tax_rate = 0.10
else:
    tax_rate = 0.15

tax = grand_total * tax_rate
grand_total += tax

print(f"Tax Applied ({int(tax_rate*100)}%): ₹{tax:.2f}")
print(f"Grand Total after Tax: ₹{grand_total:.2f}")

#  Promotional Discount on Specific Items

PROMO_CODE = "PROMO10"
promo_discount = 0
promo_items = []   # to store descriptions of promo items

for item in items:
    if item["code"] == PROMO_CODE:
        discount = item["total"] * 0.10
        item["total"] -= discount
        promo_discount += discount
        promo_items.append(item["desc"])

# Recalculate grand total
grand_total = sum(item["total"] for item in items)

if promo_discount > 0:
    print(f"\nPromotional Discount Applied on Item(s): {', '.join(promo_items)}")
    print(f"Total Promotional Discount: ₹{promo_discount:.2f}")
else:
    print("\nNo Promotional Discount Applied")

print(f"Grand Total after Promo Discount: ₹{grand_total:.2f}")

#  Payment Mode 

payment_mode = input("\nSelect Payment Mode (cash/card): ").lower()

if payment_mode == "card":
    surcharge = grand_total * 0.02
    grand_total += surcharge
    print(f"Credit Card Surcharge (2%): ₹{surcharge:.2f}")
else:
    print("No surcharge for cash payment")

print(f"Final Payable Amount: ₹{grand_total:.2f}")



# Minimum Purchase Requirement

if grand_total < 500:
    print("❌ Minimum purchase amount ₹500 not met. Invoice cannot be generated.")
    exit()

#  Loyalty Points

loyalty_points = int(grand_total // 100)

print(f"\nLoyalty Points Earned: {loyalty_points}")



