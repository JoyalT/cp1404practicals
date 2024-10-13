"""
CP1404/CP5632 Practical
List comprehensions (similar version)
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop creating a new list of first initials
first_initials = [name[0] for name in names]  # List comprehension directly
print(first_initials)

# list comprehension creating a list of initials from full names
full_initials = [f"{name.split()[0][0]}{name.split()[1][0]}" for name in full_names]
print(full_initials)

# filtering names that start with 'A'
a_names = [name for name in names if name[0] == 'A']
print(a_names)

# sorting and joining names into a single string
joined_names = " ".join(sorted(names))
print(joined_names)

# converting full names to lowercase
lowercase_full_names = [full_name.lower() for full_name in full_names]
print(lowercase_full_names)

# converting string numbers to integers
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = list(map(int, almost_numbers))  # Using map to convert to integers
print(numbers)

# selecting numbers greater than 9
numbers_greater_than_9 = [number for number in numbers if number > 9]
print(numbers_greater_than_9)

# creating a string of last names for full names longer than 11 characters
long_last_names = ", ".join([full_name.split()[1] for full_name in full_names if len(full_name) > 11])
print(long_last_names)