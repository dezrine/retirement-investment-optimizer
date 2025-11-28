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

# Optional plotting support
try:
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    PLOTTING_AVAILABLE = True
except Exception:
    PLOTTING_AVAILABLE = False


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
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="Calculate", command=self.calculate_fixed_investor).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(btn_frame, text="Plot Growth", command=self.plot_fixed_investor).pack(side=tk.LEFT)
        
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
        btn_frame = ttk.Frame(frame)
        btn_frame.pack(pady=15)
        ttk.Button(btn_frame, text="Calculate", command=self.calculate_variable_investor).pack(side=tk.LEFT, padx=(0, 8))
        ttk.Button(btn_frame, text="Plot Growth", command=self.plot_variable_investor).pack(side=tk.LEFT)
        
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
            # store last computed series for plotting
            self._last_fixed = dict(principal=principal, rate=rate, contribution=contribution, years=years)
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
            # store last computed series for plotting
            self._last_variable = dict(principal=principal, rates=rates, contribution=contribution)
        except ValueError as e:
            messagebox.showerror("Input Error", f"Invalid input: {e}")
            self.vi_result.config(text="")

    # --- Plotting helpers ---
    def _plot_window(self, title, years, balances, principal_only=None):
        if not PLOTTING_AVAILABLE:
            messagebox.showerror("Plotting Unavailable", "Matplotlib is not installed. Install it with: pip install matplotlib")
            return

        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("700x550")
        
        fig, ax = plt.subplots(figsize=(7, 5), dpi=100)
        ax.plot(years, balances, marker='o', linewidth=2, label='Total Balance (with interest/contributions)', color='#27ae60')
        
        # Plot principal-only comparison if provided
        if principal_only is not None:
            ax.plot(years, principal_only, marker='s', linewidth=2, label='Principal Only (no interest)', color='#e74c3c', linestyle='--')
            ax.legend(loc='upper left')
        
        ax.set_xlabel('Year', fontsize=11)
        ax.set_ylabel('Balance ($)', fontsize=11)
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K' if x >= 1000 else f'${x:.0f}'))

        canvas = FigureCanvasTkAgg(fig, master=win)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add toolbar
        from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
        toolbar = NavigationToolbar2Tk(canvas, win)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Add export button
        btn_frame = ttk.Frame(win)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Button(btn_frame, text="Export as PNG", command=lambda: self._export_plot(fig, title)).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Export as PDF", command=lambda: self._export_plot(fig, title, fmt='pdf')).pack(side=tk.LEFT)
        
        canvas.draw()

    def plot_fixed_investor(self):
        # Build the yearly balances using the same logic as fixedInvestor
        info = getattr(self, '_last_fixed', None)
        if info is None:
            messagebox.showinfo('Plot Info', 'Run Calculate first to generate data to plot.')
            return

        principal = info['principal']
        rate = info['rate']
        contribution = info['contribution']
        years = info['years']

        balances = []
        principal_only = []
        bal = principal
        prin = principal
        for y in range(1, years + 1):
            bal = bal * (1 + rate) + contribution
            prin = prin + contribution
            balances.append(bal)
            principal_only.append(prin)

        yrs = list(range(1, years + 1))
        self._plot_window('Fixed Growth Curve', yrs, balances, principal_only)

    def plot_variable_investor(self):
        info = getattr(self, '_last_variable', None)
        if info is None:
            messagebox.showinfo('Plot Info', 'Run Calculate first to generate data to plot.')
            return

        principal = info['principal']
        rates = info['rates']
        contribution = info['contribution']

        balances = []
        principal_only = []
        bal = principal
        prin = principal
        for i, r in enumerate(rates, start=1):
            bal = bal * (1 + r) + contribution
            prin = prin + contribution
            balances.append(bal)
            principal_only.append(prin)

        yrs = list(range(1, len(rates) + 1))
        self._plot_window('Variable Growth Curve', yrs, balances, principal_only)

    def _export_plot(self, fig, title, fmt='png'):
        """Export the plot to a file (PNG or PDF)."""
        from tkinter import filedialog
        file_ext = f".{fmt}"
        default_name = title.replace(' ', '_').lower() + file_ext
        file_path = filedialog.asksaveasfilename(
            defaultextension=file_ext,
            filetypes=[(f"{fmt.upper()} files", f"*{file_ext}"), ("All files", "*.*")],
            initialfile=default_name
        )
        if file_path:
            try:
                fig.savefig(file_path, format=fmt, dpi=150, bbox_inches='tight')
                messagebox.showinfo("Export Successful", f"Plot exported to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Export Failed", f"Could not export: {e}")
    
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
