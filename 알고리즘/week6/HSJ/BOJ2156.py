n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * n

if n >= 1:
    dp[0] = arr[0]
if n >= 2:
    dp[1] = dp[0] + arr[1]
if n >= 3:
    dp[2] = max(dp[0] + arr[2], dp[1], arr[1] + arr[2])

if n >= 4:
    for i in range(3, n):
        dp[i] = max(dp[i-2] + arr[i], arr[i] + arr[i-1] + dp[i-3], dp[i-1])

print(dp[n-1])