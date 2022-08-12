# codingninjas.com/codestudio/problems/count-ways-to-reach-nth-stairs_798650

def climb_stairs_recursion_naive(n):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    return climb_stairs_recursion_naive(n-1) + climb_stairs_recursion_naive(n-2)

def climb_stairs_recursion_dp(n, dp):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2
    if dp.get(n) is not None:
        return dp[n]
    dp[n] = climb_stairs_recursion_dp(n-1, dp) + climb_stairs_recursion_dp(n-2, dp)
    return dp[n]

def countDistinctWays(nStairs: int) -> int:
    if nStairs == 0:
        return 1
    if nStairs <= 3:
        return nStairs
    a = 2
    b = 3
    for _ in range(4, nStairs+1):
        curr = a+b
        a = b
        b = curr
    return curr

print(countDistinctWays(10))

# 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887,

# input = [10, 51,1,76,18,54,9,49,26,49,22]

# 32951280099
# 1
# 5527939700884757
# 4181
# 139583862445
# 55
# 12586269025
# 196418
# 12586269025
# 28657

# 951279875
# 1
# 662189184
# 4181
# 583861472
# 55
# 586268941
# 196418
# 586268941
# 28657
