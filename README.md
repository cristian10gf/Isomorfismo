# Graph Comparison Project

This project aims to compare a graph with its adjacency matrix. It consists of two classes: `Graph` and `Matrix`, and a main file `main.py` that sets up a sample graph and compares it with its adjacency matrix.

## Project Structure

The project has the following file structure:

```
graph-comparison
├── src
│   ├── graph.py
│   ├── matrix.py
│   └── main.py
├── tests
│   ├── test_graph.py
│   └── test_matrix.py
├── .gitignore
├── README.md
└── requirements.txt
```

- `src/graph.py`: This file exports a class `Graph` which represents a graph. It has methods to add vertices and edges, get the adjacency matrix, and check if a vertex or edge exists.

- `src/matrix.py`: This file exports a class `Matrix` which represents an adjacency matrix. It has methods to set and get values, and to convert the matrix to a graph.

- `src/main.py`: This file is the entry point of the application. It creates instances of the `Graph` and `Matrix` classes, sets up a sample graph, and compares the graph with its adjacency matrix.

- `tests/test_graph.py`: This file contains unit tests for the `Graph` class. It tests the methods to add vertices and edges, get the adjacency matrix, and check if a vertex or edge exists.

- `tests/test_matrix.py`: This file contains unit tests for the `Matrix` class. It tests the methods to set and get values, and to convert the matrix to a graph.

- `.gitignore`: This file specifies the files and directories that should be ignored by git.

- `README.md`: This file contains the documentation for the project.

- `requirements.txt`: This file lists the dependencies required by the project.

## Usage

To use this project, clone the repository and install the dependencies listed in `requirements.txt`. Then, run `main.py` to see the comparison between a sample graph and its adjacency matrix.

## Contributions

Contributions to this project are welcome. Please submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.