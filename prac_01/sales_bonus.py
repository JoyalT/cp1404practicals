"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# Get sales amount from the user
revenue = float(input("Input sales amount: $"))
while revenue > 0:
    # Calculate commission based on revenue
    if revenue < 1000:
        reward = revenue * 0.10  # 10% commission for sales below $1000
    else:
        reward = revenue * 0.15  # 15% commission for sales $1000 or more
    print(f"Your commission is ${reward:.0f}")
    revenue = float(input("Input sales amount: $"))
print("Sales figure not valid.")