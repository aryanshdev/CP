import sys

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        if n == 0:
            sys.stdin.readline()
            print(0)
            return
        s_list = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    counts = [0] * 51
    total = 0
    for x in s_list:
        if x <= 50:
            counts[x] += 1
        total += x

    score1 = total

    mex1 = 0
    while mex1 <= 50 and counts[mex1] > 0:
        mex1 += 1
    mex2 = mex1
    for i in range(mex1):
        if counts[i] == 1:
            mex2 = i
            break

    def sum_up_to(k):
        if k <= 0:
            return 0
        return (k - 1) * k // 2

    sumRemoved1 = sum_up_to(mex1)
    score2 = mex1 + (total - sumRemoved1)
    
    pt1 = sum_up_to(mex1)
    pt2 = sum_up_to(mex2)
    score3 = (mex1 + mex2) + (total - pt1 - pt2)

    print(max(score1, score2, score3))

t = sys.stdin.readline()

t = int(t)
for _ in range(t):
    solve()
