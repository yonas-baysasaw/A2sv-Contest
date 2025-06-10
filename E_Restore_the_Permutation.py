import collections
import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    b_list = list(map(int, input().split()))

    start_events = [collections.deque() for _ in range(n + 2)] 
    end_buckets = [collections.deque() for _ in range(n + 1)]

    for idx in range(n):
        position = idx + 1
        b_val = b_list[idx]

        left_bound = 0
        right_bound = 0

        if b_val == 0:
            left_bound = position + 1
            right_bound = n
        else:
            left_bound = (position // (b_val + 1)) + 1
            right_bound = (position // b_val)
        
        if left_bound <= n + 1: 
            start_events[left_bound].append((right_bound, idx))
        
    permutation = [0] * n
    min_right_bucket = 1 

    for value in range(1, n + 1):
        for right_val, original_idx in start_events[value]:
            if right_val <= n: 
                end_buckets[right_val].append(original_idx)
            
        while min_right_bucket <= n and not end_buckets[min_right_bucket]:
            min_right_bucket += 1
        
        assign_idx = end_buckets[min_right_bucket].popleft()
        permutation[assign_idx] = value

    sys.stdout.write(" ".join(map(str, permutation)) + "\n")

num_test_cases = int(input())
for _ in range(num_test_cases):
    solve()
