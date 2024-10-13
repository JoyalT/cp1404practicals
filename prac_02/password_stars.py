def main():
    user_password = get_input()
    masked_password = show_asterisks(user_password)
    print(masked_password)

def show_asterisks(user_password):
    return '*' * len(user_password)

def get_input():
    user_password = input("Enter your password: ")
    return user_password


main()
