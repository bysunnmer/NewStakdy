T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    min = 100000

    for i in range(N):
        for j in range(N):
            s = arr[i][j]
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx, ny = i + dx, j + dy
                while 0 <= nx < N and 0 <= ny < N:
                    s += arr[nx][ny]
                    nx += dx
                    ny += dy
            if s > max:
                max = s
            if s < min:
                min = s

    result = max - min
    print(f'#{tc} {result}')