a = [list(map(int, input().split())) for _ in range(2)]

for i in a:
    print(sum(i)/len(i), end=' ')
print()

for i in range(1):
    for j in range(4):
        print((a[i][j]+a[i+1][j])/2, end=' ')
print()

total=[]
for i in range(2):
    for j in range(4):
        total.append(a[i][j])
print(f'{sum(total)/len(total):.1f}')
 

