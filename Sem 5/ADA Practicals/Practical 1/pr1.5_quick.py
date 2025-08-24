import time
import matplotlib.pyplot as plt
from datetime import datetime

# ⚡ Quick Sort Implementation
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


# ------------------- Console Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 2D")
print("Implementation and Time Analysis of Quick Sort")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.\n")

# Input
n = int(input("Enter number of elements: "))
arr = []

print("Enter array elements:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

# Execution
start_time = time.time()
sorted_arr = quick_sort(arr.copy(), 0, n - 1)
end_time = time.time()
exec_time = end_time - start_time

print(f"\nSorted Array: {sorted_arr}")
print(f"Execution Time: {exec_time:.6f} seconds")

# ------------------- Chart -------------------
plt.figure(figsize=(12, 6))
bars = plt.bar(["Quick Sort"], [exec_time], color='teal')
plt.ylabel("Execution Time (seconds)")
plt.title("Time Analysis of Quick Sort")

# Annotate bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.00001, f"{height:.6f}s",
             ha='center', fontsize=10)

# Complexity details
info = (
    "Time Complexity:\n"
    "  Best Case   : O(n log n)\n"
    "  Average Case: O(n log n)\n"
    "  Worst Case  : O(n^2) (when array is already sorted and pivot is chosen poorly)\n\n"
    "Space Complexity:\n"
    "  O(log n) — due to recursive stack calls\n\n"
    f"Execution Time for n = {n}: {exec_time:.6f} seconds"
)

plt.text(0.6, exec_time * 0.5, info,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
