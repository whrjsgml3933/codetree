num1, num2 = map(int, input().split())

arr = [0] * 10
arr[0] = num1
arr[1] = num2

for i in range(2, 10):
    if (arr[i-1] + arr[i-2])%10 < 0:
        arr[i] = arr[i-1] + arr[i-2]
    else:
        arr[i] = (arr[i-1] + arr[i-2])%10 

print(*arr)