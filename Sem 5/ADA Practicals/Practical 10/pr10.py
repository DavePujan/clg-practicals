# Implementation of Prim's Algorithm
import time
import matplotlib.pyplot as plt
import sys
from datetime import datetime
import random

sys.setrecursionlimit(10000)

# 🔁 Prim’s Algorithm (Adjacency Matrix - Simple O(V^2))
def prims_simple(graph, V):
    key = [float('inf')] * V
    mstSet = [False] * V
    key[0] = 0
    total_weight = 0
    for _ in range(V):
        u = min((k, idx) for idx, k in enumerate(key) if not mstSet[idx])[1]
        mstSet[u] = True
        total_weight += key[u]
        for v in range(V):
            if graph[u][v] and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
    return total_weight

# 🔁 Prim’s Algorithm (Using Priority Queue - Efficient O(E log V))
import heapq
def prims_heap(graph, V):
    visited = [False] * V
    min_heap = [(0, 0)]
    total_weight = 0
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
    return total_weight

# ⏱️ Time measurement function
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# ------------------- Program Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 4A")
print("Implementation of Prim’s Algorithm")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input
V = int(input("\nEnter number of vertices: "))
E = int(input("Enter number of edges: "))

# Adjacency Matrix (for simple version)
graph_matrix = [[0] * V for _ in range(V)]
# Adjacency List (for heap version)
graph_list = [[] for _ in range(V)]

print("Enter edges (u v w):")
for _ in range(E):
    u, v, w = map(int, input().split())
    graph_matrix[u][v] = w
    graph_matrix[v][u] = w
    graph_list[u].append((v, w))
    graph_list[v].append((u, w))

# Results
simple_res = prims_simple(graph_matrix, V)
heap_res = prims_heap(graph_list, V)

print(f"\nMST Total Weight using Simple Prim’s: {simple_res}")
print(f"MST Total Weight using Heap-based Prim’s: {heap_res}")

# ------------------- Chart Comparison -------------------
sizes = [10, 20, 30, 40]
times_simple = []
times_heap = []

for size in sizes:
    g_matrix = [[0] * size for _ in range(size)]
    g_list = [[] for _ in range(size)]
    for _ in range(size * 3):  # random edges
        u, v = random.sample(range(size), 2)
        w = random.randint(1, 100)
        g_matrix[u][v] = g_matrix[v][u] = w
        g_list[u].append((v, w))
        g_list[v].append((u, w))

    times_simple.append(measure_time(prims_simple, g_matrix, size))
    times_heap.append(measure_time(prims_heap, g_list, size))

plt.figure(figsize=(12, 6))
plt.plot(sizes, times_simple, marker='o', label='Prim’s O(V^2)', color='red')
plt.plot(sizes, times_heap, marker='s', label='Prim’s O(E log V)', color='green')

for x, y in zip(sizes, times_simple):
    plt.text(x, y + 0.0001, f"{y:.6f}s", ha='center', fontsize=8, color='red')
for x, y in zip(sizes, times_heap):
    plt.text(x, y + 0.0001, f"{y:.6f}s", ha='center', fontsize=8, color='green')

info_text = (
    "Enrollment No: 230130107078\n"
    "Prim’s Algorithm Time & Space Complexity:\n\n"
    "Simple (Adj Matrix):\n"
    "  Time: O(V^2)\n"
    "  Space: O(V^2)\n\n"
    "Heap (Adj List):\n"
    "  Time: O(E log V)\n"
    "  Space: O(V + E)\n"
)

plt.text(max(sizes)*0.55, max(times_simple)*0.6, info_text,
         fontsize=9, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title("Prim’s Algorithm: Simple vs Heap Execution Time", fontsize=14)
plt.xlabel("Number of Vertices")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
