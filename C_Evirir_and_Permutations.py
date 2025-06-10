num_test_cases = int(input())
for _ in range(num_test_cases):
    n = int(input())
    s = input().strip()

    R_p = [n] * n
    min_p_idx_from_right = n + 1
    for j in range(n - 1, -1, -1):
        if s[j] == 'p':
            min_p_idx_from_right = j + 1
        R_p[j] = min_p_idx_from_right
    for i in range(n):
        if R_p[i] == n + 1:
            R_p[i] = n

    R_s = [n] * n
    min_s_val_from_left = n + 1
    for j in range(n):
        if s[j] == 's':
            min_s_val_from_left = min(min_s_val_from_left, n - (j + 1) + 1)
        R_s[j] = min_s_val_from_left
    for i in range(n):
        if R_s[i] == n + 1:
            R_s[i] = n

    U = [0] * n
    for j in range(n):
        U[j] = min(R_p[j], R_s[j])
    U.sort()
    possible = True
    for k in range(n):
        if U[k] < k + 1:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")

