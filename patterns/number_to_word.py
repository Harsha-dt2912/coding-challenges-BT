num_words = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

while True:
    num = input("Enter a number: ").strip()
    if num.isdigit():
        break
    else:
        print("Invalid input! Enter digits only.")

print("Output:")
for digit in num:
    print(num_words[int(digit)], end=" ")
