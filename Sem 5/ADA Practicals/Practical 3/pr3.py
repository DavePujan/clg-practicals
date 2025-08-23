import time
import matplotlib.pyplot as plt
from datetime import datetime

# 🔺 Heapify function to maintain max-heap property
def heapify(arr, n, i):
    largest = i       # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2 # right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)

# 🔺 Heap Sort function
def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)
    return arr

# ------------------- Console Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 1H")
print("Max-Heap Sort Algorithm")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.\n")

# Input
n = int(input("Enter number of elements: "))
arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

print(f"\nOriginal Array: {arr}")

# Execution
start_time = time.time()
sorted_arr = heap_sort(arr.copy())
end_time = time.time()
exec_time = end_time - start_time

print(f"Sorted Array (Heap Sort): {sorted_arr}")

# ------------------- Chart -------------------
plt.figure(figsize=(12, 6))
bars = plt.bar(["Heap Sort"], [exec_time], color='purple')
plt.ylabel("Execution Time (seconds)")
plt.title("Max-Heap Sort Algorithm")

# Annotate bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.00001, f"{height:.6f}s",
             ha='center', fontsize=10)

# Complexity details
info = (
    "Time Complexity:\n"
    "  Best Case: O(n log n)\n"
    "  Average Case: O(n log n)\n"
    "  Worst Case: O(n log n)\n\n"
    "Space Complexity:\n"
    "  O(1) — In-place sorting\n\n"
    f"Input Size: {n}\n"
    f"Sorted Output: {sorted_arr}"
)

plt.text(0.6, exec_time * 0.5, info,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
