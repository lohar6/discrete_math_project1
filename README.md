# Discrete Mathematics II - Project Delivery 1

This project implements undirected and directed graphs in Python without using external graph libraries, managed with **uv**.

## Project Structure

* `data/example_graph.txt`: Text file with the test graph (`source,target,weight`).
* `src/project_oned_iscrete/graph.py`: Main `Graph` class with the graph structure and verification functions.
* `main.py`: Script used to load the file and test all functions.

## Why I Chose Adjacency Lists

I decided to represent both undirected and directed graphs using an **Adjacency List** built with a regular Python dictionary (`dict`), where each key is a node and its value is a list of tuples `(neighbor, weight)`.

I chose this approach because:
1. **It is easy to understand and code:** Working with Python dictionaries and lists is much more intuitive than building and indexing a two-dimensional matrix, especially when nodes are names or letters like `'A'` or `'B'`.
2. **It saves space:** If a graph doesn't have connections between every single pair of nodes, a matrix wastes a lot of space with zeros. With a dictionary, I only store the connections that actually exist.
3. **Easy to adapt for directed and undirected graphs:** With the exact same structure, if the graph is undirected I just add the connection in both directions; if it is directed, I only add it in one direction.

## How It Went

At the beginning, setting up the environment with `uv` and understanding how to translate graph theory into code without external libraries was a bit challenging. The trickiest part was handling cycle detection differently for undirected graphs (making sure not to confuse going back to the parent node with a real cycle) versus directed graphs (keeping track of the current path). Once I understood how BFS and DFS move through the dictionary, implementing `is_tree` and `is_forest` became much clearer since they directly use the connectivity and cycle results.

## How to Run

Run the main script using `uv`:

    uv run main.py