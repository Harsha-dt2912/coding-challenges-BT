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

# Patient Details (Validated Input)

name = get_valid_patient_name()
age = get_valid_age()
gender = get_valid_gender()
contact = get_valid_contact()

