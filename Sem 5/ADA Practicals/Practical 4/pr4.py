import time
import matplotlib.pyplot as plt
import sys
from datetime import datetime

# Increase recursion limit for larger input
sys.setrecursionlimit(10000)

# 🔁 Iterative factorial
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 🔁 Recursive factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# ⏱️ Time measurement function
def measure_time(func, n):
    start = time.time()
    func(n)
    end = time.time()
    return end - start

# ------------------- Program Output (like screenshot) -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 1E")
print("Factorial Program (Iterative & Recursive)")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input from user
n = int(input("Enter a number: "))

# Factorial results
iter_res = factorial_iterative(n)
rec_res = factorial_recursive(n)

print(f"\nFactorial of {n} (Iterative): {iter_res}")
print(f"Factorial of {n} (Recursive): {rec_res}")

# ------------------- Chart Comparison -------------------
# 📏 Measure time
time_iterative = measure_time(factorial_iterative, n)
time_recursive = measure_time(factorial_recursive, n)

# 📊 Plotting comparison
methods = ['Iterative', 'Recursive']
times = [time_iterative, time_recursive]

plt.figure(figsize=(12, 6))
bars = plt.bar(methods, times, color=['green', 'blue'])

# 📝 Annotate bars with time values
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.0001,
             f"{height:.6f} s", ha='center', fontsize=10)

# 📘 Complexity details
info_text = (
    "Factorial Time & Space Complexity:\n\n"
    "Iterative Method:\n"
    "  Time: O(n)\n"
    "  Space: O(1)\n\n"
    "Recursive Method:\n"
    "  Time: O(n)\n"
    "  Space: O(n) (due to recursion stack)\n\n"
    "Best / Worst / Avg Case: Same (as input size n defines time)\n"
)

# 🧾 Add text box to plot
plt.text(1.5, max(times) * 0.4, info_text,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title(f"Factorial Computation Time (n = {n}) - Iterative vs Recursive", fontsize=14)
plt.ylabel("Time (seconds)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
