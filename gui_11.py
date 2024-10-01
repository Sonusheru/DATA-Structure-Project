import customtkinter as ctk
from collections import deque, defaultdict
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

class GraphApp:
    def __init__(self, root):
        self.graph = defaultdict(list)
        self.root = root
        self.root.title("Graph GUI with BFS Shreeraj-S075")
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

        self.bfs_label = ctk.CTkLabel(root, text="Start Vertex for BFS:")
        self.bfs_label.grid(row=4, column=0, padx=10, pady=10)
        self.bfs_entry = ctk.CTkEntry(root)
        self.bfs_entry.grid(row=4, column=1, padx=10, pady=10)

        self.bfs_button = ctk.CTkButton(root, text="Run BFS", command=self.run_bfs)
        self.bfs_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.visualize_button = ctk.CTkButton(root, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        
        self.visualize_bfs_button = ctk.CTkButton(root, text="Visualize BFS Graph", command=self.visualize_bfs_graph)
        self.visualize_bfs_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.name_label = ctk.CTkLabel(root, text="Shreeraj-S075")
        self.name_label.grid(row=8, column=0,sticky='w',padx=5)

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

    def bfs_tree(self, start):
        visited = set()
        bfs_tree = defaultdict(list)
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    bfs_tree[current].append(neighbor)
                    queue.append(neighbor)

        return bfs_tree

    def run_bfs(self):
        start_vertex = self.bfs_entry.get().strip()
        if start_vertex in self.graph:
            bfs_tree = self.bfs_tree(start_vertex)
            self.display_bfs_tree(bfs_tree, start_vertex)
        else:
            messagebox.showerror("Error", f"Start vertex {start_vertex} is not in the graph.")

    def display_bfs_tree(self, bfs_tree, start):
        display_text = f"Breadth-First Tree starting from {start}:\n"
        display_text += "\n".join([f"{vertex}: {bfs_tree[vertex]}" for vertex in bfs_tree])
        messagebox.showinfo("BFS Tree", display_text)

    def visualize_graph(self):
        G = nx.Graph(self.graph)
        plt.figure(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray', font_size=15, font_weight='bold')
        
        plt.gcf().canvas.manager.set_window_title("Graph Visualization by [Your Name]")
        
        plt.show()

    def visualize_bfs_graph(self):
        start_vertex = self.bfs_entry.get().strip()
        if start_vertex not in self.graph:
            messagebox.showerror("Error", f"Start vertex {start_vertex} is not in the graph.")
            return

        bfs_tree = self.bfs_tree(start_vertex)
        
        bfs_graph = nx.DiGraph()
        for vertex, neighbors in bfs_tree.items():
            for neighbor in neighbors:
                bfs_graph.add_edge(vertex, neighbor)

        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(bfs_graph)
        nx.draw(bfs_graph, pos, with_labels=True, node_color='lightgreen', node_size=1000, edge_color='black', arrows=True, font_size=8, font_weight='bold')
        
        plt.gcf().canvas.manager.set_window_title(f"BFS Visualization from {start_vertex} by Shreeraj-S075")

        plt.show()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    app = GraphApp(root)
    root.mainloop()