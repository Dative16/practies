from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)
        if not directed:
            self.graph[v].append(u)
    
    def bfs(self, start):
        """Breadth First Search"""
        visited = set()
        result = []
        queue = deque([start])
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                queue.extend([neighbor for neighbor in self.graph[vertex] 
                            if neighbor not in visited])
        
        return result
    
    def dfs(self, start):
        """Depth First Search (Iterative)"""
        visited = set()
        result = []
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                # Add neighbors in reverse for natural DFS order
                for neighbor in reversed(self.graph[vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start):
        """Depth First Search (Recursive)"""
        visited = set()
        result = []
        
        def dfs_util(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return result

# Example
print("\nGraph Algorithms:")
g = Graph()
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
for u, v in edges:
    g.add_edge(u, v, directed=True)

print("BFS starting from 2:", g.bfs(2))
print("DFS (Iterative) starting from 2:", g.dfs(2))
print("DFS (Recursive) starting from 2:", g.dfs_recursive(2))