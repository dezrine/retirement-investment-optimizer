# retirement-investment-optimizer

AOA Group Project

## Running the Application

### GUI Version (Recommended) ⭐

```bash
python gui_app.py
```

This launches an interactive **Tkinter GUI** with 4 tabs:

- **Fixed Growth**: Calculate final balance with fixed annual interest rate + **interactive growth chart**
- **Variable Growth**: Model varying annual interest rates + **interactive growth chart**
- **Retirement Longevity**: Determine how many years funds will last
- **Max Withdrawal**: Find maximum sustainable annual withdrawal

#### Plotting Features (Bonus Marks)

The Fixed Growth and Variable Growth tabs include:

- **Interactive Charts**: Visualize portfolio growth over time with Matplotlib
- **Dual Series**: Compare total balance (with interest) vs. principal only (no interest)
- **Toolbar**: Zoom, pan, and interact with charts directly
- **Export**: Save plots as PNG or PDF for reports/presentations

To use plotting, install Matplotlib:

```bash
pip install matplotlib
```

### CLI Version (Terminal)

```bash
python main_app.py
```

### Windows UTF-8 Setup (Recommended for Emoji Display)

If you see garbled characters instead of emojis when running the app, enable UTF-8 mode:

#### Option 1: Temporary (Current Session Only)

```powershell
$env:PYTHONIOENCODING = 'utf-8'; python main_app.py
```

#### Option 2: Python 3.11+

```powershell
python -X utf8 main_app.py
```

#### Option 3: Windows Terminal (Recommended)

1. Open **Windows Terminal** (not Command Prompt)
2. Run:
   ```powershell
   python main_app.py
   ```
   Windows Terminal natively supports UTF-8 and will display emojis correctly.

#### Option 4: Permanent Environment Variable (All Sessions)

1. Press `Win + X` and select **System**
2. Go to **Advanced system settings** → **Environment variables**
3. Click **New** (User variables)
4. Set `Variable name:` `PYTHONIOENCODING` and `Variable value:` `utf-8`
5. Click OK and restart your terminal
6. Run: `python main_app.py`
