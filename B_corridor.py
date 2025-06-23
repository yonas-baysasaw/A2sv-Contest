t = int(input())
for _ in range(t):
    n = int(input())
    max_k = float('inf')
    for _ in range(n):
        d, s = map(int, input().split())
        current_max = d + (s - 1) // 2
        if current_max < max_k:
            max_k = current_max
    print(max_k)