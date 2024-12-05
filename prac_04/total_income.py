"""
CP1404/CP5632 Practical
"""


def main():
    """Display an income report for salaries over a specified number of months."""
    salaries = []
    num_months = int(input("How many months? "))

    for month in range(1, num_months + 1):
        salary = float(input(f"Enter salary for month {month}: "))
        salaries.append(salary)

    print_salary_report(salaries, num_months)


def print_salary_report(salaries, num_months):
    """Print a formatted salary report based on the given salaries and number of months."""
    print("\nSalary Report\n-------------")
    total_salary = 0
    for month in range(1, num_months + 1):
        salary = salaries[month - 1]
        total_salary += salary
        print(f"Month {month:2} - Salary: ${salary:10.2f} Total: ${total_salary:10.2f}")


main()