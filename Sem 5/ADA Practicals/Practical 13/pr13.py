import time
import matplotlib.pyplot as plt
import sys
from datetime import datetime

sys.setrecursionlimit(10000)

# 🔁 Palindrome check (Recursive)
def palindrome_recursive(s, start, end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return palindrome_recursive(s, start + 1, end - 1)

# 🔁 Palindrome check (Iterative)
def palindrome_iterative(s):
    return s == s[::-1]

# 🔁 Simple BRTS simulation (seat reservation)
def brts_simulation(seats, operations):
    seat_list = [0]*seats
    for op, idx in operations:
        if op == 'book':
            seat_list[idx] = 1
        elif op == 'cancel':
            seat_list[idx] = 0
    return seat_list

# 🔁 Simple HR simulation (add/delete employee)
def hr_simulation(employees, operations):
    emp_dict = {}
    for emp in employees:
        emp_dict[emp] = "Active"
    for op, emp in operations:
        if op == 'remove' and emp in emp_dict:
            emp_dict.pop(emp)
    return emp_dict

# ⏱️ Time measurement function
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# ------------------- Program Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 6A")
print("Open-Ended Problems: Palindromes, BRTS, HR Design")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input
s = input("\nEnter a string to check palindrome: ")
seats = int(input("Enter number of seats in BRTS: "))
employees = input("Enter employee names (space separated): ").split()

# Sample operations
brts_ops = [('book', 0), ('book', seats-1), ('cancel', 0)]
hr_ops = [('remove', employees[0])] if employees else []

# Results
pal_rec = palindrome_recursive(s, 0, len(s)-1)
pal_iter = palindrome_iterative(s)
brts_res = brts_simulation(seats, brts_ops)
hr_res = hr_simulation(employees, hr_ops)

print(f"\nPalindrome (Recursive): {pal_rec}")
print(f"Palindrome (Iterative): {pal_iter}")
print(f"BRTS seat status after operations: {brts_res}")
print(f"HR employee status after operations: {hr_res}")

# ------------------- Chart Comparison -------------------
lengths = [5, 10, 20, 50]
times_rec = []
times_iter = []

for l in lengths:
    test_str = s[:l] if l <= len(s) else s + 'A'*(l-len(s))
    times_rec.append(measure_time(palindrome_recursive, test_str, 0, len(test_str)-1))
    times_iter.append(measure_time(palindrome_iterative, test_str))

plt.figure(figsize=(12, 6))
plt.plot(lengths, times_rec, marker='o', label='Recursive Palindrome', color='red')
plt.plot(lengths, times_iter, marker='s', label='Iterative Palindrome', color='green')

# Annotate points
for x, y in zip(lengths, times_rec):
    plt.text(x, y + 0.00001, f"{y:.6f}s", ha='center', fontsize=8, color='red')
for x, y in zip(lengths, times_iter):
    plt.text(x, y + 0.00001, f"{y:.6f}s", ha='center', fontsize=8, color='green')

# 📘 Complexity details
info_text = (
    "Enrollment No: 230130107024\n"
    "Open-Ended Problems Time & Space Complexity:\n\n"
    "Palindrome Recursive:\n"
    "  Time: O(n)\n"
    "  Space: O(n) due to recursion\n\n"
    "Palindrome Iterative:\n"
    "  Time: O(n)\n"
    "  Space: O(1)\n\n"
    "BRTS & HR Simulation:\n"
    "  Time: O(n) for operations\n"
    "  Space: O(n) for seats/employees\n"
)

plt.text(max(lengths)*0.55, max(times_rec)*0.6, info_text,
         fontsize=9, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title("Open-Ended Problems: Recursive vs Iterative Execution Time", fontsize=14)
plt.xlabel("Length of Input / Number of Elements")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
