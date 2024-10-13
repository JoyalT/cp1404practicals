"""
CP1404/CP5632 Practical
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_subject_data()
    display_subject_details(subject_data)


def load_subject_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    with open(FILENAME) as file:
        for line in file:
            line = line.strip()  # Remove any newline characters
            details = line.split(',')  # Split the line into subject, lecturer, and number of students
            details[2] = int(details[2])  # Convert number of students to an integer
            subject_details.append(details)  # Append the list ['subject', 'lecturer', students] to subject_details
    return subject_details


def display_subject_details(subject_data):
    """Display details of each subject in the format: 'subject is taught by lecturer and has students students'."""
    for subject in subject_data:
        subject_code, lecturer_name, student_count = subject
        print(f"{subject_code} is taught by {lecturer_name} and has {student_count} students")


main()