"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
day = 0

print(f"Starting price: ${price:,.2f}")

while MIN_PRICE <= price <= MAX_PRICE:
    day += 1
    price_change = 0
    # 50% chance to increase or decrease
    if random.randint(1, 2) == 1:
        # Increase by 0 to 10%
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # Decrease by 0 to 5%
        price_change = -random.uniform(0, MAX_DECREASE)

    price += price_change
    print(f"Day {day}: ${price:,.2f}")

print("Simulation ended.")
