# Derangement_Sequence(!n)

def Derangement_Sequence(n):
    dp = [0 for _ in range(101)]
    dp[1], dp[2] = 0, 1
    for i in range(3, 101):
        dp[i] = (i-1)*(dp[i-1]+dp[i-2])
    return dp[n]
