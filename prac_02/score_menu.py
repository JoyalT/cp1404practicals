def main():
    score = get_valid_score()  # Get a valid score before the menu loop
    choice = ""

    while choice.upper() != "Q":
        print_menu()
        choice = input("Choose an option: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid choice, please choose a valid option.")


def print_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! It must be between 0 and 100.")
        score = float(input("Enter a valid score (0-100): "))
    return score


def print_result(score):
    """Determine and print the result based on the score."""
    if score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    """Print stars equal to the value of the score."""
    print('*' * int(score))


# Start the program
main()