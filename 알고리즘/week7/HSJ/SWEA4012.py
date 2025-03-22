T = int(input())


def comb(cnt, idx):
    if cnt == N // 2:
        a_list.append(path[:])
        return

    for i in range(idx, N):
        path.append(i)
        comb(cnt + 1, i + 1)
        path.pop()


def compare(idx):
    a = b = 0
    for i in range(len(a_list[idx])):
        for j in range(i+1, len(a_list[idx])):
            a += S[a_list[idx][i]][a_list[idx][j]] + S[a_list[idx][j]][a_list[idx][i]]
    for i in range(len(b_list[idx])):
        for j in range(i+1, len(b_list[idx])):
            b += S[b_list[idx][i]][b_list[idx][j]] + S[b_list[idx][j]][b_list[idx][i]]
    dif = abs(a-b)
    return dif


for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    path = []
    a_list = []
    b_list = []
    min = 20000

    comb(0, 0)

    for a in a_list:
        b = []
        for idx in range(N):
            if idx not in a:
                b.append(idx)
        b_list.append(b)
        
    for i in range(len(a_list)):
        temp = compare(i)
        if min > temp:
            min = temp

    print(f'#{tc} {min}')