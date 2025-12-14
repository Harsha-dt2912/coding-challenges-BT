import re

MAX_SALARY = 10_000_000  # ₹1,00,00,000
STANDARD_DEDUCTION = 50_000  # ₹50,000


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

# ---------------- CALCULATION gross salary ---------------- #

def gross_salary(basic, allowance, bonus_percent):
    gross_monthly = basic + allowance
    annual_bonus = (gross_monthly * 12) * (bonus_percent / 100)
    annual_gross = (gross_monthly * 12) + annual_bonus
    return gross_monthly, annual_gross

# ---------------- CALCULATION taxable income ---------------- #

def calculate_taxable_income(annual_gross):
    return max(annual_gross - STANDARD_DEDUCTION, 0)

# ---------------- CALCULATION tax ---------------- #
def calculate_tax(taxable_income):
    tax = 0
    slabs = [
        (300000, 0.00),
        (600000, 0.05),
        (900000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float('inf'), 0.30)
    ]

    previous = 0
    for limit, rate in slabs:
        if taxable_income > previous:
            amount = min(taxable_income, limit) - previous
            tax += amount * rate
            previous = limit
        else:
            break

    # Section 87A rebate
    if taxable_income <= 700000:
        tax = 0
    # health and education cess 4%
    cess = tax * 0.04
    total_tax = tax + cess
    return tax, cess, total_tax

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


gross_monthly, annual_gross = gross_salary(
    basic_salary, special_allowance, bonus_percentage)

print("\n---Gross Salary Details ---")
print(f"Gross Monthly Salary : ₹{gross_monthly:.2f}")
print(f"Annual Gross Salary  : ₹{annual_gross:.2f}")



taxable_income = calculate_taxable_income(annual_gross)

print("\n--- Taxable Income Calculation ---")
print(f"Standard Deduction : ₹50,000")
print(f"Taxable Income     : ₹{taxable_income:.2f}")


tax, cess, total_tax = calculate_tax(taxable_income)

print("\n--- Tax Calculation ---")
print(f"Tax        : ₹{tax:.2f}")
print(f"Cess (4%)  : ₹{cess:.2f}")
print(f"Total Tax  : ₹{total_tax:.2f}")


