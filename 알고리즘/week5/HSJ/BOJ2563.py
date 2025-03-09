N = int(input())
black = 0
visited = [[0] * 101 for _ in range(101)]
cnt = 0
for _ in range(N):
    l, b = map(int, input().split())
    for i in range(1, 11):
        for j in range(1, 11):
            visited[l+i][b+j] = 1
for i in range(1, 101):
    for j in range(1, 101):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)
