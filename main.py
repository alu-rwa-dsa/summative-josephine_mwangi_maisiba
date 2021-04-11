# Authors: Samwel Maisiba, Modester Mwangi, Josephine Uwizeye
# GitHub Handles: Sammyiel, Modester-mw, Josephine-Uwizeye

# We are going to implement the maze game using undirected and unweighted graph

list1 = []


def traverse_vertices():
    for i in list1:
        print(i, end=' ')


def set_vertices(vertex):
    if vertex not in list1:
        list1.append(vertex)


class Graph:

    def __init__(self, current_vertex, pointed_vertex):
        self.current_vertex = current_vertex
        self.pointed_vertex = pointed_vertex

    set_vertices("A")
    set_vertices("B")
    set_vertices("C")
    set_vertices("D")
    set_vertices("E")
    set_vertices("F")


traverse_vertices()
