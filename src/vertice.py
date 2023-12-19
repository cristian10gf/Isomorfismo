
class Vertice():
    def __init__(self, dato: int):
        self.__dato: int = dato
        self.__adyacents: list[Vertice] = []

    def add_adyacent(self, vertice: 'Vertice'):
        self.__adyacents.append(vertice)

    def get_dato(self) -> int:
        return self.__dato
    
    def get_adyacents(self) -> list['Vertice']:
        return self.__adyacents
    
    def __eq__(self, other: 'Vertice') -> bool:
        return self.__dato == other.get_dato()
    
    def __str__(self) -> str:
        return str(self.__dato) + f" -> {str([vertice.get_dato() for vertice in self.__adyacents])}"
    
    def __repr__(self) -> str:
        return self.__str__()
    
