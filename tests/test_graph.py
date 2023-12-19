import unittest
from src.graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_vertex('C')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')

    def test_add_vertex(self):
        self.graph.add_vertex('D')
        self.assertTrue(self.graph.has_vertex('D'))

    def test_add_edge(self):
        self.graph.add_edge('A', 'C')
        self.assertTrue(self.graph.has_edge('A', 'C'))

    def test_has_vertex(self):
        self.assertTrue(self.graph.has_vertex('A'))
        self.assertFalse(self.graph.has_vertex('D'))

    def test_has_edge(self):
        self.assertTrue(self.graph.has_edge('B', 'C'))
        self.assertFalse(self.graph.has_edge('A', 'C'))

    def test_get_adjacency_matrix(self):
        expected_matrix = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        self.assertEqual(self.graph.get_adjacency_matrix(), expected_matrix)

if __name__ == '__main__':
    unittest.main()