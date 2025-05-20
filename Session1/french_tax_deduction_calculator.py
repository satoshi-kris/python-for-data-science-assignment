# Task 2: French Tax Deduction Calculator

def calculate_tax_deductions(income, num_half_shares, childcare_expense, home_help_expense, renovation_eligible):
    # Rule 1: Income Threshold
    income_threshold = 27000  # Example threshold; real value may vary
    income_status = "Eligible" if income <= income_threshold else "Not eligible"

    # Rule 2: Family Quotient
    max_reduction_per_half_share = 1759
    family_quotient_reduction = num_half_shares * max_reduction_per_half_share

    # Rule 3: Deductible Expenses
    childcare_credit = min(childcare_expense, 3500) * 0.5
    home_help_credit = home_help_expense * 0.5
    renovation_credit = 1500 if renovation_eligible else 0  # Sample fixed credit

    total_credits = childcare_credit + home_help_credit + renovation_credit

    return {
        "Income Status": income_status,
        "Family Quotient Reduction (€)": family_quotient_reduction,
        "Childcare Credit (€)": childcare_credit,
        "Home Help Credit (€)": home_help_credit,
        "Renovation Credit (€)": renovation_credit,
        "Total Tax Credits (€)": total_credits
    }

# Example interactive usage
print("\n--- French Tax Deduction Calculator ---")
income = float(input("Enter your income (€): "))
num_half_shares = float(input("Enter number of half-shares in household (e.g., 2 for single, 3 for 1 child): "))
childcare_expense = float(input("Enter childcare expenses (€): "))
home_help_expense = float(input("Enter home help services expenses (€): "))
renovation_input = input("Did you make energy-saving home improvements (yes/no)? ").strip().lower()
renovation_eligible = renovation_input == "yes"

result = calculate_tax_deductions(income, num_half_shares, childcare_expense, home_help_expense, renovation_eligible)

print("\n--- Tax Deduction Summary ---")
for key, value in result.items():
    print(f"{key}: {value}")
