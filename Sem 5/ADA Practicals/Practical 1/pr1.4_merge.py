import time
import matplotlib.pyplot as plt
from datetime import datetime

# ⚡ Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursive sort
        merge_sort(L)
        merge_sort(R)

        # Merging process
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# ------------------- Console Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 2C")
print("Implementation and Time Analysis of Merge Sort")
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
sorted_arr = merge_sort(arr.copy())
end_time = time.time()
exec_time = end_time - start_time

print(f"\nSorted Array: {sorted_arr}")
print(f"Execution Time: {exec_time:.6f} seconds")

# ------------------- Chart -------------------
plt.figure(figsize=(12, 6))
bars = plt.bar(["Merge Sort"], [exec_time], color='teal')
plt.ylabel("Execution Time (seconds)")
plt.title("Time Analysis of Merge Sort")

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
    "  Worst Case  : O(n log n)\n\n"
    "Space Complexity:\n"
    "  O(n) — extra arrays used during merge\n\n"
    f"Execution Time for n = {n}: {exec_time:.6f} seconds"
)

plt.text(0.6, exec_time * 0.5, info,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
