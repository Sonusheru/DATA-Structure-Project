import tkinter as tk
from tkinter import messagebox

def create_node(data):
    return {'data': data, 'next': None}

def append(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    last = head
    while last['next']:
        last = last['next']
    last['next'] = new_node
    return head

def prepend(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    new_node['next'] = head
    return new_node

def delete(head, key):
    curr = head
    prev = None
    while curr:
        if curr['data'] == key:
            if prev:
                prev['next'] = curr['next']
            else:
                head = curr['next']
            return head
        prev = curr
        curr = curr['next']
    return head

def traverse(head):
    elems = []
    curr = head
    while curr:
        elems.append(curr['data'])
        curr = curr['next']
    return elems

class LinkedListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Singly Linked List GUI")
        self.head = None

        self.create_widgets()

    def create_widgets(self):
        self.append_label = tk.Label(self.root, text="Append Value:")
        self.append_label.grid(row=0, column=0)
        self.append_entry = tk.Entry(self.root)
        self.append_entry.grid(row=0, column=1)
        self.append_button = tk.Button(self.root, text="Append", command=self.append_value)
        self.append_button.grid(row=0, column=2)

        self.prepend_label = tk.Label(self.root, text="Prepend Value:")
        self.prepend_label.grid(row=1, column=0)
        self.prepend_entry = tk.Entry(self.root)
        self.prepend_entry.grid(row=1, column=1)
        self.prepend_button = tk.Button(self.root, text="Prepend", command=self.prepend_value)
        self.prepend_button.grid(row=1, column=2)

        self.delete_label = tk.Label(self.root, text="Delete Value:")
        self.delete_label.grid(row=2, column=0)
        self.delete_entry = tk.Entry(self.root)
        self.delete_entry.grid(row=2, column=1)
        self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_value)
        self.delete_button.grid(row=2, column=2)

        self.display_button = tk.Button(self.root, text="Display", command=self.display_list)
        self.display_button.grid(row=3, columnspan=3)

        self.result_label = tk.Label(self.root, text="Linked List:")
        self.result_label.grid(row=4, column=0)
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.grid(row=5, columnspan=3)

    def append_value(self):
        data = self.append_entry.get()
        if data:
            for value in data.split(','):
                self.head = append(self.head, value.strip())
            self.append_entry.delete(0, tk.END)
            self.display_list()

    def prepend_value(self):
        data = self.prepend_entry.get()
        if data:
            self.head = prepend(self.head, data)
            self.prepend_entry.delete(0, tk.END)
            self.display_list()

    def delete_value(self):
        key = self.delete_entry.get()
        if key:
            self.head = delete(self.head, key)
            self.delete_entry.delete(0, tk.END)
            self.display_list()

    def display_list(self):
        elems = traverse(self.head)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, " -> ".join(elems))

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListGUI(root)
    root.mainloop()