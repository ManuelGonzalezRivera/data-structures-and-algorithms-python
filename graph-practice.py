import heapq

# UnifiedGraph Class Definition
class UnifiedGraph:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]

        for edge in edges:
            if self.weighted:
                node1, node2, w = edge
                self.data[node1].append(node2)
                self.weight[node1].append(w)
                if not self.directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(w)
            else:
                node1, node2 = edge
                self.data[node1].append(node2)
                if not self.directed:
                    self.data[node2].append(node1)

    def __repr__(self):
        result = ""
        for i in range(self.num_nodes):
            if self.weighted:
                neighbors = list(zip(self.data[i], self.weight[i]))
                result += f"{i}: {neighbors}\n"
            else:
                result += f"{i}: {self.data[i]}\n"
        return result

    def bfs(self, root):
        queue = [root]
        discovered = [False] * self.num_nodes
        distance = [None] * self.num_nodes
        parent = [None] * self.num_nodes

        discovered[root] = True
        distance[root] = 0
        idx = 0

        while idx < len(queue):
            current = queue[idx]
            idx += 1
            for node in self.data[current]:
                if not discovered[node]:
                    discovered[node] = True
                    distance[node] = distance[current] + 1
                    parent[node] = current
                    queue.append(node)
        return queue, distance, parent

    def dfs(self, root): # with cycle count
        stack = [root]
        discovered = [False] * self.num_nodes
        parent = [None] * self.num_nodes
        result = []
        cycle_count = 0

        while stack:
            current = stack.pop()
            if not discovered[current]:
                discovered[current] = True
                result.append(current)
                for node in self.data[current]:
                    if not discovered[node]:
                        stack.append(node)
                        parent[node] = current
                    elif parent[current] != node:
                        cycle_count += 1
        return result, parent, cycle_count

    def shortest_path(self, source, target): # with heap
        distances = [float('inf')] * self.num_nodes
        parent = [None] * self.num_nodes
        visited = [False] * self.num_nodes

        distances[source] = 0
        pq = [(0, source)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if visited[current_node]:
                continue
            visited[current_node] = True

            if current_node == target:
                break
            # updating distances
            for i, neighbor in enumerate(self.data[current_node]):
                weight = self.weight[current_node][i] if self.weighted else 1
                if distances[current_node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current_node] + weight
                    parent[neighbor] = current_node
                    heapq.heappush(pq, (distances[neighbor], neighbor))

        return distances[target], parent


# Test Data
num_nodes5 = 9
edges5 = [(0, 1, 3), (0, 3, 2), (0, 8, 4), (1, 7, 4), (2, 7, 2), (2, 3, 6),
          (2, 5, 1), (3, 4, 1), (4, 8, 8), (5, 6, 8)]

num_nodes6 = 5
edges6 = [(0, 1), (1, 2), (2, 3), (2, 4), (4, 2), (3, 0)]

# Integration Tests
print('--- Starting UnifiedGraph Integration Tests ---')

# Test 1: Instantiate UnifiedGraph for weighted, undirected graph (ug5)
ug5 = UnifiedGraph(num_nodes5, edges5, weighted=True, directed=False)
print(f"\nGraph 5 (Weighted, Undirected):\n{ug5}")

# Test 2: Instantiate UnifiedGraph for unweighted, directed graph (ug6)
ug6 = UnifiedGraph(num_nodes6, edges6, weighted=False, directed=True)
print(f"\nGraph 6 (Unweighted, Directed):\n{ug6}")

# Test 3: Shortest Path (Dijkstra) on ug5: Node 0 to 6
dist, parents = ug5.shortest_path(0, 6)
print(f'\nShortest path (0 to 6) in ug5: Distance = {dist}, Parents = {parents}')

# Test 4: DFS on ug6 starting from node 0 (directed graph) with cycle detection
dfs_result, dfs_parents, cycles = ug6.dfs(0)
print(f'\nDFS on ug6 (root 0): Result = {dfs_result}, Cycle Count = {cycles}')

# Test 5: BFS on ug5 starting from node 3
bfs_queue, bfs_dist, bfs_parents = ug5.bfs(3)
print(f'\nBFS on ug5 (root 3): Queue = {bfs_queue}')
print(f'BFS Distances: {bfs_dist}')

print('\n--- UnifiedGraph Integration Tests Complete ---')
