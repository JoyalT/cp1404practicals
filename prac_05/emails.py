def get_name_from_email(email):
    """Extract a name from the given email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = ' '.join(parts).title()
    return name


def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        is_name_correct = input(f"Is your name {name}? (Y/n) ").lower()

        if is_name_correct != "" and is_name_correct != 'y':
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    # Display the dictionary entries
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()