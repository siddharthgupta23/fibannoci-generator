

import tkinter as tk
from tkinter import ttk
from fibonacci_generator import fibonacci_sequence  # Importing the function

class FibonacciGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Generator")
        
        self.label = ttk.Label(self.root, text="Enter the number of Fibonacci numbers:")
        self.label.pack(pady=56)
        
        self.entry = ttk.Entry(self.root)
        self.entry.pack(pady=56)
        
        self.generate_button = ttk.Button(self.root, text="Generate Fibonacci Series", command=self.generate_fibonacci)
        self.generate_button.pack(pady=56)
        
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=56)
        
    def generate_fibonacci(self):
        try:
            count = int(self.entry.get())
            if count <= 0:
                raise ValueError("Please enter a positive integer.")
            
            fibonacci_numbers = fibonacci_sequence(count)
            self.result_label.config(text=f"Fibonacci Series: {fibonacci_numbers}")
            
        except ValueError as e:
            self.result_label.config(text=str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FibonacciGeneratorApp(root)
    root.mainloop()
