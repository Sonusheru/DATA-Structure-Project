
import customtkinter as ctk
from itertools import permutations
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

class TSP:
    def __init__(self, distance_matrix, point_names):
        self.distance_matrix = distance_matrix
        self.point_names = point_names
        self.num_points = len(distance_matrix)

    def calculate_total_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i]][route[i + 1]]
        total_distance += self.distance_matrix[route[-1]][route[0]]  # return to start point
        return total_distance

    def solve(self, method="brute_force"):
        if method == "brute_force":
            return self.brute_force()
        elif method == "greedy":
            return self.greedy()

    def brute_force(self):
        min_distance = math.inf
        best_route = None
        for perm in permutations(range(self.num_points)):
            current_distance = self.calculate_total_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                best_route = perm
        return best_route, min_distance

    def greedy(self, start_point=0):
        visited = [False] * self.num_points
        visited[start_point] = True
        route = [start_point]
        current_point = start_point
        total_distance = 0

        for _ in range(self.num_points - 1):
            next_point = None
            min_distance = math.inf
            for point in range(self.num_points):
                if not visited[point] and self.distance_matrix[current_point][point] < min_distance:
                    min_distance = self.distance_matrix[current_point][point]
                    next_point = point

            route.append(next_point)
            total_distance += min_distance
            visited[next_point] = True
            current_point = next_point

        total_distance += self.distance_matrix[current_point][start_point]
        route.append(start_point)
        return route, total_distance

class TSPApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TSP Solver with Custom Point Names")
        self.geometry("900x600")

        self.num_points_label = ctk.CTkLabel(self, text="Enter number of points:")
        self.num_points_label.pack(pady=10)

        self.num_points_entry = ctk.CTkEntry(self, width=100)
        self.num_points_entry.pack(pady=5)

        self.generate_button = ctk.CTkButton(self, text="Generate Matrix & Names", command=self.generate_matrix)
        self.generate_button.pack(pady=10)

        self.distance_matrix_entries = []
        self.point_name_entries = []
        self.result_textbox = ctk.CTkTextbox(self, height=200, width=600)
        self.result_textbox.pack(pady=10)

        self.solve_button = ctk.CTkButton(self, text="Solve TSP", command=self.solve_tsp)
        self.solve_button.pack(pady=5)

    def generate_matrix(self):
        try:
            self.num_points = int(self.num_points_entry.get())
        except ValueError:
            self.result_textbox.insert("end", "Please enter a valid number of points.\n")
            return

        self.clear_matrix()

        self.point_name_label = ctk.CTkLabel(self, text="Enter the names of the points:")
        self.point_name_label.pack(pady=5)

        for i in range(self.num_points):
            name_entry = ctk.CTkEntry(self, width=100)
            name_entry.pack(pady=2)
            self.point_name_entries.append(name_entry)

        self.distance_matrix_label = ctk.CTkLabel(self, text="Enter the distance matrix:")
        self.distance_matrix_label.pack(pady=10)

        matrix_frame = ctk.CTkFrame(self)
        matrix_frame.pack(pady=10)

        for i in range(self.num_points):
            row_entries = []
            for j in range(self.num_points):
                entry = ctk.CTkEntry(matrix_frame, width=50)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.distance_matrix_entries.append(row_entries)

    def clear_matrix(self):
        for row in self.distance_matrix_entries:
            for entry in row:
                entry.destroy()
        self.distance_matrix_entries = []
        for entry in self.point_name_entries:
            entry.destroy()
        self.point_name_entries = []

    def get_distance_matrix_and_names(self):
        distance_matrix = []
        point_names = []

        for entry in self.point_name_entries:
            point_names.append(entry.get())

        for i in range(self.num_points):
            row = []
            for j in range(self.num_points):
                try:
                    value = int(self.distance_matrix_entries[i][j].get())
                except ValueError:
                    self.result_textbox.insert("end", "Please enter valid distances.\n")
                    return None, None
                row.append(value)
            distance_matrix.append(row)

        return distance_matrix, point_names

    def solve_tsp(self):
        distance_matrix, point_names = self.get_distance_matrix_and_names()
        if distance_matrix is None or point_names is None:
            return

        tsp = TSP(distance_matrix, point_names)
        brute_force_route, brute_force_distance = tsp.solve(method="brute_force")
        greedy_route, greedy_distance = tsp.solve(method="greedy")

        self.display_result(brute_force_route, brute_force_distance, "Brute Force", point_names)
        self.display_result(greedy_route, greedy_distance, "Greedy", point_names)

        self.visualize_route(brute_force_route, point_names, distance_matrix, "Brute Force")
        self.visualize_route(greedy_route, point_names, distance_matrix, "Greedy")

    def display_result(self, route, distance, method, point_names):
        method_name = method.replace("_", " ").title()
        route_str = " -> ".join(f"{point_names[city]}" for city in route)
        result = f"{method_name} Method:\nOptimal Route: {route_str}\nTotal Distance: {distance}\n\n"
        self.result_textbox.insert("end", result)
        self.result_textbox.yview("end")

    def visualize_route(self, route, point_names, distance_matrix, title):
        new_window = ctk.CTkToplevel(self)
        new_window.title(title + " Route Visualization")
        new_window.geometry("900x500")

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.set_title(title)

        self.plot_route(ax, route, point_names, distance_matrix)

        canvas = FigureCanvasTkAgg(fig, master=new_window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def plot_route(self, ax, route, point_names, distance_matrix):
        coords = {i: (math.cos(2 * math.pi * i / len(point_names)), math.sin(2 * math.pi * i / len(point_names))) for i in range(len(point_names))}
        G = nx.DiGraph()

        for i in range(len(point_names)):
            G.add_node(i, pos=coords[i])

        edge_labels = {}
        for i in range(len(route) - 1):
            G.add_edge(route[i], route[i + 1], weight=distance_matrix[route[i]][route[i + 1]])
            edge_labels[(route[i], route[i + 1])] = distance_matrix[route[i]][route[i + 1]]

        G.add_edge(route[-1], route[0], weight=distance_matrix[route[-1]][route[0]])
        edge_labels[(route[-1], route[0])] = distance_matrix[route[-1]][route[0]]

        pos = nx.get_node_attributes(G, 'pos')

        nx.draw(G, pos, ax=ax, with_labels=False, node_color='skyblue', node_size=700)
        node_labels = {i: point_names[i] for i in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12)
        nx.draw_networkx_edges(G, pos, ax=ax, arrowstyle='->', arrowsize=20, edge_color='black')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)

        ax.set_aspect('equal')

if __name__ == "__main__":
    app = TSPApp()
    app.mainloop()