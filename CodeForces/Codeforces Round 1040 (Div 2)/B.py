def solve():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n, s = map(int, input[ptr:ptr+2])
        ptr += 2
        a = list(map(int, input[ptr:ptr+n]))
        ptr += n
        
        # The minimal sum is the sum of the direct path 1 to n
        minimal_sum = sum(a)
        # The maximal sum is more complex, but for the problem, perhaps not needed
        
        # Check if s is the minimal sum (direct path)
        if s == minimal_sum:
            print(-1)
            continue
        
        # Check if s is less than minimal sum or more than maximal possible
        # For the problem, perhaps any rearrangement where direct path sum != s is sufficient
        # So, try to rearrange the array such that the direct path sum is not s
        
        # The direct path sum is sum(a), but rearranged a's sum is same
        # So, if original sum is s, then any rearrangement will have sum s for direct path
        # Hence, if original sum is s, then impossible to prevent Alice
        
        # Otherwise, can we rearrange so direct path sum is not s? But sum(a) is fixed
        # So, if original sum is not s, then any rearrangement will have sum(a) != s for direct path
        
        # But Alice can take longer paths, so need to ensure no path sums to s
        
        # For the problem, perhaps the answer is -1 only if s is the direct path sum
        # Otherwise, any rearrangement is acceptable (but need to provide one)
        
        # So, if sum(a) != s, then output any rearrangement (e.g., sorted)
        # Else, output -1
        
        if sum(a) == s:
            print(-1)
        else:
            # Rearrange the array in any way, e.g., sorted
            a_sorted = sorted(a)
            print(' '.join(map(str, a_sorted)))

solve()