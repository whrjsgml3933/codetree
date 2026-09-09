a = [list(input().split()) for _ in range(5)]

for i in a:
    for j in i:
        j.upper()
        print(j.upper(), end=' ')
    print()