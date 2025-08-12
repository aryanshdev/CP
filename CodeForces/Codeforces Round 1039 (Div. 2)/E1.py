import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, k = map(int, input[ptr:ptr + 2])
        ptr += 2
        a = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        v_max = max(a)
        # Find all positions where v_max occurs
        positions = [i for i, x in enumerate(a) if x == v_max]
        # We need to find a subarray of length >=k that includes at least one v_max
        # The simplest way is to take a window of size k around any v_max
        found = False
        l, r = 0, 0
        for pos in positions:
            # The subarray must be of length at least k and include pos
            # The minimal subarray is [pos, pos + k -1] or [pos -k +1, pos], but need to stay within bounds
            # Let's try to take a window of size k centered around pos if possible
            start = max(0, pos - (k - 1))
            end = start + k - 1
            if end < n:
                l, r = start + 1, end + 1  # converting to 1-based
                found = True
                break
            else:
                end = n - 1
                start = end - k + 1
                if start >= 0:
                    l, r = start + 1, end + 1
                    found = True
                    break
        if not found:
            # If no such window found (unlikely as per problem statement), take the first occurrence and extend
            pos = positions[0]
            l = max(1, pos + 1 - k + 1)
            r = pos + 1
        print(v_max, l, r)

solve()