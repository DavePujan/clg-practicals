import time
import matplotlib.pyplot as plt
import sys
from datetime import datetime

sys.setrecursionlimit(10000)

# 🔁 Recursive LCS (Exponential)
def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    else:
        return max(lcs_recursive(X, Y, m-1, n), lcs_recursive(X, Y, m, n-1))

# 🔁 DP LCS (Efficient)
def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# ⏱️ Time measurement function
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# ------------------- Program Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 5A")
print("Longest Common Subsequence (LCS) Problem")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input
X = input("\nEnter first string: ")
Y = input("Enter second string: ")

m, n = len(X), len(Y)

# Results
rec_res = lcs_recursive(X, Y, m, n)
dp_res = lcs_dp(X, Y)

print(f"\nLength of LCS using Recursive: {rec_res}")
print(f"Length of LCS using DP: {dp_res}")

# ------------------- Chart Comparison -------------------
lengths = [(5,5), (10,10), (12,12), (15,15)]
times_recursive = []
times_dp = []

for lX, lY in lengths:
    sample_X = X[:lX] if lX <= m else X + 'A'*(lX-m)
    sample_Y = Y[:lY] if lY <= n else Y + 'B'*(lY-n)
    times_recursive.append(measure_time(lcs_recursive, sample_X, sample_Y, len(sample_X), len(sample_Y)))
    times_dp.append(measure_time(lcs_dp, sample_X, sample_Y))

plt.figure(figsize=(12, 6))
plt.plot([l[0] for l in lengths], times_recursive, marker='o', label='Recursive (Exponential)', color='red')
plt.plot([l[0] for l in lengths], times_dp, marker='s', label='Dynamic Programming (Efficient)', color='green')

# Annotate points
for x, y in zip([l[0] for l in lengths], times_recursive):
    plt.text(x, y + 0.0001, f"{y:.6f}s", ha='center', fontsize=8, color='red')
for x, y in zip([l[0] for l in lengths], times_dp):
    plt.text(x, y + 0.0001, f"{y:.6f}s", ha='center', fontsize=8, color='green')

# 📘 Complexity details
info_text = (
    "Enrollment No: 230130107078\n"
    "LCS Problem Time & Space Complexity:\n\n"
    "Recursive Method:\n"
    "  Time: Exponential (O(2^(m+n)))\n"
    "  Space: O(m+n) due to recursion depth\n\n"
    "Dynamic Programming Method:\n"
    "  Time: O(m × n)\n"
    "  Space: O(m × n)\n"
)

plt.text(max([l[0] for l in lengths])*0.55, max(times_recursive)*0.6, info_text,
         fontsize=9, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title("LCS Problem: Recursive vs DP Execution Time", fontsize=14)
plt.xlabel("Length of String")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
