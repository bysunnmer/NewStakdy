import heapq

N = int(input())
room = []
pq = []

for i in range(N):
    S, T = map(int, input().split())
    room.append([S, T])
room.sort()

heapq.heappush(pq, room[0][1])
for r in range(1, N):
    if room[r][0] < pq[0]:
        heapq.heappush(pq, room[r][1])
    else:
        heapq.heappop(pq)
        heapq.heappush(pq, room[r][1])
        
print(len(pq))