# Ask for the user's name
name = input("Enter your name: ")
with open("name.txt", "w") as name_file:
    name_file.write(name)

# Open name.txt and read the name, then print a greeting
with open("name.txt", "r") as name_file:
    name = name_file.read().strip()  # Ensure to remove any extraneous whitespace
print(f"Hi {name}!")

# Open numbers_file.txt.txt, read the first two numbers_file.txt
with open("numbers_file.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline().strip())  # Read first line and convert to int
    second_number = int(numbers_file.readline().strip())  # Read second line and convert to int

result = first_number + second_number
print(f"The sum of the first two numbers_file.txt is: {result}")

# Calculate the total of all numbers_file.txt in numbers_file.txt.txt
with open("numbers_file.txt", "r") as numbers_file:
    total = sum(int(line.strip()) for line in numbers_file)  # Convert each line to an integer and sum them

print(f"The total of all numbers_file.txt is: {total}")
