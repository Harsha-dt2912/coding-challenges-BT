def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} marks: ").strip())
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter numeric marks.")

name = input("Enter student name: ").strip() or "Student"

m1 = get_marks("physics")
m2 = get_marks("chemistry")
m3 = get_marks("maths")

total = m1 + m2 + m3
average = total / 3

if average >= 60:
    result = "1st Class"
elif average >= 50:
    result = "2nd Class"
elif average >= 35:
    result = "Pass Class"
else:
    result = "Fail"

print("\n--- Student Result ---")
print("Name    :", name)
print("Total   :", total)
print("Average :", round(average, 2))
print("Class   :", result)
