import math

def read_input(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("❌ Input cannot be empty.")
            continue

        try:
            number = float(value)

            # Disallow NaN or Infinity
            if math.isnan(number) or math.isinf(number):
                print("❌ Invalid number (NaN or Infinity).")
                continue

            if number <= 0:
                print("❌ Value cannot be negative or ZERO")
                continue

            return number

        except ValueError:
            print("❌ Enter a valid numeric value.")


def safe_multiply(a, b):
   
    result = a * b
    if math.isinf(result):
        print("❌ Overflow occurred (number too large).")
        exit()
    return result


print("📌 SIMPLE INTEREST CALCULATOR")
print("--------------------------------")

P = read_input("Enter Principal (P): ")
R = read_input("Enter Rate of interest (R): ")
T = read_input("Enter Time (T): ")

# SI = (P × R × T) / 100
p_r = safe_multiply(P, R)
p_r_t = safe_multiply(p_r, T)
SI = p_r_t / 100   

print("\n Simple Interest =", SI)
