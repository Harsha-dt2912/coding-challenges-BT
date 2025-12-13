while True:
    try:
        num = float(input("Enter a decimal number: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid decimal number.")

whole_part = int(num)
fractional_part = num - whole_part

print("Whole part:", whole_part)
print("Fractional part:", round(fractional_part, 6))
