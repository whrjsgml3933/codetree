a = list(map(int, input().split()))

a_sum = 0
b = 0
c = 0
for i in a[1::2]:
    a_sum += i

for i in a[2::3]:
    b += i
    c += 1
print(f'{a_sum} {(b/c):.1f}')