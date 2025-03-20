N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]
cnt = 0

for idx in range(N-1, -1, -1):
    if A[idx] > K:
        continue
    cnt += K // A[idx]
    K %= A[idx]
    if K == 0:
        break

print(cnt)
