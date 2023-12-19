import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from src.matrix import Matrix
from src.graph import Graph

window = tk.Tk()
window.title("My Window")
window.geometry("400x300")

# Add a label to the window
label = tk.Label(window, text="Enter the values of the matrix:")
label.pack()

# Add an entry widget to the window
entry = tk.Text(window, width=30)
entry.config(width=30, height=10)
entry.config(font=("Consolas",12), selectbackground="red", padx=5, pady=5)
entry.pack()

grafos = []
grafos_propios: list[Graph] = []

def create_graph():
    # Get the values from the entry widget
    values = entry.get(1.0, tk.END)
    # Convert the values to a list of integers
    matrix = [[int(x) for x in row.split()] for row in values.split('\n')]
    matrix.pop()
    new_matrix = Matrix(len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix.set_value(i, j, matrix[i][j])
    grafos_propios.append(new_matrix.to_graph())

    # Create a graph from the matrix
    print(matrix)
    grafos.append(nx.from_numpy_array(np.array(matrix)))
    # Draw the graph
    nx.draw(grafos[-1], with_labels=True, font_weight='bold', node_color='green', edge_color='red' )
    plt.show()

def compare_graphs():
    if len(grafos) < 2:
        return
    else:
        popup = tk.Toplevel()
        popup.title("Compare")
        popup.geometry("400x100")
        label = tk.Label(popup, text="The graphs are isomorphic" if nx.is_isomorphic(grafos[-2], grafos[-1]) else "The graphs are not isomorphic")
        label.pack()

        texto = ""
        if len(grafos_propios[-2].get_vertices()) == len(grafos_propios[-1].get_vertices()):
            texto += "The graphs have the same number of vertices\n"
            vertices_1, vertices_2 = 0, 0

            grados_1, grados_2 = [], []
            for vertice in grafos_propios[-2].get_vertices():
                grado = 0
                for arista in vertice.get_adyacents():
                    grado += 1
                    vertices_1 += 1
                grados_1.append(grado)
            
            for vertice in grafos_propios[-1].get_vertices():
                grado = 0
                for arista in vertice.get_adyacents():
                    grado += 1
                    vertices_2 += 1
                grados_2.append(grado)

            if vertices_1 == vertices_2:
                texto += "The graphs have the same number of edges\n"
            else:
                texto += "The graphs don't have the same number of edges\n"

            grados_1.sort()
            grados_2.sort()
            if grados_1 == grados_2:
                texto += "The graphs have the same degree sequence\n"
            else:
                texto += "The graphs don't have the same degree sequence\n"
            
        else:
            texto += "The graphs don't have the same number of vertices\n"
            
        propio = tk.Label(popup, text=texto)
        propio.pack()


compare = tk.Button(window, text="Copare",  command=compare_graphs)
compare.pack()

# Add a button to the window
button = tk.Button(window, text="Submit",  command=create_graph)
button.pack()

