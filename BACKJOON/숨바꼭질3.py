dp = [100000] * 200000
n, k = map(int, input().split())
dp[n] = 0

def find_dp(now, x):
    print(x, abs(k-n), x>abs(k-n), now>k*2 )
    if(now<=0 or x>abs(k-n)):
        return

    dp[now] = min(x, dp[now])
    if now == k:
        return

    print(dp[now-1]>x+1, now, x, dp[now-1])
    if (dp[now*2]>x):
        find_dp(now*2, x)
    if(now>0 and dp[now-1]>x+1):
        find_dp(now-1, x+1)
    if(now<=k*2 and dp[now+1]>x+1):
        find_dp(now+1, x+1)

now = n
find_dp(now, 0)

print(dp[k])