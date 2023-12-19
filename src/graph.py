from src.vertice import Vertice

class Graph():
    def __init__(self) -> None:
        self.__vertices: list[Vertice] = []
        self.__adjacency_matrix = []

    def add_vertex(self, vertex: int) -> None:
        vertice = Vertice(vertex)
        self.__vertices.append(vertice)

    def add_vertexs(self, vertexs: list[int]) -> None:
        for vertex in vertexs:
            self.add_vertex(vertex)

    def add_edge(self, vertex1: Vertice, vertex2: Vertice) -> None:
        if vertex1 not in self.__vertices:
            self.add_vertex(vertex1.get_dato())
        if vertex2 not in self.__vertices:
            self.add_vertex(vertex2.get_dato())
        vertex1.add_adyacent(vertex2)

    def get_adjacency_matrix(self) -> list[list[int]]:
        for vertice in self.__vertices:
            row = []
            for vertice2 in self.__vertices:
                    if vertice2 in vertice.get_adyacents():
                        row.append(1)
                    else:
                        row.append(0)
            self.__adjacency_matrix.append(row)
        return self.__adjacency_matrix
    
    def get_vertices(self) -> list[Vertice]:
        return self.__vertices
    
    def vertex(self, vertex: int):
        for vertice in self.__vertices:
            if vertice.get_dato() == vertex:
                return vertice
    
    def __eq__(self, other: 'Graph') -> bool:
        if len(self.__vertices) != len(other.get_vertices()):
            return False
        for vertice in self.__vertices:
            if vertice not in other.get_vertices():
                return False
        return True
    
    def __str__(self) -> str:
        nodos = ""
        for vertice in self.__vertices:
            nodos += str(vertice) + ", "
        nodos = nodos[:-2]
        return nodos
    
    def __repr__(self) -> str:
        return self.__str__()
    
