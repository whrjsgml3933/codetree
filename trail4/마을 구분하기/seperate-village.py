N = int(input())
ARR = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
def dfs(str, stc):
    STACK = []
    
    STACK.append((str, stc))
    visited[str][stc] = True
    
    cnt = 0
    while STACK:
        vr, vc = STACK.pop()
        cnt += 1
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            wr = vr+dr
            wc = vc+dc
            
            if 0<=wr<N and 0<=wc<N and ARR[wr][wc] == 1:
                if visited[wr][wc]:
                    continue
                    
                STACK.append((wr, wc))
                visited[wr][wc] = True
                
    
    cnts.append(cnt)              
                    

visited = [[False] * N for _ in range(N)]

cnts = []
for row in range(N):
    for col in range(N):
        if not visited[row][col] and ARR[row][col]==1:
            dfs(row, col)
            
print(len(cnts))
cnts.sort()
for i in cnts:
    print(i)