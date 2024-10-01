import customtkinter as ctk
import heapq
from collections import Counter

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}

    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = ''.join(codebook[char] for char in data)

    return encoded_data, codebook, root

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""

    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            current_code = ""

    return decoded_data

def draw_tree(canvas, node, x, y, x_offset, y_offset, path=""):
    if node.left:
        canvas.create_line(x, y, x - x_offset, y + y_offset, fill="black")
        canvas.create_text((x + x - x_offset) / 2, (y + y + y_offset) / 2, text="0", font=("Arial", 12),fill="black")
        draw_tree(canvas, node.left, x - x_offset, y + y_offset, x_offset // 2, y_offset, path + "0")
    if node.right:
        canvas.create_line(x, y, x + x_offset, y + y_offset, fill="black")
        canvas.create_text((x + x + x_offset) / 2, (y + y + y_offset) / 2, text="1", font=("Arial", 12),fill="black")
        draw_tree(canvas, node.right, x + x_offset, y + y_offset, x_offset // 2, y_offset, path + "1")

    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="lightblue", outline="black")
    
    if node.char is not None:
        canvas.create_text(x, y, text=f'{node.char}\n{node.freq}', font=("Arial", 10, "bold"))
    else:
        canvas.create_text(x, y, text=node.freq, font=("Arial", 10))

class HuffmanGUI(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Huffman Encoding GUI with Tree Visualization")
        self.geometry("1000x900")

        self.label = ctk.CTkLabel(self, text="Enter text to encode:")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, width=800)
        self.entry.pack(pady=10)

        self.encode_button = ctk.CTkButton(self, text="Encode", command=self.encode_text)
        self.encode_button.pack(pady=10)

        self.canvas = ctk.CTkCanvas(self, width=960, height=400, bg="white")
        self.canvas.pack(pady=20)

        self.encoded_label = ctk.CTkLabel(self, text="Encoded Data:")
        self.encoded_label.pack(pady=10)

        self.encoded_output = ctk.CTkTextbox(self, height=50, width=900)
        self.encoded_output.pack(pady=10)

        self.codebook_label = ctk.CTkLabel(self, text="Codebook:")
        self.codebook_label.pack(pady=10)

        self.codebook_output = ctk.CTkTextbox(self, height=100, width=900)
        self.codebook_output.pack(pady=10)

    def encode_text(self):
        data = self.entry.get()

        self.canvas.delete("all")

        encoded_data, codebook, root = huffman_encoding(data)

        self.encoded_output.delete("1.0", ctk.END)
        self.encoded_output.insert(ctk.END, encoded_data)

        if root:
            draw_tree(self.canvas, root, x=480, y=20, x_offset=240, y_offset=80)

        self.codebook_output.delete("1.0", ctk.END)
        for char, code in codebook.items():
            self.codebook_output.insert(ctk.END, f'{char}: {code},')

if __name__ == "__main__":
    app = HuffmanGUI()
    app.mainloop()

