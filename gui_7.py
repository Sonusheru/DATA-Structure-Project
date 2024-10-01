import heapq
import tkinter as tk
from tkinter import messagebox

pq = []

def update_display():
    if pq:
        items_str = "\n".join([f"{item} with priority {priority}" for priority, item in pq])
    else:
        items_str = "Queue is empty"
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, items_str)
    text_area.config(state=tk.DISABLED)

def enqueue_item():
    item = item_entry.get()
    priority = priority_entry.get()
    if item and priority:
        try:
            priority = int(priority)
            heapq.heappush(pq, (priority, item))
            item_entry.delete(0, tk.END)
            priority_entry.delete(0, tk.END)
            update_display()
        except ValueError:
            messagebox.showerror("Error", "Priority must be an integer")
    else:
        messagebox.showerror("Error", "Item and priority cannot be empty")

def dequeue_item():
    if pq:
        item = heapq.heappop(pq)[1]
        messagebox.showinfo("Success", f"Dequeued '{item}'")
        update_display()
    else:
        messagebox.showinfo("Info", "Queue is empty")

def peek_item():
    if pq:
        item = pq[0][1]
        messagebox.showinfo("Top Element", f"Element at the top: '{item}'")
    else:
        messagebox.showinfo("Info", "Queue is empty")

def check_is_empty():
    empty = len(pq) == 0
    messagebox.showinfo("Is Empty?", f"Is queue empty? {'Yes' if empty else 'No'}")

def get_size():
    size_ = len(pq)
    messagebox.showinfo("Queue Size", f"Queue size: {size_}")

def traverse_items():
    update_display()

root = tk.Tk()
root.title("Heapq Priority Queue")

main_frame = tk.Frame(root)
main_frame.pack(pady=20)

tk.Label(main_frame, text="Item:").grid(row=0, column=0, padx=10, pady=5)
item_entry = tk.Entry(main_frame)
item_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(main_frame, text="Priority:").grid(row=1, column=0, padx=10, pady=5)
priority_entry = tk.Entry(main_frame)
priority_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(main_frame, text="Enqueue", command=enqueue_item).grid(row=0, column=2, rowspan=2, padx=10, pady=5)
tk.Button(main_frame, text="Dequeue", command=dequeue_item).grid(row=2, column=0, columnspan=3, padx=10, pady=5)
tk.Button(main_frame, text="Peek", command=peek_item).grid(row=3, column=0, columnspan=3, padx=10, pady=5)
tk.Button(main_frame, text="Check if Empty", command=check_is_empty).grid(row=4, column=0, columnspan=3, padx=10, pady=5)
tk.Button(main_frame, text="Get Size", command=get_size).grid(row=5, column=0, columnspan=3, padx=10, pady=5)
tk.Button(main_frame, text="Traverse", command=traverse_items).grid(row=6, column=0, columnspan=3, padx=10, pady=5)

text_area = tk.Text(main_frame, height=10, width=50, state=tk.DISABLED)
text_area.grid(row=7, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()