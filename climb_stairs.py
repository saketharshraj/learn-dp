# codingninjas.com/codestudio/problems/count-ways-to-reach-nth-stairs_798650

def climb_stairs_recursion_naive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return climb_stairs_recursion_naive(n-1) + climb_stairs_recursion_naive(n-2)

def climb_stairs_recursion_dp(n, dp):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dp.get(n) is not None:
        return dp[n]
    dp[n] = climb_stairs_recursion_dp(n-1, dp) + climb_stairs_recursion_dp(n-2, dp)
    return dp[n]

