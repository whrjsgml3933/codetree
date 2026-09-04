a = list(map(int, input().split()))

cur = 0
for i in a:
    if i == 0:
        result = a[cur-1]+a[cur-2]+a[cur-3]
        print(result)

        break 
    cur += 1
    
    