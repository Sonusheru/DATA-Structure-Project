import customtkinter as ctk

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value
        return f"Inserted {value} at index {index}"

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            deleted_value = self.table[index]
            self.table[index] = None
            return f"Deleted {deleted_value} from index {index}"
        else:
            return "No element found at that index."

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            return f"Found {self.table[index]} at index {index}"
        else:
            return "No element found at that index."

    def traverse(self):
        return [f"{index}: {value}" if value else f"{index}: " for index, value in enumerate(self.table)]


class HashTableApp(ctk.CTk):
    def __init__(self, hash_table_size):
        super().__init__()
        self.hash_table = HashTable(hash_table_size)
        self.title("Hash Table GUI")
        self.geometry("500x400")

        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.pack(pady=10)
        self.display_labels = []
        for i in range(hash_table_size):
            lbl = ctk.CTkLabel(self.display_frame, text=f"{i}: ")
            lbl.grid(row=i // 2, column=i % 2, padx=10, pady=5)
            self.display_labels.append(lbl)

        self.input_entry = ctk.CTkEntry(self, placeholder_text="Enter key:value or key")
        self.input_entry.pack(pady=10)

        self.btn_frame = ctk.CTkFrame(self)
        self.btn_frame.pack(pady=10)

        self.insert_button = ctk.CTkButton(self.btn_frame, text="Insert", command=lambda: self.process_input("insert"))
        self.insert_button.grid(row=0, column=0, padx=10)

        self.delete_button = ctk.CTkButton(self.btn_frame, text="Delete", command=lambda: self.process_input("delete"))
        self.delete_button.grid(row=0, column=1, padx=10)

        self.search_button = ctk.CTkButton(self.btn_frame, text="Search", command=lambda: self.process_input("search"))
        self.search_button.grid(row=0, column=2, padx=10)

        self.size_button = ctk.CTkButton(self.btn_frame, text="Size", command=self.display_size)
        self.size_button.grid(row=0, column=3, padx=10)

        self.output_label = ctk.CTkLabel(self, text="")
        self.output_label.pack(pady=10)

        self.refresh_table()

    def process_input(self, operation):
        input_data = self.input_entry.get()
        if operation == "insert" and ":" in input_data:
            key, value = input_data.split(":")
            result = self.hash_table.insert(int(key), value)
        elif operation in ["delete", "search"] and input_data.isdigit():
            key = int(input_data)
            if operation == "delete":
                result = self.hash_table.delete(key)
            elif operation == "search":
                result = self.hash_table.search(key)
        else:
            result = "Invalid input or format."

        self.output_label.configure(text=result)
        self.refresh_table()

    def display_size(self):
        size = len([i for i in self.hash_table.table if i is not None])
        self.output_label.configure(text=f"HashTable Size: {size}")

    def refresh_table(self):
        table_data = self.hash_table.traverse()
        for i, lbl in enumerate(self.display_labels):
            lbl.configure(text=table_data[i])


if __name__ == "__main__":
    app = HashTableApp(10)
    app.mainloop()