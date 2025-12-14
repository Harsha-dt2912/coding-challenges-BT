import re

MAX_SALARY = 10_000_000  # ₹1,00,00,000


# ---------------- VALIDATION FUNCTIONS ---------------- #

def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]{1,50}", name))


def validate_emp_id(emp_id):
    return bool(re.fullmatch(r"[A-Za-z0-9]{5,10}", emp_id))


def validate_basic_salary(salary):
    return salary > 0 and salary <= MAX_SALARY


def validate_special_allowance(allowance):
    return allowance >= 0 and allowance <= MAX_SALARY


def validate_bonus_percentage(bonus):
    return 0 <= bonus <= 100


# ---------------- INPUT FUNCTIONS ---------------- #

def get_valid_name():
    while True:
        name = input("Enter Employee Name: ").strip()
        if validate_name(name):
            return name
        print("❌ Invalid Name! Alphabets only, max 50 characters.")


def get_valid_emp_id():
    while True:
        emp_id = input("Enter Employee ID: ").strip()
        if validate_emp_id(emp_id):
            return emp_id
        print("❌ Invalid EmpID! Alphanumeric, 5–10 characters.")


def get_valid_basic_salary():
    while True:
        try:
            salary = float(input("Enter Basic Monthly Salary: "))
            if validate_basic_salary(salary):
                return salary
            print("❌ Salary must be > 0 and ≤ ₹1,00,00,000.")
        except ValueError:
            print("❌ Enter a valid numeric salary.")


def get_valid_special_allowance():
    while True:
        try:
            allowance = float(input("Enter Special Allowances (Monthly): "))
            if validate_special_allowance(allowance):
                return allowance
            print("❌ Allowance must be ≥ 0 and ≤ ₹1,00,00,000.")
        except ValueError:
            print("❌ Enter a valid numeric allowance.")


def get_valid_bonus_percentage():
    while True:
        try:
            bonus = float(input("Enter Bonus Percentage (0–100): "))
            if validate_bonus_percentage(bonus):
                return bonus
            print("❌ Bonus must be between 0 and 100.")
        except ValueError:
            print("❌ Enter a valid numeric bonus percentage.")


# ---------------- MAIN (INPUT ONLY) ---------------- #

if __name__ == "__main__":
    print("\n=== Employee Input & Validation ===\n")

    name = get_valid_name()
    emp_id = get_valid_emp_id()
    basic_salary = get_valid_basic_salary()
    special_allowance = get_valid_special_allowance()
    bonus_percentage = get_valid_bonus_percentage()

    print("\n✅ Employee salary details!")
    print(f"Name               : {name}")
    print(f"Employee ID        : {emp_id}")
    print(f"Basic Salary       : ₹{basic_salary:.2f}")
    print(f"Special Allowance  : ₹{special_allowance:.2f}")
    print(f"Bonus Percentage   : {bonus_percentage}%")
