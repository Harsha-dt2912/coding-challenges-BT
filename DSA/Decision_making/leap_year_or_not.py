while True:
    year = input("Enter a year: ").strip()
    if year.isdigit():
        year = int(year)
        break
    else:
        print("Invalid input! Please enter a valid year.")

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")
