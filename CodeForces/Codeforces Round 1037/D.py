import heapq

def solve():
    n, k = map(int, input().split())
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    casinos.sort()
    curr = k
    maxCoin = k
    playable = [] 
    i = 0
    while True:
        while i < n and casinos[i][0] <= curr:
            l, r, real = casinos[i]
            if curr <= r:
                heapq.heappush(playable, -real)
            
            i += 1
        if not playable:
            break
        choose = -heapq.heappop(playable) 
        if choose <= curr:
            break
        else:
            curr = choose
            maxCoin = max(maxCoin, curr)
            
    print(maxCoin)

t = int(input())
for _ in range(t):
    solve()