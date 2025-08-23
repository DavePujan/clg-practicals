import time
import matplotlib.pyplot as plt
from datetime import datetime

# 👜 Greedy Fractional Knapsack Implementation
def fractional_knapsack(values, weights, capacity):
    n = len(values)
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    ratio.sort(reverse=True)  # Sort by value/weight ratio

    total_value = 0.0
    for r, v, w in ratio:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += r * capacity
            break
    return total_value

# ⏱️ Time measurement function
def measure_time(func, values, weights, capacity):
    start = time.time()
    result = func(values, weights, capacity)
    end = time.time()
    return result, end - start

# ------------------- Program Output (like screenshot) -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 1F")
print("Knapsack Problem using Greedy Algorithm")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# 📥 Input Example
n = int(input("\nEnter number of items: "))
values = []
weights = []
for i in range(n):
    v = int(input(f"Enter value of item {i+1}: "))
    w = int(input(f"Enter weight of item {i+1}: "))
    values.append(v)
    weights.append(w)

capacity = int(input("Enter Knapsack Capacity: "))

# ⚡ Run Greedy Knapsack
max_value, exec_time = measure_time(fractional_knapsack, values, weights, capacity)

# 🖨️ Output Result
print(f"\nMaximum value obtained: {max_value}")
print(f"Execution Time: {exec_time:.6f} seconds")

# ------------------- Chart -------------------
methods = ['Greedy Knapsack']
times = [exec_time]

plt.figure(figsize=(12, 6))
bars = plt.bar(methods, times, color=['teal'])

# 📝 Annotate bars with time values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.00001,
             f"{height:.6f} s", ha='center', fontsize=10)

# 📘 Complexity details
info_text = (
    "Greedy Knapsack Time & Space Complexity:\n\n"
    "Sorting step:\n"
    "  Time: O(n log n)\n"
    "  Space: O(n)\n\n"
    "Greedy selection:\n"
    "  Time: O(n)\n"
    "  Space: O(1)\n\n"
    "Overall:\n"
    "  Time: O(n log n)\n"
    "  Space: O(n)\n\n"
    "Best / Worst / Avg Case: Same (due to sorting step)\n"
)

# 🧾 Add text box to plot
plt.text(0.6, exec_time * 0.5, info_text,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title(f"Greedy Knapsack Computation Time (Items = {n}, Capacity = {capacity})", fontsize=14)
plt.ylabel("Time (seconds)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
