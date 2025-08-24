import time
import matplotlib.pyplot as plt
from datetime import datetime
import random

# 🫧 Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# ------------------- Console Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 2A")
print("Implementation and Time Analysis of Bubble Sort")
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
sorted_arr = bubble_sort(arr.copy())
end_time = time.time()
exec_time = end_time - start_time

print(f"\nSorted Array: {sorted_arr}")
print(f"Execution Time: {exec_time:.6f} seconds")

# ------------------- Chart -------------------
plt.figure(figsize=(12, 6))
bars = plt.bar(["Bubble Sort"], [exec_time], color='teal')
plt.ylabel("Execution Time (seconds)")
plt.title("Time Analysis of Bubble Sort")

# Annotate bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.00001, f"{height:.6f}s",
             ha='center', fontsize=10)

# Complexity details
info = (
    "Time Complexity:\n"
    "  Best Case   : O(n)   (already sorted array)\n"
    "  Average Case: O(n^2)\n"
    "  Worst Case  : O(n^2)\n\n"
    "Space Complexity:\n"
    "  O(1) — In-place sorting\n\n"
    f"Execution Time for n = {n}: {exec_time:.6f} seconds"
)

plt.text(0.6, exec_time * 0.5, info,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
