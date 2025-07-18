def solve():
    x = int(input())

    xDig = set()
    tempx = x
    if tempx == 0:
        xDig.add(0)
    while tempx > 0:
        xDig.add(tempx % 10)
        tempx //= 10

    if 0 in xDig:
        print(0)
        return

    y = 1
    while True:
        tempy = y
        hasCom = False
        if tempy == 0: 
            pass
        else:
            while tempy > 0:
                if (tempy % 10) in xDig:
                    hasCom = True
                    break
                tempy //= 10
        
        if hasCom:
            print(y)
            return
        y += 1

t = int(input())
for _ in range(t):
    solve()