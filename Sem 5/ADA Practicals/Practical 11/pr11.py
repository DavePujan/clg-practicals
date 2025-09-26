import time
import matplotlib.pyplot as plt
import sys
from datetime import datetime
import random

sys.setrecursionlimit(10000)

# 🔁 Disjoint Set (Union-Find) for Kruskal
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# 🔁 Kruskal’s Algorithm
def kruskal(V, edges):
    ds = DisjointSet(V)
    mst_weight = 0
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_weight += w
    return mst_weight

# ⏱️ Time measurement function
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# ------------------- Program Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 4B")
print("Implementation of Kruskal’s Algorithm")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input
V = int(input("\nEnter number of vertices: "))
E = int(input("Enter number of edges: "))

edges = []
print("Enter edges (u v w):")
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Results
mst_weight = kruskal(V, edges)
print(f"\nMST Total Weight using Kruskal’s Algorithm: {mst_weight}")

# ------------------- Chart Comparison -------------------
sizes = [10, 20, 30, 40]
times_kruskal = []

for size in sizes:
    edges = []
    for _ in range(size * 3):  # random edges
        u, v = random.sample(range(size), 2)
        w = random.randint(1, 100)
        edges.append((u, v, w))
    times_kruskal.append(measure_time(kruskal, size, edges))

plt.figure(figsize=(12, 6))
plt.plot(sizes, times_kruskal, marker='o', label="Kruskal's Algorithm", color='blue')

for x, y in zip(sizes, times_kruskal):
    plt.text(x, y + 0.0001, f"{y:.6f}s", ha='center', fontsize=8, color='blue')

info_text = (
    "Enrollment No: 230130107078\n"
    "Kruskal’s Algorithm Time & Space Complexity:\n\n"
    "Time: O(E log E)  (Sorting edges dominates)\n"
    "Space: O(V + E)   (Disjoint set + edge list)\n"
)

plt.text(max(sizes)*0.55, max(times_kruskal)*0.6, info_text,
         fontsize=9, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title("Kruskal’s Algorithm Execution Time", fontsize=14)
plt.xlabel("Number of Vertices")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
