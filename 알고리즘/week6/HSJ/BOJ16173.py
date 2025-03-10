def dfs(r, c):
  if r == c == N-1:
    return "HaruHaru"
  
  visited[r][c] = 1
  for dr, dc in [[0, 1 * arr[r][c]], [1 * arr[r][c], 0]]:
    nr, nc = r + dr, c + dc
    if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
      if dfs(nr, nc) == "HaruHaru":
        return "HaruHaru"
  return "Hing"


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
result = dfs(0, 0)
print(result)