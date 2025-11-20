# Project       :   Analysis of Algorithms
# Instructor    :   Oral Robinson
# Date          :   November , 2025
# Authors       :   Desrine Harripaul, Rackeel Brooks, Giomar Griffiths and Zemario Pascoe

from typing import List

# --- Core Algorithmic Functions ---

def fixedInvestor(principal: float, rate: float, years: int, annual_contribution: float = 0.0) -> float:
    """
    Updated to include annual contributions in accordance with the rubric's
    Illustrative Example:

        Y_n = (salary * (savings + company contribution)) + Y_{n-1} * (1 + rate)

    Equivalent to:
        balance = balance * (1 + rate) + annual_contribution

    Parameters:
        principal (float): Initial investment amount.
        rate (float): Annual interest rate as decimal.
        years (int): Number of years invested.
        annual_contribution (float): Amount added at the end of each year.

    Returns:
        float: Final balance after compounding and contributions.
    """
    balance = principal
    for _ in range(years):
        balance = balance * (1 + rate) + annual_contribution
    return balance


def variableInvestor(principal: float, rateList: List[float], annual_contribution: float = 0.0) -> float:
    """
    Models the effect of varying annual interest rates sequentially, with optional
    annual contributions.
    """
    balance = principal
    for rate in rateList:
        balance = balance * (1 + rate) + annual_contribution
    return balance


def finallyRetired(balance: float, expense: float, rate: float) -> int:
    """
    Determines the number of years retirement funds last under steady withdrawals.

    Logic:
        balance = balance * (1 + rate) - expense

    Caps at 500 years to prevent infinite loops.
    """
    years = 0
    current_balance = balance

    while current_balance > 0 and years < 500:
        current_balance = current_balance * (1 + rate)
        current_balance -= expense
        years += 1

        # Early exit for extremely small balance
        if current_balance < 1e-6:
            break

    return years


def maximumExpensed(balance: float, rate: float, target_years: int = 30) -> float:
    """
    Uses Successive Approximation (Binary Search) to determine the maximum
    sustainable annual withdrawal so that the funds last at least `target_years`.

    This function directly supports the Divide-and-Conquer requirement.
    """
    low_expense = 0.0
    high_expense = balance
    optimal_expense = 0.0

    for _ in range(100):  # Ensures high precision
        mid_expense = (low_expense + high_expense) / 2
        years_sustained = finallyRetired(balance, mid_expense, rate)

        if years_sustained >= target_years:
            optimal_expense = mid_expense
            low_expense = mid_expense
        else:
            high_expense = mid_expense

    return optimal_expense

# End of financial_models.py
