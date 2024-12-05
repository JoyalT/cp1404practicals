"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Get the user input for marks
marks_obtained = float(input("Please input your score: "))

# Check if the score is within the valid range
if marks_obtained < 0 or marks_obtained > 100:
    print("Score out of range!")
else:
    # Determine the result based on the score
    if marks_obtained < 50:
        print("Needs Improvement")
    elif marks_obtained <= 90:
        print("Satisfactory")
    else:
        print("Outstanding")