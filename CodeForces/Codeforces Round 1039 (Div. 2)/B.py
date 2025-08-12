import sys

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        p = list(map(int, input[ptr:ptr + n]))
        ptr += n
        
        q = []
        s = []
        left = 0
        right = n - 1
        for _ in range(n):
            if left > right:
                break
            if p[left] < p[right]:
                q.append(p[left])
                s.append('L')
                left += 1
            else:
                q.append(p[right])
                s.append('R')
                right -= 1
            # Check if the last 5 elements form a bad sequence
            if len(q) >= 5:
                last_five = q[-5:]
                increasing = True
                decreasing = True
                for i in range(4):
                    if last_five[i] >= last_five[i + 1]:
                        increasing = False
                    if last_five[i] <= last_five[i + 1]:
                        decreasing = False
                if increasing or decreasing:
                    # Need to undo the last move and choose the other option
                    if s[-1] == 'L':
                        left -= 1
                        q.pop()
                        s.pop()
                        # Now choose 'R'
                        q.append(p[right])
                        s.append('R')
                        right -= 1
                    else:
                        right += 1
                        q.pop()
                        s.pop()
                        # Now choose 'L'
                        q.append(p[left])
                        s.append('L')
                        left += 1
        print(''.join(s))

solve()