print("Name: Dave Pujan M.,\nEnrollment No.: 230130107024\n")

import time
import matplotlib.pyplot as plt
import random

# 🔁 Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        # Merge two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# 📌 Input size
n = 10000  # You can change this to test with larger arrays

# 📥 Prepare input cases
best_case = list(range(n))                   # Sorted array
worst_case = list(range(n, 0, -1))           # Reverse sorted
average_case = best_case.copy()
random.shuffle(average_case)                # Randomized input

# ⏱️ Time measurement function
def measure_time(case):
    arr = case.copy()
    start = time.time()
    merge_sort(arr)
    return time.time() - start

# 🕒 Measure time for each case
best_time = measure_time(best_case)
average_time = measure_time(average_case)
worst_time = measure_time(worst_case)

# 📊 Plotting chart
plt.figure(figsize=(12, 6))
cases = ['Best Case', 'Average Case', 'Worst Case']
times = [best_time, average_time, worst_time]
colors = ['green', 'orange', 'red']
bars = plt.bar(cases, times, color=colors)

# 📝 Annotate bars with exact time
for bar, t in zip(bars, times):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
             f"{t:.4f} s", ha='center', fontsize=10)

# 📌 Merge Sort Complexity Info
complexity_text = (
    "Merge Sort Complexity:\n"
    "Time Complexity:\n"
    "  Best Case: O(n log n)\n"
    "  Average Case: O(n log n)\n"
    "  Worst Case: O(n log n)\n"
    "Space Complexity: O(n)\n"
    "Stable: Yes"
)

plt.title("Merge Sort: Time Analysis (n = 10,000)", fontsize=14)
plt.ylabel("Time (seconds)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# ℹ️ Show complexity as box on the plot
plt.text(2.2, max(times) * 0.6, complexity_text,
         fontsize=10, bbox=dict(facecolor='lightblue', alpha=0.7))

plt.tight_layout()
plt.show()
