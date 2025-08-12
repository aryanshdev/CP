import sys

def solve():
    n = int(sys.stdin.readline())
    p = [0] + list(map(int, sys.stdin.readline().split()))
    
    invr = [0] * (n + 1)
    gl = [0] * (n + 1)
    
    bit = Tree(2 * n + 1)
    
    invp = 0
    for i in range(n, 0, -1):
        invr[i] = bit.query(p[i] - 1)
        invp += invr[i]
        bit.upd(p[i])
        
    bit.init(2 * n + 1)
    
    for i in range(1, n + 1):
        gl[i] = bit.query(p[i] - 1)
        bit.upd(p[i])
    
    sum_neg = 0
    for i in range(1, n + 1):
        D = (n - p[i]) - invr[i] - gl[i]
        if D < 0:
            sum_neg += D
    
    ans = invp + sum_neg
    print(ans)

class Tree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def init(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def upd(self, index):
        while index <= self.size:
            self.tree[index] += 1
            index += index & (-index)
            
    def query(self, index):
        s = 0
        while index > 0:
            s += self.tree[index]
            index -= index & (-index)
        return s

t = int(sys.stdin.readline())
for _ in range(t):
    solve()