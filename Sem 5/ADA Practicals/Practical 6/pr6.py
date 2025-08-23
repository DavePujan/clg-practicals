import time
import matplotlib.pyplot as plt
from datetime import datetime

# 📐 Matrix Chain Multiplication DP implementation
def matrix_chain_order(p, n):
    # m[i][j] = Minimum number of multiplications needed to compute A[i..j]
    m = [[0 for _ in range(n)] for _ in range(n)]

    # L is chain length
    for L in range(2, n):  
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n - 1]

# ------------------- Console Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 1G")
print("Matrix Chain Multiplication (Dynamic Programming)")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.\n")

# Input
n = int(input("Enter number of matrices: "))
p = []

print("Enter dimensions (for n matrices you need n+1 numbers):")
for i in range(n + 1):
    p.append(int(input(f"Dimension {i}: ")))

# Execution
start_time = time.time()
min_mult = matrix_chain_order(p, n + 1)
end_time = time.time()
exec_time = end_time - start_time

print(f"\nMinimum number of multiplications = {min_mult}")

# ------------------- Chart -------------------
plt.figure(figsize=(12, 6))
bars = plt.bar(["Matrix Chain Multiplication (DP)"], [exec_time], color='teal')
plt.ylabel("Execution Time (seconds)")
plt.title("Matrix Chain Multiplication Using Dynamic Programming")

# Annotate bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.00001, f"{height:.6f}s",
             ha='center', fontsize=10)

# Complexity details
info = (
    "Time Complexity:\n"
    "  O(n^3) — due to three nested loops\n\n"
    "Space Complexity:\n"
    "  O(n^2) — DP table used to store intermediate results\n\n"
    "Best / Worst / Average Case:\n"
    "  All have same complexity (O(n^3))\n"
    f"\nMinimum Multiplications for {n} matrices: {min_mult}"
)

plt.text(0.6, exec_time * 0.5, info,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
