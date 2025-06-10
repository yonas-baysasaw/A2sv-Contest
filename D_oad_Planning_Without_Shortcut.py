import collections
import sys

def solve():
    n, m, s, t = map(int, sys.stdin.readline().split())

    adj = [[] for _ in range(n + 1)]
    connected_pairs = set()

    for _ in range(m):
        u_road, v_road = map(int, sys.stdin.readline().split())
        adj[u_road].append(v_road)
        adj[v_road].append(u_road)
        connected_pairs.add(frozenset({u_road, v_road}))

    dist_s = [-1] * (n + 1)
    q_s = collections.deque()
    dist_s[s] = 0
    q_s.append(s)
    while q_s:
        curr = q_s.popleft()
        for neighbor in adj[curr]:
            if dist_s[neighbor] == -1:
                dist_s[neighbor] = dist_s[curr] + 1
                q_s.append(neighbor)

    dist_t = [-1] * (n + 1)
    q_t = collections.deque()
    dist_t[t] = 0
    q_t.append(t)
    while q_t:
        curr = q_t.popleft()
        for neighbor in adj[curr]:
            if dist_t[neighbor] == -1:
                dist_t[neighbor] = dist_t[curr] + 1
                q_t.append(neighbor)

    original_dist_st = dist_s[t]
    count = 0
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if frozenset({u, v}) not in connected_pairs:
                if dist_s[u] + 1 + dist_t[v] >= original_dist_st and \
                   dist_s[v] + 1 + dist_t[u] >= original_dist_st:
                    count += 1
    sys.stdout.write(str(count) + "\n")

solve()
