def tax_check():
    name = input("Enter your name: ").strip() or "User"

    while True:
        salary_input = input("Enter your salary: ").strip()
        try:
            salary = float(salary_input)
            break
        except ValueError:
            print("Invalid salary! Please enter a numeric value.")

    if salary > 300000:
        print(f"{name}, your salary is {salary} and you MUST pay tax.")
    else:
        print(f"{name}, your salary is {salary} and you DO NOT need to pay tax.")

if __name__ == "__main__":
    tax_check()