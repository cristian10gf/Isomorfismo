from src.matrix import Matrix

def test_set_value():
    matrix = Matrix(3)
    matrix.set_value(0, 0, 1)
    assert matrix.get_value(0, 0) == 1

def test_get_value():
    matrix = Matrix(3)
    matrix.set_value(0, 0, 1)
    assert matrix.get_value(0, 0) == 1

def test_to_graph():
    matrix = Matrix(3)
    matrix.set_value(0, 1, 1)
    matrix.set_value(1, 2, 1)
    graph = matrix.to_graph()
    assert graph.get_adjacency_matrix() == matrix.get_matrix()

# intentionally left blank