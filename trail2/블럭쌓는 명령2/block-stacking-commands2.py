n, k = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
lst = [0]*(n+1)
for a, b in arr:

    for i in range(a, b+1):
        lst[i] += 1

print(max(lst))
