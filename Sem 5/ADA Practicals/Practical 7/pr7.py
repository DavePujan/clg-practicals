import time 
import matplotlib.pyplot as plt
import sys
from datetime import datetime

# Increase recursion limit
sys.setrecursionlimit(10000)

# 🔁 Recursive solution (Exponential)
def coin_change_recursive(coins, m, amount):
    if amount == 0:
        return 0
    res = float('inf')
    for i in range(m):
        if coins[i] <= amount:
            sub_res = coin_change_recursive(coins, m, amount - coins[i])
            if sub_res != float('inf') and sub_res + 1 < res:
                res = sub_res + 1
    return res

# 🔁 Dynamic Programming solution (Efficient)
def coin_change_dp(coins, m, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in range(m):
            if coins[j] <= i:
                sub_res = dp[i - coins[j]]
                if sub_res != float('inf') and sub_res + 1 < dp[i]:
                    dp[i] = sub_res + 1
    return dp[amount]

# ⏱️ Time measurement function
def measure_time(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

# ------------------- Program Output -------------------
print(f"Thu {datetime.now().strftime('%b %d %H:%M:%S %Y')}")
print("Practical No : 1E")
print("Making Change Problem (Recursive & Dynamic Programming)")
print("Enrollment No : 230130107024")
print("Name : Dave Pujan M.")

# Input
amount = int(input("\nEnter the amount: "))
coins = list(map(int, input("Enter coin denominations (space separated): ").split()))
m = len(coins)

# Results
rec_res = coin_change_recursive(coins, m, amount)
dp_res = coin_change_dp(coins, m, amount)

print(f"\nMinimum coins required for {amount} using Recursive: {rec_res}")
print(f"Minimum coins required for {amount} using DP: {dp_res}")

# ------------------- Chart Comparison -------------------
time_recursive = measure_time(coin_change_recursive, coins, m, amount)
time_dp = measure_time(coin_change_dp, coins, m, amount)

methods = ['Recursive', 'Dynamic Programming']
times = [time_recursive, time_dp]

plt.figure(figsize=(12, 6))
bars = plt.bar(methods, times, color=['blue', 'green'])

# Annotate bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height + 0.0001,
             f"{height:.6f} s", ha='center', fontsize=10)

# 📘 Complexity details
info_text = (
    "Coin Change Problem Time & Space Complexity:\n\n"
    "Recursive Method:\n"
    "  Time: Exponential O(2^n)\n"
    "  Space: O(amount) (due to recursion depth)\n\n"
    "Dynamic Programming Method:\n"
    "  Time: O(n * amount)\n"
    "  Space: O(amount)\n\n"
    "Best / Worst / Avg Case: Same (depends on amount)\n"
)

# 🧾 Add text box to plot
plt.text(0.6, max(times) * 0.6, info_text,
         fontsize=10, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))

plt.title(f"Making Change Problem (Amount = {amount}) - Recursive vs DP", fontsize=14)
plt.ylabel("Execution Time (seconds)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
