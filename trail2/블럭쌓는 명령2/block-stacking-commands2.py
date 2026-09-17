n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
result = []
for i in range(k):
    result.append(abs(n-k))

print(max(result))