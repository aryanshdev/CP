import sys
from collections import defaultdict, deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        n = int(input[ptr])
        ptr += 1
        pairs = []
        for i in range(n):
            a, b = map(int, input[ptr:ptr+2])
            ptr += 2
            pairs.append((a, b, i+1)) 
        pairs.sort(key=lambda x: x[1])
        
        parent = {}
        
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u
        
        selected = []
        for a, b, idx in pairs:
            u, v = a, b
            if u not in parent:
                parent[u] = u
            if v not in parent:
                parent[v] = v
            if find(u) != find(v):
                union(u, v)
                selected.append(idx)
       
        intervals = []
        for a, b, idx in pairs:
            if idx in selected:
                intervals.append((a, b))
        
        if not intervals:
            currF = 0
        else:
            intervals.sort()
            unionInt = []
            currStart, currEnd = intervals[0]
            for s, e in intervals[1:]:
                if s <= currEnd:
                    currEnd = max(currEnd, e)
                else:
                    unionInt.append((currStart, currEnd))
                    currStart, currEnd = s, e
            unionInt.append((currStart, currEnd))
            currF = 0
            for s, e in unionInt:
                currF += e - s
        
        maxDif = currF - 0
        bestIdx = selected.copy()
        remaining = [ (a, b, idx) for a, b, idx in pairs if idx not in selected ]
        
        graph = defaultdict(list)
        nodes = set()
        for a, b, idx in pairs:
            if idx in selected:
                u, v = a, b
                graph[u].append(v)
                graph[v].append(u)
                nodes.add(u)
                nodes.add(v)
        
        for a, b, idx in remaining:
            graph[a].append(b)
            graph[b].append(a)
            nodes.add(a)
            nodes.add(b)
            
            tempInt = intervals.copy()
            tempInt.append((a, b))
            tempInt.sort()
            newF = 0
            if tempInt:
                union = []
                currS, currE = tempInt[0]
                for s, e in tempInt[1:]:
                    if s <= currE:
                        currE = max(currE, e)
                    else:
                        union.append((currS, currE))
                        currS, currE = s, e
                union.append((currS, currE))
                newF = 0
                for s, e in union:
                    newF += e - s
            visited = {}
            queue = deque()
            queue.append((a, None))
            visited[a] = 0
            found = False
            cycle = 0
            while queue and not found:
                current, parent_node = queue.popleft()
                for nieghbor in graph[current]:
                    if nieghbor == b and current != a and parent_node != b:
                       
                        cycle = visited[current] + 1
                        found = True
                        break
                    if nieghbor not in visited and nieghbor != parent_node:
                        visited[nieghbor] = visited[current] + 1
                        queue.append((nieghbor, current))
                if found:
                    break
            
            if found:
                newG = cycle + 1 
            else:
                newG = 0
            
            newDiff = newF - newG
            if newDiff > maxDif:
                maxDif = newDiff
                bestIdx = selected.copy()
                bestIdx.append(idx)
            
            graph[a].remove(b)
            graph[b].remove(a)
            if not graph[a]:
                del graph[a]
            if not graph[b]:
                del graph[b]
        
        bestIdx.sort()
        print(len(bestIdx))
        if bestIdx:
            print(' '.join(map(str, bestIdx)))
        else:
            print()

solve()