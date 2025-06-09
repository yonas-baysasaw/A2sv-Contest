t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    found_one = False
    for x in a:
        if x == 1:
            found_one = True
            break
    
    if found_one:
        print("YES")
    else:
        print("NO")