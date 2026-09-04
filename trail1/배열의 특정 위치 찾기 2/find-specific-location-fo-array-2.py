a = list(map(int, input().split()))

sum1 = sum(a[0::2])

sum2 = sum(a[1::2])

print(abs(sum1 - sum2))