from src.vertice import Vertice
from src.graph import Graph

class Matrix():
    def __init__(self, size):
        self.__size = size
        self.__matrix = [[0 for _ in range(size)] for _ in range(size)]

    def set_value(self, row: int, col: int, value: int = 1):
        self.__matrix[row][col] = value

    def get_value(self,row: int, col: int) -> int:
        return self.__matrix[row][col]
    
    def size(self) -> int:
        return self.__size
    
    def get_matrix(self) -> list[list[int]]:
        return self.__matrix
    
    def forEach(self, function: callable):
        for i in range(self.__size):
            for j in range(self.__size):
                function(i, j, self.__matrix[i][j])

    def to_graph(self) -> 'Graph':
        graph = Graph()
        for i in range(self.__size):
            graph.add_vertex(i)
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__matrix[i][j] != 0:
                    graph.add_edge(graph.vertex(i), graph.vertex(j))
        return graph