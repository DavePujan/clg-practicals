print("Name: Dave Pujan M.,\nEnrollment No.: 230130107024\n")

import time
import matplotlib.pyplot as plt

# 🔁 Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # optimization for best case
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# 📌 Fixed Input Size
size = 500
best_case = list(range(size))  # Already sorted (Best)
worst_case = list(range(size, 0, -1))  # Reverse sorted (Worst)
avg_case = list(range(size))
import random
random.shuffle(avg_case)  # Random order (Average)

# 🕒 Measure Time
def time_bubble_sort(arr):
    start = time.time()
    bubble_sort(arr.copy())
    return time.time() - start

best_time = time_bubble_sort(best_case)
avg_time = time_bubble_sort(avg_case)
worst_time = time_bubble_sort(worst_case)

# 📊 Plotting
cases = ['Best Case', 'Average Case', 'Worst Case']
times = [best_time, avg_time, worst_time]

plt.figure(figsize=(12, 7))
bars = plt.bar(cases, times, color=['green', 'orange', 'red'])
plt.title("Bubble Sort Time Complexity Analysis (n = 500)", fontsize=14)
plt.ylabel("Time Taken (seconds)", fontsize=12)

# Annotate bars with time
for bar, time_val in zip(bars, times):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
             f"{time_val:.4f} s", ha='center', fontsize=10)

# 📝 Complexity Details on Chart
complexity_text = (
    "Bubble Sort Time and Space Complexity:\n"
    "Best Case:    O(n)     → Already Sorted\n"
    "Average Case: O(n²)\n"
    "Worst Case:   O(n²)    → Reversed\n"
    "Space Complexity: O(1) – In-place\n"
    "Stable: Yes"
)

plt.text(2.1, max(times)*0.6, complexity_text,
         fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.9), verticalalignment='top')

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()
