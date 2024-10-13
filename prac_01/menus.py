# Get user's name
user_name = input("Please enter your name: ")
OPTIONS = "(H)ello \n(G)oodbye \n(Q)uit"
print(OPTIONS)

# Get user's menu selection
user_choice = input("Choose an option: ").upper()
while user_choice != 'Q':
   if user_choice == 'H':
       print(f"Hello, {user_name}!")
   elif user_choice == 'G':
       print(f"Goodbye, {user_name}!")
   else:
       print("Invalid option, try again.")
   print(OPTIONS)
   user_choice = input("Choose an option: ").upper()

print("Program terminated.")