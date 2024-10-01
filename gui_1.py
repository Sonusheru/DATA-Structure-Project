import tkinter as tk
from tkinter import messagebox

queue = []

def enqueue():
    element = entry.get()
    if element:
        queue.append(element)
        update_queue_display()
    else:
        messagebox.showwarning("Input Error", "Please enter an element to enqueue.")

def dequeue():
    if is_empty():
        messagebox.showinfo("Dequeue", "Queue is empty")
    else:
        result = queue.pop(0)
        messagebox.showinfo("Dequeue", result)
        update_queue_display()

def peek():
    if is_empty():
        messagebox.showinfo("Peek", "Queue is empty")
    else:
        messagebox.showinfo("Peek", queue[0])

def is_empty():
    return len(queue) == 0

def size():
    messagebox.showinfo("Size", len(queue))

def update_queue_display():
    queue_display.delete(1.0, tk.END)
    queue_display.insert(tk.END, str(queue))

root = tk.Tk()
root.title("Queue Operations")

frame = tk.Frame(root)
frame.pack(pady=20)

entry_label = tk.Label(frame, text="Element:")
entry_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame)
entry.grid(row=0, column=1, padx=5)

enqueue_button = tk.Button(frame, text="Enqueue", command=enqueue)
enqueue_button.grid(row=0, column=2, padx=5)

dequeue_button = tk.Button(frame, text="Dequeue", command=dequeue)
dequeue_button.grid(row=1, column=0, columnspan=3, pady=5)

peek_button = tk.Button(frame, text="Peek", command=peek)
peek_button.grid(row=2, column=0, columnspan=3, pady=5)

is_empty_button = tk.Button(frame, text="isEmpty", command=lambda: messagebox.showinfo("isEmpty", is_empty()))
is_empty_button.grid(row=3, column=0, columnspan=3, pady=5)

size_button = tk.Button(frame, text="Size", command=size)
size_button.grid(row=4, column=0, columnspan=3, pady=5)

queue_display = tk.Text(root, height=5, width=50)
queue_display.pack(pady=10)

update_queue_display()

root.mainloop()