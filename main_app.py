# Project       :   Analysis of Algorithms
# Instructor    :   Oral Robinson
# Date          :   November , 2025
# Authors       :   Desrine Harripaul, Rackeel Brooks, Giomar Griffiths and Zemario Pascoe

import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import cli_handlers 

def main_menu():
    """
    Displays the welcome message, executes the 5-second delay, 
    and then starts the interactive menu loop.
    """
    
    # --- 1. Welcome Message ---
    print("\n\n=====================================================")
    print("👋 Welcome to the CIT3003 Retirement Optimization System")
    print("=====================================================")
    
    # --- 2. Delay for 5 seconds ---
    print("\nSystem loading... please give us a moment...")
    time.sleep(2)
    
    # --- 3. Main Menu Loop ---
    while True:
        print("\n\n======================= MENU ========================")
        print("Please select the financial model you wish to execute:")
        print("1. Fixed Growth Simulation (fixedInvestor)")
        print("2. Variable Growth Simulation (variableInvestor)")
        print("3. Retirement Longevity (finallyRetired)")
        print("4. Optimal Withdrawal Calculation (maximumExpensed)")
        print("5. Exit Application")
        print("=====================================================")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            cli_handlers.handle_fixed_investor()
        elif choice == '2':
            cli_handlers.handle_variable_investor()
        elif choice == '3':
            cli_handlers.handle_finally_retired()
        elif choice == '4':
            cli_handlers.handle_maximum_expensed()
        elif choice == '5':
            print("\nThank you for using the Retirement Optimizer. Goodbye! 👋\n")
            break
        else:
            print("\n[ERROR] Invalid selection. Please enter a number between 1 and 5.")

# --- Application Entry Point ---
if __name__ == "__main__":
    main_menu()