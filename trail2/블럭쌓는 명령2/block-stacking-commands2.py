n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
print(abs(k-n))