# Kadane's Algorithm for Maximum subarray problem

def kadane(n, lst):
    dp = [lst[0]]
    for i in range(1, n):
        dp.append(max(dp[i-1]+lst[i], lst[i]))
    return max(dp)