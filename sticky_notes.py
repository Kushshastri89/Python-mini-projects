import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

def save_note():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Saved", "Note saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save: {e}")

def open_note():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open: {e}")

def change_color():
    color = colorchooser.askcolor(title="Choose background color")[1]
    if color:
        text_area.config(bg=color)

# GUI Setup
root = tk.Tk()
root.title("Sticky Notes")
root.geometry("400x400")

# Text Area
text_area = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 14))
text_area.pack(expand=True, fill='both')

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(fill='x')

save_btn = tk.Button(btn_frame, text="Save", command=save_note)
save_btn.pack(side='left', padx=5, pady=5)

open_btn = tk.Button(btn_frame, text="Open", command=open_note)
open_btn.pack(side='left', padx=5)

color_btn = tk.Button(btn_frame, text="Color", command=change_color)
color_btn.pack(side='left', padx=5)

clear_btn = tk.Button(btn_frame, text="Clear", command=lambda: text_area.delete(1.0, tk.END))
clear_btn.pack(side='left', padx=5)

root.mainloop()
