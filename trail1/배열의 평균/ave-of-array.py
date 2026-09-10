a = [list(map(int, input().split())) for _ in range(2)]

for i in a:
    print(sum(i)/len(i), end=' ')
print()

for i in range(1):
    for j in range(4):
        print((a[i][j]+a[i+1][j])/2, end=' ')
print()

total=[]
for i in range(len(a)):
    for j in range(len(a[0])):
        total.append(a[i][j])
print(sum(total)/len(total))
 

