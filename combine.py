import customtkinter as ctk
import tkinter as tk
import subprocess

def run_python_file(file_name):
    subprocess.Popen(['python3', file_name])

ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue") 

btn_names = ['ADT', 'Stack', 'Singly Linked List', 'Doubly Linked List', 'Queue', 'Priority Queue', 
             'Heapq Priority Queue', 'BinaryTree', 'Huffman Encoding', 'Graph', 'Graph BFS', 
             'Graph DFS', 'TSPApp', 'HashTable(No Collision)', 'HashTable(Collision)']

root = ctk.CTk()
root.title("Data Structures")
root.geometry("400x600")

main_frame = ctk.CTkFrame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ctk.CTkScrollbar(main_frame, orientation="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

scrollable_frame = ctk.CTkFrame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=scrollable_frame, anchor="n", width=400) 

label = ctk.CTkLabel(scrollable_frame, text="Click the DataStruture Button you want", font=("Arial", 16))
label.pack(pady=20)

for i, name in enumerate(btn_names):
    file_name = f'Ds proj/gui_{i+1}.py' 
    button = ctk.CTkButton(scrollable_frame, text=name, command=lambda file_name=file_name: run_python_file(file_name), width=250, height=40)
    button.pack(pady=10)

root.mainloop()
