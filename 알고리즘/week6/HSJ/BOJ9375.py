T = int(input())

for tc in range(1, T+1):
  n = int(input())
  have = []
  kind = []
  cnt = 1

  for _ in range(n):
    c, k = input().split()
    have.append([c, k])
    kind.append(k)

    copy_kind = kind
    copy_kind = list(set(copy_kind))

  for ck in copy_kind:
    cnt *= kind.count(ck) + 1

  print(cnt - 1)