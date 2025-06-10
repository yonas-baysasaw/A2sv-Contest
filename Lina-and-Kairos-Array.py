def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True


   

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    found_sorted_permutation = False
    
   
    for i in range(n):
        
        shifted_a = a[i:] + a[:i]
        
        if is_sorted(shifted_a):
            found_sorted_permutation = True
            break 
            
    if found_sorted_permutation:
        print("Yes")
    else:
        print("No")