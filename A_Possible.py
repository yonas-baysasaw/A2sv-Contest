t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if 1 not in a:
        print("NO")
        continue

    print("YES")
