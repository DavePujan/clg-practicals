import time
import matplotlib.pyplot as plt
from datetime import datetime

# 🔍 Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# 🔍 Binary Search (iterative)
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# ------------------- Console Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 1I")
print("Implementation and Time Analysis of Linear & Binary Search")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.\n")

# Input
n = int(input("Enter number of elements in array: "))
arr = []
print("Enter sorted array elements:")
for i in range(n):
    arr.append(int(input(f"Element {i+1}: ")))

x = int(input("\nEnter element to search: "))

print(f"\nArray: {arr}")
print(f"Element to Search: {x}\n")

# Execution - Linear Search
start_time = time.time()
linear_result = linear_search(arr, x)
end_time = time.time()
linear_time = end_time - start_time

# Execution - Binary Search
start_time = time.time()
binary_result = binary_search(arr, x)
end_time = time.time()
binary_time = end_time - start_time

# Output Results
if linear_result != -1:
    print(f"Linear Search: Element found at index {linear_result}")
else:
    print("Linear Search: Element not found")

if binary_result != -1:
    print(f"Binary Search: Element found at index {binary_result}")
else:
    print("Binary Search: Element not found")

# ------------------- Chart -------------------
plt.figure(figsize=(12, 6))
methods = ["Linear Search", "Binary Search"]
times = [linear_time, binary_time]
bars = plt.bar(methods, times, color=['orange', 'green'])
plt.ylabel("Execution Time (seconds)")
plt.title("Time Analysis: Linear vs Binary Search")

# Annotate bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.00001, f"{height:.6f}s",
             ha='center', fontsize=10)

# Complexity details
info = (
    "Time Complexity:\n"
    "  Linear Search:\n"
    "    Best Case: O(1)\n"
    "    Worst Case: O(n)\n"
    "    Average Case: O(n)\n\n"
    "  Binary Search:\n"
    "    Best Case: O(1)\n"
    "    Worst Case: O(log n)\n"
    "    Average Case: O(log n)\n\n"
    "Space Complexity:\n"
    "  Linear Search: O(1)\n"
    "  Binary Search: O(1) (iterative)\n\n"
    f"Array Size: {n}, Search Element: {x}"
)

plt.text(1.2, max(times) * 0.5, info,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
