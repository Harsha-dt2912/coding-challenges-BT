import re

# ---------------- PATIENT VALIDATION FUNCTIONS ---------------- #

def validate_patient_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]{1,50}", name))


def validate_age(age):
    return age > 0 and age <= 120


def validate_gender(gender):
    return gender.lower() in ["male", "female", "other"]


def validate_contact(contact):
    return contact.isdigit() and len(contact) == 10

# ---------------- PATIENT INPUT FUNCTIONS ---------------- #

def get_valid_patient_name():
    while True:
        name = input("Enter Patient Name: ").strip()
        if validate_patient_name(name):
            return name
        print("❌ Invalid name! Alphabets only, max 50 characters.")


def get_valid_age():
    while True:
        try:
            age = int(input("Enter Age: "))
            if validate_age(age):
                return age
            print("❌ Age must be between 1 and 120.")
        except ValueError:
            print("❌ Enter a valid numeric age.")


def get_valid_gender():
    while True:
        gender = input("Enter Gender (Male/Female/Other): ").strip()
        if validate_gender(gender):
            return gender.capitalize()
        print("❌ Gender must be Male, Female, or Other.")


def get_valid_contact():
    while True:
        contact = input("Enter Contact Number: ").strip()
        if validate_contact(contact):
            return contact
        print("❌ Contact must be a valid 10-digit number.")


# -------- Admin sets services of the day----------
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

# ----------Patient Details---------------

name = get_valid_patient_name()
age = get_valid_age()
gender = get_valid_gender()
contact = get_valid_contact()


# -----------service selection-----------------

print("\nAvailable Services:")
for i, service in enumerate(services, start=1):
    print(f"{i}. {service}")

print("\nSelect services using comma or space (e.g., 1,3 or 1 3)")
print("Enter Q to quit without selecting any service.")

selected_services = []

while True:
    user_choice = input("Select service numbers: ").strip()

    # Quit option 
    if user_choice.lower() == 'q':
        print("No services selected. Exiting selection.")
        selected_services = []
        break

    # Empty input
    if not user_choice:
        print("❌ At least one service must be selected or press Q to quit.")
        continue

    try:
        
        user_input = user_choice.replace(",", " ")
        choices = [int(i.strip()) for i in user_input.split()]

        selected_services = []   # reset before adding
        for choice in choices:
            if 1 <= choice <= len(services):
                selected_services.append(services[choice - 1])
            else:
                raise ValueError

        # Remove duplicates
        selected_services = list(dict.fromkeys(selected_services))

        break

    except ValueError:
        print("❌ Invalid selection. Please enter valid service numbers.")

# -----Fetching Costs of Selected Services-------

selected_costs = []

if not selected_services:
    print("No services selected. Billing process terminated.")
    exit()

for service in selected_services:
    index = services.index(service)
    selected_costs.append(costs[index])

print("\nSelected Services and Costs:")
for i in range(len(selected_services)):
    print(f"{i+1}. {selected_services[i]} - ₹{selected_costs[i]}")

#  Calculating Total Cost

subtotal = sum(selected_costs)
print(f"\nTotal Cost (Before Tax): ₹{subtotal}")

# --------Apply Discounts---------

discount = 0
senior_discount=0
high_bill_discount=0
# Senior Citizen Discount
if age >= 60:
    senior_discount = subtotal * 0.10
    discount += senior_discount
    print(f"Senior Citizen Discount (10%): ₹{senior_discount:.2f}")

# High Bill Discount
if subtotal > 5000:
    high_bill_discount = (subtotal - discount) * 0.05
    discount += high_bill_discount
    print(f"High Bill Discount (5%): ₹{high_bill_discount:.2f}")

discounted_subtotal = subtotal - discount
print(f"Subtotal after Discounts: ₹{discounted_subtotal:.2f}")

# Applying GST 

GST_RATE = 0.18
gst_amount = discounted_subtotal * GST_RATE
grand_total = discounted_subtotal + gst_amount

print(f"GST (18%): ₹{gst_amount:.2f}")
print(f"Grand Total: ₹{grand_total:.2f}")


#  -----------Invoice Generation-----------------


print("\n" + "-" * 60)
print("              HealWell Care Hospital")
print("                  Patient Invoice")
print("-" * 60)

# ---- Patient Info ----
print("Patient Information")
print("-" * 60)
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Gender  : {gender}")
print(f"Contact : {contact}")

# ---- Services Table ----
print("\nServices Availed")
print("-" * 60)
print(f"{'No.':<5}{'Service':<30}{'Cost (₹)':>10}")
print("-" * 60)

for i in range(len(selected_services)):
    print(f"{i+1:<5}{selected_services[i]:<30}{selected_costs[i]:>10}")

print("-" * 60)

# ---- Billing Summary ----
print("Billing Summary")
print("-" * 60)
print(f"{'Subtotal':<40} ₹{subtotal:>8.2f}")

# Discounts
if discount > 0:
    print("Discounts Applied:")
    if senior_discount > 0:
        print(f"{'Senior Citizen Discount (10%)':<40}-₹ {senior_discount:>7.2f}")
    if high_bill_discount > 0:
        print(f"{'High Bill Discount (5%)':<40}-₹ {high_bill_discount:>7.2f}")

    print(f"{'Total Discount':<40}-₹ {discount:>7.2f}")
    print(f"{'Subtotal After Discount':<40} ₹ {discounted_subtotal:>8.2f}")
else:
    print(f"{'Discounts not Applied':<40} ₹ 0.00")

# GST & Total
print(f"{'GST (18%)':<40} ₹ {gst_amount:>8.2f}")
print("-" * 60)
print(f"{'GRAND TOTAL':<40} ₹ {grand_total:>8.2f}")

print("-" * 60)
print("Thank you for choosing HealWell Care Hospital!")
print("-" * 60)
