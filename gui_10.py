import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox

class GraphApp:
    def __init__(self, root):
        self.graph = {}

        self.root = root
        self.root.title("Graph GUI Shreeraj-S075")
        ctk.set_appearance_mode("light")
        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        self.vertex_label = ctk.CTkLabel(root, text="Vertices (space-separated):")
        self.vertex_label.grid(row=0, column=0, padx=10, pady=10)
        self.vertex_entry = ctk.CTkEntry(root)
        self.vertex_entry.grid(row=0, column=1, padx=10, pady=10)
        self.vertex_entry.insert(0,'A B C D E F')
        
        self.edge_label = ctk.CTkLabel(root, text="Edges (A-B format):")
        self.edge_label.grid(row=1, column=0, padx=10, pady=10)
        self.edge_entry = ctk.CTkEntry(root)
        self.edge_entry.grid(row=1, column=1, padx=10, pady=10)
        self.edge_entry.insert(0,'A-B A-F B-C C-D D-E E-C')
        
        self.add_vertex_button = ctk.CTkButton(root, text="Add Vertex", command=self.add_vertex)
        self.add_vertex_button.grid(row=2, column=0, padx=10, pady=10)

        self.remove_vertex_button = ctk.CTkButton(root, text="Remove Vertex", command=self.remove_vertex)
        self.remove_vertex_button.grid(row=2, column=1, padx=10, pady=10)
        
        self.add_edge_button = ctk.CTkButton(root, text="Add Edge", command=self.add_edge)
        self.add_edge_button.grid(row=3, column=0, padx=10, pady=10)

        self.remove_edge_button = ctk.CTkButton(root, text="Remove Edge", command=self.remove_edge)
        self.remove_edge_button.grid(row=3, column=1, padx=10, pady=10)

        self.display_button = ctk.CTkButton(root, text="Display Graph", command=self.display_graph)
        self.display_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        self.visualize_button = ctk.CTkButton(root, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.name_label = ctk.CTkLabel(root, text="Shreeraj-S075")
        self.name_label.grid(row=6, column=0,sticky='w',padx=5)
    
    def add_vertex(self):
        vertices = self.vertex_entry.get().split()
        for vertex in vertices:
            if vertex not in self.graph:
                self.graph[vertex] = []
            else:
                messagebox.showwarning("Warning", f"Vertex {vertex} already exists.")
        messagebox.showinfo("Success", f"Vertices added.")
        
    
    def remove_vertex(self):
        vertices = self.vertex_entry.get().split()
        for vertex in vertices:
            if vertex in self.graph:
                for adjacent in list(self.graph[vertex]):
                    self.graph[adjacent].remove(vertex)
                del self.graph[vertex]
                messagebox.showinfo("Success", f"Vertex {vertex} removed.")
            else:
                messagebox.showwarning("Warning", f"Vertex {vertex} does not exist.")
    
    def add_edge(self):
        edges = self.edge_entry.get().split()
        for i in edges:
            vertex1, vertex2 = i.split('-')
            if vertex1 in self.graph and vertex2 in self.graph:
                if vertex2 not in self.graph[vertex1]:
                    self.graph[vertex1].append(vertex2)
                if vertex1 not in self.graph[vertex2]:
                    self.graph[vertex2].append(vertex1)
            else:
                messagebox.showerror("Error", "One or both vertices not found.")
                print(vertex1,vertex2)
        messagebox.showinfo("Success", f"Edge's added.")
        
    def remove_edge(self):
        edge = self.edge_entry.get().split('-')
        if len(edge) == 2:
            vertex1, vertex2 = edge
            if vertex1 in self.graph and vertex2 in self.graph:
                if vertex2 in self.graph[vertex1]:
                    self.graph[vertex1].remove(vertex2)
                if vertex1 in self.graph[vertex2]:
                    self.graph[vertex2].remove(vertex1)
                messagebox.showinfo("Success", f"Edge between {vertex1} and {vertex2} removed.")
            else:
                messagebox.showerror("Error", "One or both vertices not found.")
        else:
            messagebox.showerror("Error", "Please enter a valid edge format (A-B).")
    
    def display_graph(self):
        display_text = "\n".join([f"{vertex}: {edges}" for vertex, edges in self.graph.items()])
        messagebox.showinfo("Graph", display_text)
    
    def visualize_graph(self):
        G = nx.Graph(self.graph)
        plt.figure(figsize=(2, 4))
        plt.title("Graph Visualization Shreeraj-S075")
        plt.xlabel("Average Pulse")
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', font_size=8, font_weight='bold')
        plt.show()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = GraphApp(root)
    root.mainloop()