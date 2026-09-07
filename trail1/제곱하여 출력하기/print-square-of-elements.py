N = int(input())
arr = list(map(int, input().split()))

[print(f'{arr[i]**2}', end=' ') for i in range(N)]

