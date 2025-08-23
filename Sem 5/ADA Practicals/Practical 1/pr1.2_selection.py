print("Name: Dave Pujan M.,\nEnrollment No.: 230130107024\n")

import time
import matplotlib.pyplot as plt
import random

# 🔁 Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 📌 Fixed input size
n = 500
best_case = list(range(n))              # Already sorted
worst_case = list(range(n, 0, -1))      # Reversed
average_case = list(range(n))
random.shuffle(average_case)           # Randomized

# ⏱️ Timing Function
def measure_time(data):
    arr = data.copy()
    start = time.time()
    selection_sort(arr)
    end = time.time()
    return end - start

# 🕒 Measure execution time for each case
best_time = measure_time(best_case)
average_time = measure_time(average_case)
worst_time = measure_time(worst_case)

# 📊 Plotting Bar Graph
cases = ['Best Case', 'Average Case', 'Worst Case']
times = [best_time, average_time, worst_time]
colors = ['green', 'orange', 'red']

plt.figure(figsize=(12, 7))
bars = plt.bar(cases, times, color=colors)
plt.title("Selection Sort Time Complexity Analysis (n = 500)", fontsize=14)
plt.ylabel("Time Taken (seconds)", fontsize=12)

# Annotate each bar with time
for bar, t in zip(bars, times):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.0005,
             f"{t:.4f} s", ha='center', fontsize=10)

# 📝 Complexity Annotation on Plot
complexity_details = (
    "Selection Sort Time and Space Complexity:\n"
    "Best Case:    O(n²)\n"
    "Average Case: O(n²)\n"
    "Worst Case:   O(n²)\n"
    "Space Complexity: O(1) – In-place sorting\n"
    "Stable: No"
)

plt.text(2.1, max(times) * 0.6, complexity_details,
         fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.9), verticalalignment='top')

plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
