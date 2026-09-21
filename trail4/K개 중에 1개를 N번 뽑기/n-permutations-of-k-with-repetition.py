K, N = map(int, input().split())

# Please write your code here.
answer = [0] * N

def choose(idx):
    if idx == N:
        print(*answer)
        return
    for i in range(1, K+1):
        answer[idx] = i
        choose(idx+1)

choose(0)