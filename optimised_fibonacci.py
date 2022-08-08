from datetime import datetime

def fibonacci_optimised(n, dp: dict):
    if n <= 1:
        return n
    
    if dp.get(n) is not None:
        return dp[n]

    dp[n] = fibonacci_optimised(n-1, dp) + fibonacci_optimised(n-2, dp)
    return dp[n]


def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)


start = datetime.now()
print(fibonacci_optimised(30, {}))
print("Pro Code Time", (datetime.now() - start).total_seconds())

start = datetime.now()
print(fibonacci_naive(30))
print('Noob Code Time', (datetime.now() - start).total_seconds())

