def checkFree(k: int, c: int, a: list[int]) -> bool:
    for i in range(k):   
        exp = k - 1 - i
        if exp >= 63: 
            return False

        pow2 = 1 << exp
        
        if a[i] > c // pow2:
            return False
    return True

def solve():
    st = input().split()
    n = int(st[0])
    c = int(st[1])

    a = list(map(int, input().split()))

    a.sort()

    low = 0
    high = n
    maxFree = 0

    while low <= high:
        k = low + (high - low) // 2
        if k == 0:
            maxFree = max(maxFree, k)
            low = k + 1
            continue
        
        if checkFree(k, c, a):
            maxFree = k 
            low = k + 1
        else:
            high = k - 1
    
    print(n - maxFree)

n = int(input())
for _ in range(n):
    solve()