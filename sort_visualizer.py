import tkinter as tk
from tkinter import ttk, messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            yield data, [j, j+1]

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            yield data, [j+1, i]
        data[j + 1] = key
        yield data, [j+1, i]

def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            yield data, [min_idx, j]
        data[i], data[min_idx] = data[min_idx], data[i]
        yield data, [i, min_idx]

def merge_sort(data):
    def merge_sort_rec(data, l, r):
        if l < r:
            m = (l + r) // 2
            yield from merge_sort_rec(data, l, m)
            yield from merge_sort_rec(data, m + 1, r)
            yield from merge(data, l, m, r)

    def merge(data, l, m, r):
        left = data[l:m+1]
        right = data[m+1:r+1]
        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            yield data, list(range(l, r+1))
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
            yield data, list(range(l, r+1))
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
            yield data, list(range(l, r+1))

    return merge_sort_rec(data, 0, len(data)-1)

def quick_sort(data):
    def quick_sort_rec(data, low, high):
        if low < high:
            pi = partition(data, low, high)
            yield from quick_sort_rec(data, low, pi - 1)
            yield from quick_sort_rec(data, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            yield arr, [i, j]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        yield arr, [i + 1, high]
        return i + 1

    return quick_sort_rec(data, 0, len(data)-1)

# GUI App
class SortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Sorting Visualizer")

        self.algorithms = {
            "Bubble Sort": bubble_sort,
            "Insertion Sort": insertion_sort,
            "Selection Sort": selection_sort,
            "Merge Sort": merge_sort,
            "Quick Sort": quick_sort,
        }

        self.data = []
        self.sort_generator = None
        self.is_paused = False
        self.after_id = None

        self.setup_ui()

    def setup_ui(self):
        control_frame = tk.Frame(self.root, bg="white")
        control_frame.pack(pady=10)

        tk.Label(control_frame, text="Elements:", bg="white").grid(row=0, column=0)
        self.size_var = tk.StringVar(value="50")
        tk.Entry(control_frame, textvariable=self.size_var, width=5).grid(row=0, column=1)

        tk.Label(control_frame, text="Algorithm:", bg="white").grid(row=0, column=2)
        self.algo_menu = ttk.Combobox(control_frame, values=list(self.algorithms.keys()))
        self.algo_menu.grid(row=0, column=3)
        self.algo_menu.current(0)

        tk.Label(control_frame, text="Speed (ms):", bg="white").grid(row=0, column=4)
        self.speed_var = tk.StringVar(value="100")
        tk.Entry(control_frame, textvariable=self.speed_var, width=5).grid(row=0, column=5)

        tk.Button(control_frame, text="Generate", command=self.generate_data).grid(row=0, column=6, padx=5)
        self.start_btn = tk.Button(control_frame, text="Start", command=self.start_sorting)
        self.start_btn.grid(row=0, column=7, padx=5)
        self.pause_btn = tk.Button(control_frame, text="Pause", command=self.toggle_pause)
        self.pause_btn.grid(row=0, column=8, padx=5)

        # Chart
        self.figure, self.ax = plt.subplots(figsize=(9, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack()

    def generate_data(self):
        try:
            size = int(self.size_var.get())
            if size < 2 or size > 200:
                raise ValueError
            self.data = [random.randint(10, 100) for _ in range(size)]
            self.draw_data(self.data)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a number between 2 and 200")

    def draw_data(self, data, highlight=[]):
        self.ax.clear()
        colors = ["red" if i in highlight else "blue" for i in range(len(data))]
        self.ax.bar(range(len(data)), data, color=colors)
        self.ax.set_title("Sorting Visualization")
        self.canvas.draw()

    def start_sorting(self):
        if not self.data:
            messagebox.showwarning("Missing Data", "Generate data first.")
            return

        try:
            speed = int(self.speed_var.get())
        except ValueError:
            messagebox.showerror("Invalid Speed", "Enter a valid speed in milliseconds.")
            return

        algo_name = self.algo_menu.get()
        self.sort_generator = self.algorithms[algo_name](self.data.copy())
        self.start_btn.config(state=tk.DISABLED)
        self.pause_btn.config(text="Pause", state=tk.NORMAL)
        self.is_paused = False
        self.animate_sort(speed)

    def animate_sort(self, speed):
        if self.is_paused:
            return
        try:
            data, highlight = next(self.sort_generator)
            self.draw_data(data, highlight)
            self.after_id = self.root.after(speed, lambda: self.animate_sort(speed))
        except StopIteration:
            self.draw_data(self.data)
            self.start_btn.config(state=tk.NORMAL)
            self.pause_btn.config(state=tk.DISABLED)

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            if self.after_id:
                self.root.after_cancel(self.after_id)
            self.pause_btn.config(text="Resume")
        else:
            self.pause_btn.config(text="Pause")
            self.animate_sort(int(self.speed_var.get()))

# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizer(root)
    root.mainloop()
