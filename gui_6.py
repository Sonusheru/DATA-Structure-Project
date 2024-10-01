import tkinter as tk
from tkinter import messagebox

queue = []

def enqueue():
    element = entry_operation.get()
    priority = entry_priority.get()
    if element and priority:
        queue.append((element, int(priority)))
        queue.sort(key=lambda x: x[1])
        update_queue_display()
        entry_operation.delete(0, tk.END)
        entry_priority.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both operation and priority.")

def dequeue():
    if not queue:
        messagebox.showinfo("Dequeue", "Queue is empty")
    else:
        result = queue.pop(0)
        messagebox.showinfo("Dequeue", f"Dequeued: {result}")
        update_queue_display()

def peek():
    if not queue:
        messagebox.showinfo("Peek", "Queue is empty")
    else:
        result = queue[0]
        messagebox.showinfo("Peek", f"Peek: {result}")

def is_empty():
    if len(queue) == 0:
        messagebox.showinfo("Is Empty", 'Queue is Empty')
    else:
        messagebox.showinfo("Is Empty", 'Queue is not Empty')


def size():
    result = len(queue)
    messagebox.showinfo("Size", result)

def traverse():
    if not queue:
        messagebox.showinfo("Queue", "Queue is empty")
    else:
        result = "\n".join([f'Operation {i[0]} with priority {i[1]}' for i in queue])
        messagebox.showinfo("Queue", result)

def update_queue_display():
    queue_display.delete(1.0, tk.END)
    if queue:
        queue_display.insert(tk.END, "\n".join([f'Operation {i[0]} with priority {i[1]}' for i in queue]))

root = tk.Tk()
root.title("Priority Queue Operations")

frame = tk.Frame(root)
frame.pack(pady=20)

entry_label_operation = tk.Label(frame, text="Operation:")
entry_label_operation.grid(row=0, column=0, padx=5)

entry_operation = tk.Entry(frame)
entry_operation.grid(row=0, column=1, padx=5)

entry_label_priority = tk.Label(frame, text="Priority:")
entry_label_priority.grid(row=1, column=0, padx=5)

entry_priority = tk.Entry(frame)
entry_priority.grid(row=1, column=1, padx=5)

enqueue_button = tk.Button(frame, text="Enqueue", command=enqueue)
enqueue_button.grid(row=2, column=0, padx=5, pady=5)

dequeue_button = tk.Button(frame, text="Dequeue", command=dequeue)
dequeue_button.grid(row=2, column=1, padx=5, pady=5)

peek_button = tk.Button(frame, text="Peek", command=peek)
peek_button.grid(row=3, column=0, padx=5, pady=5)

is_empty_button = tk.Button(frame, text="Is Empty", command=is_empty)
is_empty_button.grid(row=3, column=1, padx=5, pady=5)

size_button = tk.Button(frame, text="Size", command=size)
size_button.grid(row=4, column=0, padx=5, pady=5)

traverse_button = tk.Button(frame, text="Traverse", command=traverse)
traverse_button.grid(row=4, column=1, padx=5, pady=5)

queue_display = tk.Text(root, height=10, width=50)
queue_display.pack(pady=20)

root.mainloop()