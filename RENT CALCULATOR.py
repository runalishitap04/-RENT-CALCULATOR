def rent_calculator():
    print("=== Rent Calculator ===")

    # Get the monthly rent amount
    while True:
        try:
            rent_amount = float(input("Enter monthly rent amount (₹): "))
            if rent_amount < 0:
                print("Rent amount cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Get number of months
    while True:
        try:
            months = int(input("Enter number of months: "))
            if months <= 0:
                print("Months must be at least 1. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Optional: Get utility charges per month
    while True:
        utility_input = input("Do you want to include monthly utilities? (y/n): ").strip().lower()
        if utility_input == 'y':
            while True:
                try:
                    utilities = float(input("Enter monthly utilities amount (₹): "))
                    if utilities < 0:
                        print("Utilities cannot be negative. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            break
        elif utility_input == 'n':
            utilities = 0.0
            break
        else:
            print("Please enter 'y' or 'n'.")

    # Calculate total rent
    total_rent = (rent_amount + utilities) * months

    print("\n=== Rent Summary ===")
    print(f"Monthly Rent: ₹{rent_amount:.2f}")
    print(f"Monthly Utilities: ₹{utilities:.2f}")
    print(f"Number of Months: {months}")
    print(f"Total Rent (including utilities): ₹{total_rent:.2f}")

if __name__ == "__main__":
    rent_calculator()
