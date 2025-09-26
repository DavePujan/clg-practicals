# Implementation of Graph and Searching (DFS and BFS)
import time
import matplotlib.pyplot as plt
import sys
from datetime import datetime
from collections import deque

# Increase recursion limit for DFS
sys.setrecursionlimit(10000)

# ---------------- Graph Implementation ----------------
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Undirected Graph

    # 🔁 DFS (Recursive)
    def dfs_recursive(self, v, visited=None):
        if visited is None:
            visited = [False] * self.V
        visited[v] = True
        for u in self.adj[v]:
            if not visited[u]:
                self.dfs_recursive(u, visited)
        return visited

    # 🔁 BFS (Queue based)
    def bfs(self, s):
        visited = [False] * self.V
        queue = deque([s])
        visited[s] = True
        while queue:
            v = queue.popleft()
            for u in self.adj[v]:
                if not visited[u]:
                    visited[u] = True
                    queue.append(u)
        return visited


# ⏱️ Time measurement function
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start


# ------------------- Program Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 2C")
print("Graph Traversal (DFS & BFS)")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input Graph
n = int(input("\nEnter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = Graph(n)
print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    graph.add_edge(u, v)

start_vertex = int(input("Enter start vertex: "))

# Run DFS & BFS
dfs_res = graph.dfs_recursive(start_vertex)
bfs_res = graph.bfs(start_vertex)

print(f"\nDFS visited from {start_vertex}: {dfs_res}")
print(f"BFS visited from {start_vertex}: {bfs_res}")

# ------------------- Chart Comparison -------------------
# Compare execution times for growing graph sizes
sizes = [10, 50, 100, 200]
times_dfs = []
times_bfs = []

for size in sizes:
    g = Graph(size)
    # Make a chain-like graph
    for i in range(size - 1):
        g.add_edge(i, i + 1)

    times_dfs.append(measure_time(g.dfs_recursive, 0))
    times_bfs.append(measure_time(g.bfs, 0))

plt.figure(figsize=(12, 6))
plt.plot(sizes, times_dfs, marker='o', label='DFS (Recursive)', color='red')
plt.plot(sizes, times_bfs, marker='s', label='BFS (Queue)', color='green')

# Annotate points
for x, y in zip(sizes, times_dfs):
    plt.text(x, y + 0.0001, f"{y:.6f}s", ha='center', fontsize=8, color='red')
for x, y in zip(sizes, times_bfs):
    plt.text(x, y + 0.0001, f"{y:.6f}s", ha='center', fontsize=8, color='green')

# 📘 Complexity details
info_text = (
    "Enrollment No: 230130107078\n"
    "Graph Traversal Time & Space Complexity:\n\n"
    "DFS (Recursive):\n"
    "  Time: O(V + E)\n"
    "  Space: O(V) due to recursion stack\n\n"
    "BFS (Queue):\n"
    "  Time: O(V + E)\n"
    "  Space: O(V) due to queue\n"
)

# 🧾 Add text box
plt.text(max(sizes)*0.55, max(times_dfs)*0.6, info_text,
         fontsize=9, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title("Graph Traversal: DFS vs BFS Execution Time", fontsize=14)
plt.xlabel("Number of Vertices")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
