import tkinter as tk
from tkinter import simpledialog, messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        curr = self.head 
        while curr:
            if curr.data == key and curr == self.head:
                if not curr.next:
                    curr = None
                    self.head = None
                    return
                else:
                    next_node = curr.next
                    curr.next = None
                    next_node.prev = None
                    curr = None
                    self.head = next_node
                    return
            elif curr.data == key:
                if curr.next:
                    prev = curr.prev
                    next_node = curr.next
                    prev.next = next_node
                    next_node.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None
                    return
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return
            curr = curr.next

    def traverse(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next
        return elems

class DLLApp:
    def __init__(self, root):
        self.dll = DoublyLinkedList()
        self.root = root
        self.root.title("Doubly Linked List GUI")

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.append_button = tk.Button(self.frame, text="Append", command=self.append_node)
        self.append_button.grid(row=0, column=0, padx=5, pady=5)

        self.prepend_button = tk.Button(self.frame, text="Prepend", command=self.prepend_node)
        self.prepend_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete_node)
        self.delete_button.grid(row=0, column=2, padx=5, pady=5)

        self.display_button = tk.Button(self.frame, text="Display", command=self.display_list)
        self.display_button.grid(row=0, column=3, padx=5, pady=5)

        self.exit_button = tk.Button(self.frame, text="Exit", command=root.quit)
        self.exit_button.grid(row=0, column=4, padx=5, pady=5)

    def append_node(self):
        data = simpledialog.askstring("Append", "Enter the value to append:")
        if data:
            for value in data.split(','):
                self.dll.append(value.strip())

    def prepend_node(self):
        data = simpledialog.askstring("Prepend", "Enter the value to prepend:")
        if data:
            self.dll.prepend(data.strip())

    def delete_node(self):
        data = simpledialog.askstring("Delete", "Enter the value to delete:")
        if data:
            self.dll.delete(data.strip())

    def display_list(self):
        elems = self.dll.traverse()
        messagebox.showinfo("Doubly Linked List", " <--> ".join(elems))

if __name__ == "__main__":
    root = tk.Tk()
    app = DLLApp(root)
    root.mainloop()
