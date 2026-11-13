from src.project_oned_iscrete.graph import Graph

def main():
    file_path = "data/example_graph.txt"

    print("--- Undirected Graph ---")
    undirected = Graph.load_from_file(file_path, is_directed=False)
    undirected.is_connected()
    undirected.has_cycles()
    undirected.is_tree()
    undirected.is_forest()

    print("\n--- Directed Graph ---")
    directed = Graph.load_from_file(file_path, is_directed=True)
    directed.is_connected()
    directed.has_cycles()
    directed.is_tree()
    directed.is_forest()

if __name__ == "__main__":
    main()