# Prompt user for 5 numbers and store them in a list
numbers = []
for i in range(5):
    number = float(input(f"Number: "))
    numbers.append(number)

# Output information about the numbers
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

# List of usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask user for their username
username_input = input("Enter your username: ")

# Check if the username is in the list of authorized users
if username_input in usernames:
    print("Access granted")
else:
    print("Access denied")