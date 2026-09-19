n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
lst = [0]*10000
for i in range(n):
    a, b = segments[i]
    for j in range(a, b):
        lst[j] += 1
print(max(lst))