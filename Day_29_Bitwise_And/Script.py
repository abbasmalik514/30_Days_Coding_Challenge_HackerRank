t = int(input())
for _ in range(t): 
    n, k = map(int, input().split())
    max_result = 0

    for i in range(n-1, 1, -1):
        for j in range(n, i, -1):
            bitwise_result = i & j
            if bitwise_result < k and bitwise_result > max_result:
                max_result = bitwise_result
            if max_result == k-1:
                break
        if max_result == k-1:
            break
    print(max_result)
