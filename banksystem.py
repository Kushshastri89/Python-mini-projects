import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
from datetime import datetime

DB_FILE = "users.json"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Load or initialize users
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

class BankingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Enhanced Banking System")
        self.master.geometry("450x500")
        self.users = load_users()
        self.current_user = None

        self.show_login()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_login(self):
        self.clear_window()
        tk.Label(self.master, text="Login", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.master, text="Username").pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        tk.Label(self.master, text="Password").pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        tk.Button(self.master, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.master, text="New User? Register", command=self.show_register).pack()

    def show_register(self):
        self.clear_window()
        tk.Label(self.master, text="Register", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.master, text="Username").pack()
        self.new_username = tk.Entry(self.master)
        self.new_username.pack()

        tk.Label(self.master, text="Password").pack()
        self.new_password = tk.Entry(self.master, show="*")
        self.new_password.pack()

        tk.Button(self.master, text="Create Account", command=self.register).pack(pady=5)
        tk.Button(self.master, text="Back to Login", command=self.show_login).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            self.show_admin_panel()
            return

        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            self.users[username]["last_login"] = self.current_time()
            save_users(self.users)
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def register(self):
        username = self.new_username.get()
        password = self.new_password.get()

        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
            return
        if not username or not password:
            messagebox.showerror("Error", "Fill all fields.")
            return

        self.users[username] = {
            "password": password,
            "balance": 0,
            "created_on": self.current_time(),
            "last_login": "",
            "transactions": []
        }
        save_users(self.users)
        messagebox.showinfo("Success", "Account created!")
        self.show_login()

    def show_dashboard(self):
        self.clear_window()
        user = self.users[self.current_user]

        tk.Label(self.master, text=f"Welcome {self.current_user}", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.master, text=f"Balance: ₹{user['balance']}", font=("Arial", 14)).pack()
        tk.Label(self.master, text=f"Last Login: {user['last_login']}", font=("Arial", 10)).pack()
        tk.Label(self.master, text=f"Created On: {user['created_on']}", font=("Arial", 10)).pack()

        tk.Button(self.master, text="Deposit", command=self.deposit_window).pack(pady=5)
        tk.Button(self.master, text="Withdraw", command=self.withdraw_window).pack(pady=5)
        tk.Button(self.master, text="View Transactions", command=self.view_transactions).pack(pady=5)
        tk.Button(self.master, text="Logout", command=self.show_login).pack(pady=10)

    def deposit_window(self):
        amount = self.get_amount("Deposit")
        if amount:
            self.users[self.current_user]["balance"] += amount
            self.log_transaction("deposit", amount)
            save_users(self.users)
            self.show_dashboard()

    def withdraw_window(self):
        amount = self.get_amount("Withdraw")
        if amount:
            if self.users[self.current_user]["balance"] >= amount:
                self.users[self.current_user]["balance"] -= amount
                self.log_transaction("withdraw", amount)
                save_users(self.users)
                self.show_dashboard()
            else:
                messagebox.showerror("Error", "Insufficient balance!")

    def log_transaction(self, ttype, amount):
        self.users[self.current_user]["transactions"].append({
            "type": ttype,
            "amount": amount,
            "time": self.current_time()
        })

    def get_amount(self, title):
        try:
            amt = simpledialog.askinteger(title, f"Enter amount to {title.lower()}:", parent=self.master)
            if amt is not None and amt > 0:
                return amt
            else:
                messagebox.showerror("Invalid", "Enter a positive number.")
        except:
            messagebox.showerror("Error", "Invalid input.")
        return None

    def view_transactions(self):
        self.clear_window()
        tk.Label(self.master, text=f"{self.current_user} - Transaction History", font=("Arial", 16)).pack(pady=10)
        for txn in self.users[self.current_user]["transactions"]:
            tk.Label(self.master, text=f"{txn['time']} - {txn['type'].capitalize()} ₹{txn['amount']}").pack()
        tk.Button(self.master, text="Back", command=self.show_dashboard).pack(pady=10)

    def show_admin_panel(self):
        self.clear_window()
        tk.Label(self.master, text="Admin Panel", font=("Arial", 18)).pack(pady=10)

        users = load_users()
        for uname, udata in users.items():
            tk.Label(self.master, text=f"{uname} | ₹{udata['balance']} | {len(udata['transactions'])} Txns").pack()

        tk.Button(self.master, text="Logout", command=self.show_login).pack(pady=10)

    def current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Main
root = tk.Tk()
app = BankingApp(root)
root.mainloop()
