def checkDecom(s, m) :
    currS = s
    currM = m
    while currS > 0:
        if currM <= 0:
            return False
        x = currS // 2 + 1
        
        if x > currM:
            return False
        
        currS -= x
        currM = x - 1 
    return True

def solve():
    n = int(input())
    b = list(map(int, input().split()))

    if n <= 1:
        print("YES")
        return

    minPre = b[0]
    possible = True

    for i in range(1, n):
    
        if not checkDecom(b[i], minPre):
            possible = False
            break
        minPre = min(minPre, b[i])

    if possible:
        print("YES")
    else:
        print("NO")

n = int(input())
for _ in range(n):
    solve()