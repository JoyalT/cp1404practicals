"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ans:A ValueError will occur if the user inputs a value that cannot be converted to an integer
2. When will a ZeroDivisionError occur?
ans:ZeroDivisionError will occur if the user enters 0 as the denominator, because division by zero is undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
while True:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Cannot divide by zero!")
        else:
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers_file.txt!")
    print("Finished.")


