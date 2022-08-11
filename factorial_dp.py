from datetime import datetime


def factorial_recursion_naive(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial_recursion_naive(n-1)

def factorial_recursion_dp(n: int, dp: dict) -> int:
    if n == 0:
        return 1
    if dp.get(n) is not None:
        return dp[n]
    dp[n] = n * factorial_recursion_dp(n-1, dp)
    return dp[n]

def factorial_loop(n: int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


factorial_num = 30

start = datetime.now()
print(factorial_recursion_dp(factorial_num, {}))
print("DP Recursion Code Time", (datetime.now() - start).total_seconds())

start = datetime.now()
print(factorial_loop(factorial_num))
print('Loop Code Time', (datetime.now() - start).total_seconds())

start = datetime.now()
print(factorial_recursion_naive(factorial_num))
print('Naive Recursion Code Time', (datetime.now() - start).total_seconds())