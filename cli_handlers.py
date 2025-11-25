# Project       :   Analysis of Algorithms
# Instructor    :   Oral Robinson
# Date          :   November , 2025
# Authors       :   Desrine Harripaul, Rackeel Brooks, Giomar Griffiths and Zemario Pascoe

from typing import List
# Imports core logic functions
from financial_models import fixedInvestor, variableInvestor, finallyRetired, maximumExpensed

# --- Utility Functions for Input Validation ---

def get_valid_float_input(prompt: str) -> float:
    """Handles basic float input and error checking."""
    while True:
        try:
            value = float(input(prompt))
            
            return value
        except ValueError:
            print("\n[ERROR] Invalid input. Please enter a numerical value.")
            
def get_valid_positive_numerical_input(prompt: str, allow_zero: bool, Type: str):
    """ Handles float/integer input that should only be positive.

       The parameter 'allowZero' is there to reduce the amount of functions, 
       just add true or false if it should or shouldn't be entered

       'Type' parameter is for specifying whether we are working with integers or floats
    """
    while True:
        try:
            match Type:
                case "float":
                    value = float(input(prompt))
                case "int":
                    value = int(input(prompt))

            if value < 0:
                print("Value can't be negative.")
            elif value == 0 and not allow_zero:
                print("Value cannot be zero")
            else:
                return value

        except ValueError:
            print("\n[ERROR] Invalid input. Please enter a valid numerical value.")

def get_annual_interest_rate(prompt: str) -> float:
    """Handles basic float input and error checking."""
    while True:
        try:
            value = float(input(prompt))
            if not (-0.4 <= value <= 2.0):
                #range for input
                print("\n [ERROR] Rate must be between -40% and 200% (e.g., 0.04 = 4%)")
                continue
            
            return value
        except ValueError:
            print("\n[ERROR] Invalid input. Please enter a numerical value.")

# --- Handler Functions for Each Task ---

def handle_fixed_investor():
    """Menu 1: Handles Fixed Growth inputs and output."""
    print("\n--- 1. Fixed Growth Simulation ---")
    
    principal = get_valid_positive_numerical_input("   Enter Initial Principal ($): ", True, "float")
    rate = get_annual_interest_rate("   Enter Annual Interest Rate (e.g., 0.05 for 5%): ")
    # Annual Contribution input
    annual_contribution = get_valid_positive_numerical_input("   Enter Annual Contribution ($): ", True, "float")
    years = get_valid_positive_numerical_input("   Enter Years to Retirement: ", False, "int")

    # Pass the new argument to the core function
    final_balance = fixedInvestor(principal, rate, years, annual_contribution)
    
    print("\n-----------------------------------------------------")
    print(f"✅ FINAL BALANCE AFTER {years} YEARS: **${final_balance:,.2f}**")
    print("-----------------------------------------------------")

def handle_variable_investor():
    """Menu 2: Handles Variable Growth inputs and output."""
    print("\n--- 2. Variable Growth Simulation ---")

    principal = get_valid_positive_numerical_input("   Enter Starting Principal ($): ", True, "float")
    # Annual Contribution input
    annual_contribution = get_annual_interest_rate("   Enter Annual Contribution (%): ")
    rates_str = input("   Enter Annual Rates (comma-separated, e.g., 0.10, 0.05, -0.02): ")
    
    rate_list = []
    try:
        for r in rates_str.split(','):
            if r.strip():
                rate_list.append(float(r.strip()))
    except ValueError:
        print("\n[ERROR] Invalid rate list format. Please ensure all values are numbers.")
        return

    # Pass the new argument to the core function
    final_balance = variableInvestor(principal, rate_list, annual_contribution)
    
    print("\n-----------------------------------------------------")
    print(f"✅ FINAL BALANCE AFTER {len(rate_list)} YEARS: **${final_balance:,.2f}**")
    print("-----------------------------------------------------")

def handle_finally_retired():
    """Menu 3: Handles Retirement Longevity inputs and output."""
    print("\n--- 3. Retirement Expense Simulation ---")

    balance = get_valid_positive_numerical_input("   Enter Starting Retirement Balance ($): ", True, "float")
    expense = get_valid_positive_numerical_input("   Enter Annual Withdrawal/Expense ($): ", True, "float")
    rate = get_valid_positive_numerical_input("   Enter Post-Retirement Growth Rate (e.g., 0.04): ", True, "float")

    years_lasted = finallyRetired(balance, expense, rate)
    
    print("\n-----------------------------------------------------")
    if years_lasted >= 500:
        print(f"✅ Funds are Perpetual! (Lasts for >{500} years)")
    elif years_lasted <= 0:
        print("❌ Funds are depleted in Year 1 or less (Expense exceeds initial growth).")
    else:
        print(f"✅ FUNDS LAST FOR: **{years_lasted} years**")
    print("-----------------------------------------------------")


def handle_maximum_expensed():
    """Menu 4: Handles Optimization inputs and output (Binary Search)."""
    print("\n--- 4. Optimization via Successive Approximation ---")
    
    balance = get_valid_positive_numerical_input("   Enter Starting Retirement Balance ($): ", True, "float")
    rate = get_valid_positive_numerical_input("   Enter Expected Average Growth Rate (e.0.05):  ", True, "float")
    target_years = get_valid_positive_numerical_input("   Enter Target Retirement Length (Years, e.g., 30): ", False, "int")

    optimal_expense = maximumExpensed(balance, rate, target_years)
    
    # Verification to demonstrate correctness
    check_years = finallyRetired(balance, optimal_expense, rate)

    print("\n-----------------------------------------------------")
    print(f"✅ MAX SUSTAINABLE ANNUAL WITHDRAWAL (for {target_years} years): **${optimal_expense:,.2f}**")
    print(f"(Verification: This withdrawal rate lasts for {check_years} years)")
    print("-----------------------------------------------------")

# End of cli_handlers.py
