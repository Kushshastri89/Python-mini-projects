import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import StringVar

def calculate():
    try:
        rent = float(rent_var.get())
        utilities = float(util_var.get())
        roommates = int(roommates_var.get())

        total = rent + utilities
        share = total / roommates if roommates else total

        total_rent.set(f"₹ {total:.2f}")
        per_person.set(f"₹ {share:.2f}")
    except ValueError:
        total_rent.set("Invalid Input")
        per_person.set("—")

# Create App
app = tb.Window(themename="cyborg")
app.title("Modern Rent Calculator")
app.geometry("400x350")
app.resizable(False, False)

# Variables
rent_var = StringVar()
util_var = StringVar()
roommates_var = StringVar()
total_rent = StringVar()
per_person = StringVar()

# Title
tb.Label(app, text="Rent Split Calculator", font=("Helvetica", 18, "bold")).pack(pady=10)

# Inputs
frame = tb.Frame(app, padding=20)
frame.pack()

tb.Label(frame, text="Monthly Rent (₹):").grid(row=0, column=0, sticky=W, pady=5)
tb.Entry(frame, textvariable=rent_var, width=20).grid(row=0, column=1, pady=5)

tb.Label(frame, text="Utility Costs (₹):").grid(row=1, column=0, sticky=W, pady=5)
tb.Entry(frame, textvariable=util_var, width=20).grid(row=1, column=1, pady=5)

tb.Label(frame, text="Number of Roommates:").grid(row=2, column=0, sticky=W, pady=5)
tb.Entry(frame, textvariable=roommates_var, width=20).grid(row=2, column=1, pady=5)

# Calculate Button
tb.Button(app, text="Calculate", bootstyle=PRIMARY, command=calculate).pack(pady=10)

# Output
output_frame = tb.Frame(app, padding=10)
output_frame.pack()

tb.Label(output_frame, text="Total Rent:", font=("Segoe UI", 12)).grid(row=0, column=0, sticky=W)
tb.Label(output_frame, textvariable=total_rent, font=("Segoe UI", 12, "bold")).grid(row=0, column=1, sticky=W)

tb.Label(output_frame, text="Per Person:", font=("Segoe UI", 12)).grid(row=1, column=0, sticky=W)
tb.Label(output_frame, textvariable=per_person, font=("Segoe UI", 12, "bold")).grid(row=1, column=1, sticky=W)

# Run App
app.mainloop()
