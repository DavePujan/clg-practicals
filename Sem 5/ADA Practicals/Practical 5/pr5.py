import time
import matplotlib.pyplot as plt
from datetime import datetime

# ------------------- Knapsack using Dynamic Programming -------------------
def knapsack_dp(weights, values, W, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w - weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

# ⏱️ Time measurement function
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# ------------------- Program Output (like screenshot) -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 1E")
print("Knapsack Problem (Dynamic Programming)")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input
n = int(input("\nEnter number of items: "))
values = []
weights = []

print("Enter values of items:")
for i in range(n):
    values.append(int(input(f"Value of item {i+1}: ")))

print("Enter weights of items:")
for i in range(n):
    weights.append(int(input(f"Weight of item {i+1}: ")))

W = int(input("Enter maximum capacity of knapsack: "))

# Run DP Knapsack
max_profit = knapsack_dp(weights, values, W, n)

print(f"\nMaximum Profit = {max_profit}")

# ------------------- Chart Comparison -------------------
# For plotting, compare execution time with different input sizes
item_counts = [5, 10, 15, 20, 25]
times = []

for count in item_counts:
    vals = [i*10 for i in range(1, count+1)]
    wts = [i for i in range(1, count+1)]
    cap = count * 5
    t = measure_time(knapsack_dp, wts, vals, cap, count)
    times.append(t)

# 📊 Plotting comparison
plt.figure(figsize=(12, 6))
plt.plot(item_counts, times, marker='o')

# 📝 Annotate points with time values
for i, t in zip(item_counts, times):
    plt.text(i, t + 0.0001, f"{t:.6f}s", ha='center', fontsize=9)

# 📘 Complexity details
info_text = (
    "Knapsack (DP) Time & Space Complexity:\n\n"
    "Time: O(n × W)\n"
    "Space: O(n × W) [can be optimized to O(W)]\n\n"
    "Recurrence:\n"
    "K(i, w) = max( values[i-1] + K(i-1, w - weights[i-1]), K(i-1, w) ) if weights[i-1] ≤ w\n"
    "       = K(i-1, w) otherwise\n"
)

# 🧾 Add text box to plot
plt.text(max(item_counts)*0.6, max(times)*0.6, info_text,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title("Knapsack Problem Execution Time (Dynamic Programming)", fontsize=14)
plt.xlabel("Number of Items")
plt.ylabel("Time (seconds)")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
