import math

def get_value(field_name):
    while True:
        value = input(field_name).strip()

        if value == "":
            print(f"{field_name} cannot be empty.")
            continue

        try:
            number = float(value)

            # Reject NaN / Infinity
            if math.isnan(number) or math.isinf(number):
                print(f"{field_name} must be a valid finite number.")
                continue

            # Reject negative numbers
            if number < 0:
                print(f"{field_name} cannot be negative.")
                continue

            return number

        except ValueError:
            print(f"{field_name} must be a valid numeric value.")


def validate_multiply(a, b):
    
    result = a * b
    if math.isinf(result):
        print("Overflow occurred during discount calculation.")
        exit()
    return result

print(" DISCOUNT CALCULATOR")
print("--------------------------------")

total_amount = get_value("Total Amount:")
discount_percentage = get_value("Discount Percentage:")

# Formula: DiscountAmount = (A × D) / 100
a_times_d = validate_multiply(total_amount, discount_percentage)
discount_amount = a_times_d / 100   

final_price = total_amount - discount_amount

print("\n RESULTS")
print(f"Discount Amount = {discount_amount}")
print(f"Final Price After Discount = {final_price}")
