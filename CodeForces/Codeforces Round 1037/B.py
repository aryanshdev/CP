def solve():
    n,k = map(int,input().split(' '))
    arr = list(map(int, input().split(' ')))
    peaks = 0
    counter = 0
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            counter +=1
            if counter == k:
                counter = 0
                peaks +=1
                i += 1
        else:
            counter = 0
        i += 1
    print(peaks)


t = int(input())
for _ in range(t):
    solve()