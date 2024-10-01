import customtkinter as ctk
from tkinter import messagebox
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class GraphApp:
    def __init__(self, root):
        self.graph = defaultdict(list)
        self.root = root
        self.root.title("Graph GUI with DFS Shreeraj-S075")
        ctk.set_appearance_mode("light")

        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        self.vertex_label = ctk.CTkLabel(root, text="Vertices (space-separated):")
        self.vertex_label.grid(row=0, column=0, padx=10, pady=10)
        self.vertex_entry = ctk.CTkEntry(root)
        self.vertex_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.edge_label = ctk.CTkLabel(root, text="Edges (A-B format):")
        self.edge_label.grid(row=1, column=0, padx=10, pady=10)
        self.edge_entry = ctk.CTkEntry(root)
        self.edge_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.add_vertex_button = ctk.CTkButton(root, text="Add Vertex", command=self.add_vertex)
        self.add_vertex_button.grid(row=2, column=0, padx=10, pady=10)

        self.add_edge_button = ctk.CTkButton(root, text="Add Edge", command=self.add_edge)
        self.add_edge_button.grid(row=2, column=1, padx=10, pady=10)

        self.display_button = ctk.CTkButton(root, text="Display Graph", command=self.display_graph)
        self.display_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.dfs_label = ctk.CTkLabel(root, text="Start Vertex for DFS:")
        self.dfs_label.grid(row=4, column=0, padx=10, pady=10)
        self.dfs_entry = ctk.CTkEntry(root)
        self.dfs_entry.grid(row=4, column=1, padx=10, pady=10)

        self.dfs_button = ctk.CTkButton(root, text="Run DFS", command=self.run_dfs)
        self.dfs_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.visualize_button = ctk.CTkButton(root, text="Visualize Graph and DFS", command=self.visualize_dfs_graph)
        self.visualize_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.name_label = ctk.CTkLabel(root, text="Shreeraj-S075")
        self.name_label.grid(row=7, column=0,sticky='w',padx=5)

    def add_vertex(self):
        vertices = self.vertex_entry.get().split()
        for vertex in vertices:
            if vertex not in self.graph:
                self.graph[vertex] = []
            else:
                messagebox.showwarning("Warning", f"Vertex {vertex} already exists.")
        messagebox.showinfo("Success", f"Vertex added.")
    

    def add_edge(self):
        edges = self.edge_entry.get().split()
        for i in edges:
            vertex1, vertex2 = i.split('-')
            if vertex1 in self.graph and vertex2 in self.graph:
                self.graph[vertex1].append(vertex2)
                self.graph[vertex2].append(vertex1)
            else:
                messagebox.showerror("Error", "One or both vertices not found.")
        messagebox.showinfo("Success", f"Edge added.")

    def display_graph(self):
        display_text = "\n".join([f"{vertex}: {edges}" for vertex, edges in self.graph.items()])
        messagebox.showinfo("Graph", display_text)

    def dfs_tree(self, start):
        visited = set()
        dfs_tree = defaultdict(list)

        def dfs(v):
            visited.add(v)
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    dfs_tree[v].append(neighbor)
                    dfs(neighbor)

        dfs(start)
        return dfs_tree

    def run_dfs(self):
        start_vertex = self.dfs_entry.get().strip()
        if start_vertex in self.graph:
            dfs_tree = self.dfs_tree(start_vertex)
            self.display_dfs_tree(dfs_tree, start_vertex)
        else:
            messagebox.showerror("Error", f"Start vertex {start_vertex} is not in the graph.")

    def display_dfs_tree(self, dfs_tree, start):
        display_text = f"Depth-First Tree starting from {start}:\n"
        display_text += "\n".join([f"{vertex}: {dfs_tree[vertex]}" for vertex in dfs_tree])
        messagebox.showinfo("DFS Tree", display_text)

    def visualize_dfs_graph(self):
        start_vertex = self.dfs_entry.get().strip()
        if start_vertex not in self.graph:
            messagebox.showerror("Error", f"Start vertex {start_vertex} is not in the graph.")
            return

        dfs_tree = self.dfs_tree(start_vertex)
        
        plt.figure(figsize=(12, 6))

        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G)
        plt.subplot(121)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=100, edge_color='gray', font_size=8, font_weight='bold')
        plt.title("Original Graph")

        T = nx.DiGraph(dfs_tree)
        plt.subplot(122)
        nx.draw(T, pos, with_labels=True, node_color='lightgreen', node_size=100, edge_color='blue', font_size=8, font_weight='bold', arrows=True)
        plt.title(f"DFS Tree starting from {start_vertex}")

        plt.gcf().canvas.manager.set_window_title(f"DFS Visualization from {start_vertex} by Shreeraj-S075")
        
        plt.show()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = GraphApp(root)
    root.mainloop()