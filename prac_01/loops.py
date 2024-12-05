# Display odd numbers between 1 and 20
for odd in range(1, 21, 2):
    print(odd, end=' ')
print()  # Move to a new line

# Count in 10s from 0 to 100
for tens in range(0, 101, 10):
    print(tens, end=' ')
print()  # Move to a new line

# Count down from 20 to 1
for reverse in range(20, 0, -1):
    print(reverse, end=' ')
print()  # Move to a new line

# Print a single line of stars, with the number of stars entered by the user
stars_count = int(input('Enter number of stars: '))
for _ in range(stars_count):
    print('*', end='')  # Print stars in one line
print()  # Move to a new line
# Print lines of increasing stars
for rows in range(1, stars_count + 1):
    print('*' * rows)  # Print increasing number of stars