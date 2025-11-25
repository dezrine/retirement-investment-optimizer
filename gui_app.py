# Project       :   Analysis of Algorithms
# Instructor    :   Oral Robinson
# Date          :   November , 2025
# Authors       :   Desrine Harripaul, Rackeel Brooks, Giomar Griffiths and Zemario Pascoe
# GUI Version   :   Tkinter-based graphical interface

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from financial_models import fixedInvestor, variableInvestor, finallyRetired, maximumExpensed


class RetirementOptimizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Retirement Optimization System")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        
        # Create header
        header = tk.Label(
            root,
            text="Retirement Investment Optimizer",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#008a15",
            pady=10
        )
        header.pack(fill=tk.X)
        
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs for each model
        self.create_fixed_investor_tab()
        self.create_variable_investor_tab()
        self.create_finally_retired_tab()
        self.create_maximum_expensed_tab()
    
    def create_fixed_investor_tab(self):
        """Tab 1: Fixed Growth Simulation"""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Fixed Growth")
        
        tk.Label(frame, text="Fixed Growth Simulation", font=("Arial", 12, "bold")).pack()
        tk.Label(frame, text="Calculates final balance with fixed annual interest rate", 
                 font=("Arial", 9), fg="gray").pack()
        
        # Principal
        tk.Label(frame, text="Initial Principal ($):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.fi_principal = tk.StringVar()
        ttk.Entry(frame, textvariable=self.fi_principal).pack(fill=tk.X)
        
        # Interest Rate
        tk.Label(frame, text="Annual Interest Rate (e.g., 0.05 for 5%):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.fi_rate = tk.StringVar()
        ttk.Entry(frame, textvariable=self.fi_rate).pack(fill=tk.X)
        
        # Annual Contribution
        tk.Label(frame, text="Annual Contribution ($):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.fi_contribution = tk.StringVar()
        ttk.Entry(frame, textvariable=self.fi_contribution).pack(fill=tk.X)
        
        # Years
        tk.Label(frame, text="Years to Retirement:", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.fi_years = tk.StringVar()
        ttk.Entry(frame, textvariable=self.fi_years).pack(fill=tk.X)
        
        # Button
        ttk.Button(frame, text="Calculate", command=self.calculate_fixed_investor).pack(pady=15)
        
        # Result
        self.fi_result = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#27ae60")
        self.fi_result.pack(pady=10)
    
    def create_variable_investor_tab(self):
        """Tab 2: Variable Growth Simulation"""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Variable Growth")
        
        tk.Label(frame, text="Variable Growth Simulation", font=("Arial", 12, "bold")).pack()
        tk.Label(frame, text="Calculates final balance with varying annual interest rates", 
                 font=("Arial", 9), fg="gray").pack()
        
        # Principal
        tk.Label(frame, text="Initial Principal ($):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.vi_principal = tk.StringVar()
        ttk.Entry(frame, textvariable=self.vi_principal).pack(fill=tk.X)
        
        # Interest Rates (comma-separated)
        tk.Label(frame, text="Annual Interest Rates (comma-separated, e.g., 0.05,0.04,0.06):", 
                 anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.vi_rates = tk.StringVar()
        ttk.Entry(frame, textvariable=self.vi_rates).pack(fill=tk.X)
        
        # Annual Contribution
        tk.Label(frame, text="Annual Contribution (%):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.vi_contribution = tk.StringVar()
        ttk.Entry(frame, textvariable=self.vi_contribution).pack(fill=tk.X)
        
        # Button
        ttk.Button(frame, text="Calculate", command=self.calculate_variable_investor).pack(pady=15)
        
        # Result
        self.vi_result = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#27ae60")
        self.vi_result.pack(pady=10)
    
    def create_finally_retired_tab(self):
        """Tab 3: Retirement Longevity"""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Retirement Longevity")
        
        tk.Label(frame, text="Retirement Longevity Analysis", font=("Arial", 12, "bold")).pack()
        tk.Label(frame, text="Determines how many years retirement funds will last", 
                 font=("Arial", 9), fg="gray").pack()
        
        # Starting Balance
        tk.Label(frame, text="Starting Balance ($):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.fr_balance = tk.StringVar()
        ttk.Entry(frame, textvariable=self.fr_balance).pack(fill=tk.X)
        
        # Annual Expense
        tk.Label(frame, text="Annual Expense ($):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.fr_expense = tk.StringVar()
        ttk.Entry(frame, textvariable=self.fr_expense).pack(fill=tk.X)
        
        # Interest Rate
        tk.Label(frame, text="Annual Interest Rate (e.g., 0.04 for 4%):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.fr_rate = tk.StringVar()
        ttk.Entry(frame, textvariable=self.fr_rate).pack(fill=tk.X)
        
        # Button
        ttk.Button(frame, text="Calculate", command=self.calculate_finally_retired).pack(pady=15)
        
        # Result
        self.fr_result = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#27ae60")
        self.fr_result.pack(pady=10)
    
    def create_maximum_expensed_tab(self):
        """Tab 4: Optimal Withdrawal Calculation"""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Max Withdrawal")
        
        tk.Label(frame, text="Optimal Withdrawal Calculation", font=("Arial", 12, "bold")).pack()
        tk.Label(frame, text="Finds maximum annual withdrawal for target retirement duration", 
                 font=("Arial", 9), fg="gray").pack()
        
        # Starting Balance
        tk.Label(frame, text="Starting Balance ($):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.me_balance = tk.StringVar()
        ttk.Entry(frame, textvariable=self.me_balance).pack(fill=tk.X)
        
        # Interest Rate
        tk.Label(frame, text="Annual Interest Rate (e.g., 0.04 for 4%):", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.me_rate = tk.StringVar()
        ttk.Entry(frame, textvariable=self.me_rate).pack(fill=tk.X)
        
        # Target Years
        tk.Label(frame, text="Target Retirement Years:", anchor="w").pack(fill=tk.X, pady=(10, 0))
        self.me_years = tk.StringVar(value="30")
        ttk.Entry(frame, textvariable=self.me_years).pack(fill=tk.X)
        
        # Button
        ttk.Button(frame, text="Calculate", command=self.calculate_maximum_expensed).pack(pady=15)
        
        # Result
        self.me_result = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#27ae60")
        self.me_result.pack(pady=10)
    
    def calculate_fixed_investor(self):
        """Calculate fixed investor model"""
        try:
            principal = float(self.fi_principal.get())
            rate = float(self.fi_rate.get())
            contribution = float(self.fi_contribution.get())
            years = int(self.fi_years.get())
            
            if years <= 0:
                raise ValueError("Years must be positive")
            
            result = fixedInvestor(principal, rate, years, contribution)
            self.fi_result.config(text=f"Final Balance: ${result:,.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            self.fi_result.config(text="")
    
    def calculate_variable_investor(self):
        """Calculate variable investor model"""
        try:
            principal = float(self.vi_principal.get())
            rates = [float(r.strip()) for r in self.vi_rates.get().split(",")]
            contribution = float(self.vi_contribution.get())
            
            if not rates:
                raise ValueError("Please provide at least one interest rate")
            
            result = variableInvestor(principal, rates, contribution)
            self.vi_result.config(text=f"Final Balance: ${result:,.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            self.vi_result.config(text="")
    
    def calculate_finally_retired(self):
        """Calculate finally retired model"""
        try:
            balance = float(self.fr_balance.get())
            expense = float(self.fr_expense.get())
            rate = float(self.fr_rate.get())
            
            result = finallyRetired(balance, expense, rate)
            self.fr_result.config(text=f"Retirement Duration: {result} years")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            self.fr_result.config(text="")
    
    def calculate_maximum_expensed(self):
        """Calculate maximum expensed model"""
        try:
            balance = float(self.me_balance.get())
            rate = float(self.me_rate.get())
            years = int(self.me_years.get())
            
            if years <= 0:
                raise ValueError("Years must be positive")
            
            result = maximumExpensed(balance, rate, years)
            self.me_result.config(text=f"Max Annual Withdrawal: ${result:,.2f}")
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            self.me_result.config(text="")


if __name__ == "__main__":
    root = tk.Tk()
    app = RetirementOptimizerGUI(root)
    root.mainloop()
