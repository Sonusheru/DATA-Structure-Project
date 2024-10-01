import tkinter as tk
from tkinter import simpledialog, messagebox

class StackApp:
    def __init__(self, root):
        self.stack = []
        self.root = root
        self.root.title("Stack Operations")
        self.create_widgets()

    def create_widgets(self):
        self.push_button = tk.Button(self.root, text="Push", command=self.push)
        self.push_button.pack(pady=5)

        self.pop_button = tk.Button(self.root, text="Pop", command=self.pop)
        self.pop_button.pack(pady=5)

        self.display_button = tk.Button(self.root, text="Display", command=self.display)
        self.display_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search", command=self.search)
        self.search_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

        self.stack_display = tk.Label(self.root, text="", fg="blue")
        self.stack_display.pack(pady=10)

    def push(self):
        data = simpledialog.askstring("Input", "Enter values to push (comma-separated):")
        if data:
            for i in data.split(','):
                self.stack.append(int(i))
            self.display()

    def pop(self):
        if not self.is_empty():
            popped_value = self.stack.pop()
            messagebox.showinfo("Popped Value", f"Popped value: {popped_value}")
        else:
            messagebox.showwarning("Warning", "Stack is empty")
        self.display()

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        self.stack_display.config(text=f"Stack: {self.stack}")

    def search(self):
        if not self.is_empty():
            try:
                search_int = int(simpledialog.askstring("Input", "Enter a number to search:"))
                if search_int in self.stack:
                    position = self.stack.index(search_int)
                    messagebox.showinfo("Search Result", f"Number {search_int} found at position {position}")
                else:
                    messagebox.showinfo("Search Result", "Number not found")
            except ValueError:
                messagebox.showerror("Error", "Invalid input! Only numbers are accepted.")
        else:
            messagebox.showwarning("Warning", "Stack is empty")

if __name__ == "__main__":
    root = tk.Tk()
    app = StackApp(root)
    root.mainloop()