from bisect import bisect_left

def process_case(n, p):
    total = 0
    i = 0
    while i < n:
        j = i
        while j + 2 < n and max(p[j], p[j + 1]) > p[j + 2]:
            j += 1
        seg = p[i:j + 2]
        m = len(seg)

        
        for l in range(m):
            tails = []
            for r in range(l, m):
                x = seg[r]
                pos = bisect_left(tails, -x)
                if pos == len(tails):
                    tails.append(-x)
                else:
                    tails[pos] = -x
                total += len(tails)

        i = j + 2
    return total

n = int(input())
for _ in range(n):
    n = int(input())
    p = list(map(int, input().split()))
    result = process_case(n, p)
    print(result)
