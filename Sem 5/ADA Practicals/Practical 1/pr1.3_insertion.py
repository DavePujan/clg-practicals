print("Name: Dave Pujan M.,\nEnrollment No.: 230130107024\n")

import time
import random
import matplotlib.pyplot as plt

# 🔁 Insertion Sort Algorithm
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 📌 Sample input/output
sample_input = [12, 11, 13, 5, 6]
print("Original Array:", sample_input)
insertion_sort(sample_input)
print("Sorted Array using Insertion Sort:", sample_input)

# 📊 Time Analysis for Various Input Sizes
input_sizes = [100, 200, 300, 400, 500]
execution_times = []

for size in input_sizes:
    data = [random.randint(1, 1000) for _ in range(size)]
    start = time.time()
    insertion_sort(data.copy())
    end = time.time()
    elapsed = end - start
    execution_times.append(elapsed)
    print(f"Sorted {size} elements in {elapsed:.6f} seconds")

# 📈 Plotting Time vs Input Size with Complexity Info
plt.figure(figsize=(12, 7))
plt.plot(input_sizes, execution_times, marker='o', linestyle='-', color='teal', label="Execution Time")
plt.title("Insertion Sort Time Complexity Analysis", fontsize=14)
plt.xlabel("Input Size (n)", fontsize=12)
plt.ylabel("Time Taken (seconds)", fontsize=12)
plt.grid(True)

# 📝 Complexity Annotations on Graph
complexity_text = (
    "Insertion Sort Time and Space Complexity:\n"
    "Best Case:    O(n)     → Nearly Sorted Input\n"
    "Average Case: O(n²)\n"
    "Worst Case:   O(n²)    → Reversed Input\n"
    "Space Complexity: O(1) – In-place sorting\n"
    "Stable: Yes"
)

plt.text(520, max(execution_times)*0.6, complexity_text,
         fontsize=10, bbox=dict(facecolor='lightyellow', alpha=0.9), verticalalignment='top')

plt.legend()
plt.tight_layout()
plt.show()
