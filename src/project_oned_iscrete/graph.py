class Graph:
    def __init__(self, is_directed: bool = False):
        self.is_directed = is_directed
        self.adj_list = {}

    def add_edge(self, source: str, target: str, weight: float) -> None:
        if source not in self.adj_list:
            self.adj_list[source] = []
        if target not in self.adj_list:
            self.adj_list[target] = []

        self.adj_list[source].append((target, weight))

        if not self.is_directed:
            self.adj_list[target].append((source, weight))

    def get_vertices(self) -> list:
        return list(self.adj_list.keys())

    @classmethod
    def load_from_file(cls, file_path: str, is_directed: bool = False) -> 'Graph':
        graph = cls(is_directed=is_directed)
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                if len(parts) == 3:
                    source = parts[0].strip()
                    target = parts[1].strip()
                    weight = float(parts[2].strip())
                    graph.add_edge(source, target, weight)
        return graph

    def is_connected(self, _silent: bool = False) -> bool:
        vertices = self.get_vertices()
        if not vertices:
            result = True
        else:
            visited = set()
            start_node = vertices[0]
            queue = [start_node]
            visited.add(start_node)

            while queue:
                curr = queue.pop(0)
                neighbors = [nbr for nbr, _ in self.adj_list[curr]]
                
                # Si es dirigido, incluimos vecinos entrantes para evaluar conexidad débil
                if self.is_directed:
                    for node, edges in self.adj_list.items():
                        if any(nbr == curr for nbr, _ in edges):
                            neighbors.append(node)

                for nbr in neighbors:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)

            result = len(visited) == len(vertices)

        if not _silent:
            print(f"is_connected: {result}")
        return result

    def has_cycles(self, _silent: bool = False) -> bool:
        vertices = self.get_vertices()
        visited = set()
        result = False

        if not self.is_directed:
            def dfs_undirected(node, parent):
                visited.add(node)
                for neighbor, _ in self.adj_list[node]:
                    if neighbor not in visited:
                        if dfs_undirected(neighbor, node):
                            return True
                    elif neighbor != parent:
                        return True
                return False

            for vertex in vertices:
                if vertex not in visited:
                    if dfs_undirected(vertex, None):
                        result = True
                        break
        else:
            rec_stack = set()

            def dfs_directed(node):
                visited.add(node)
                rec_stack.add(node)

                for neighbor, _ in self.adj_list[node]:
                    if neighbor not in visited:
                        if dfs_directed(neighbor):
                            return True
                    elif neighbor in rec_stack:
                        return True

                rec_stack.remove(node)
                return False

            for vertex in vertices:
                if vertex not in visited:
                    if dfs_directed(vertex):
                        result = True
                        break

        if not _silent:
            print(f"has_cycles: {result}")
        return result

    def is_tree(self) -> bool:
        connected = self.is_connected(_silent=True)
        cycles = self.has_cycles(_silent=True)
        result = connected and not cycles
        print(f"is_tree: {result}")
        return result

    def is_forest(self) -> bool:
        cycles = self.has_cycles(_silent=True)
        result = not cycles
        print(f"is_forest: {result}")
        return result