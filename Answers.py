def compute_savings(item_price, discount_offered):
    """Calculate your fantastic deal based on the discount!"""
    if discount_offered >= 20:
        savings = item_price * (discount_offered / 100)
        discounted_price = item_price - savings
        return discounted_price
    else:
        return item_price

# Friendly user interaction
print("Welcome to Your Personal Savings Calculator! ")
try:
    print("\nLet's find out how much you'll save!")
    original_cost = float(input("First, tell me the original price of your item: $"))
    discount_rate = float(input("Now enter the discount percentage you're getting (just the number): "))

    your_final_price = compute_savings(original_cost, discount_rate)

    if discount_rate >= 20:
        print(f"\n🎉 Congratulations! You're saving {discount_rate}%!")
        print(f"Your discounted price is just ${your_final_price:.2f}!")
    else:
        print(f"\nThe current discount of {discount_rate}% isn't enough for additional savings.")
        print(f"Your final price remains at ${your_final_price:.2f}.")
        
except ValueError:
    print("\nOops! Please enter numbers only (like 49.99 or 25). Let's try again!")