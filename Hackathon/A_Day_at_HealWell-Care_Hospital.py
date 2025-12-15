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


#  Admin sets services of the day
services = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI"
]

costs = [500, 300, 800, 1500, 4000, 7000]

# Patient Details

name = get_valid_patient_name()
age = get_valid_age()
gender = get_valid_gender()
contact = get_valid_contact()


# service selection

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

# Fetching Costs of Selected Services

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

