print("Name: Dave Pujan M.,\nEnrollment No.: 230130107024\n")

import time
import matplotlib.pyplot as plt
import random
import sys

# Increase recursion limit for large arrays
sys.setrecursionlimit(2000)  # Increased for n=1000

# 🔁 Quick Sort implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# ⏱️ Time measurement function
def measure_time(arr):
    copied = arr.copy()
    start = time.time()
    quick_sort(copied)
    end = time.time()
    return end - start

# 📥 Input size
n = 1000

# 📊 Prepare input cases
best_case = list(range(n))                      # Already sorted (best with good pivot)
worst_case = list(range(n, 0, -1))              # Reverse sorted (worst if pivot is last)
average_case = best_case.copy()
random.shuffle(average_case)                   # Randomized input

# ⏱️ Measure execution time
best_time = measure_time(best_case)
avg_time = measure_time(average_case)
worst_time = measure_time(worst_case)

# 📈 Plotting the results
cases = ['Best Case', 'Average Case', 'Worst Case']
times = [best_time, avg_time, worst_time]
colors = ['green', 'orange', 'red']

plt.figure(figsize=(12, 6))
bars = plt.bar(cases, times, color=colors)

# 📝 Annotate bars
for bar, t in zip(bars, times):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
             f"{t:.4f} s", ha='center', fontsize=10)

# ℹ️ Quick Sort Complexity Info
info = (
    "Quick Sort Complexity:\n"
    "Time Complexity:\n"
    "  Best Case: O(n log n)\n"
    "  Average Case: O(n log n)\n"
    "  Worst Case: O(n^2) (when pivot is worst)\n"
    "Space Complexity: O(log n) (recursive stack)\n"
    "Stable: No"
)

plt.title("Quick Sort: Time Analysis (n = 10,000)", fontsize=14)
plt.ylabel("Time (seconds)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# 💬 Add complexity text box
plt.text(2.2, max(times)*0.5, info,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.show()
