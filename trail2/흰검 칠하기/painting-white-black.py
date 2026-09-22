n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

x = []
direction = []
for num, dir_val in commands:
    x.append(int(num))
    direction.append(dir_val)

# 딕셔너리로 타일 상태 관리 { 좌표: {'w': 흰색 횟수, 'b': 검은색 횟수, 'last': 마지막 색상} }
tiles = {}
curr = 0  # 시작 위치

for i in range(n):
    cnt = x[i]
    d = direction[i]
    
    if d == 'L':
        # 왼쪽으로 이동하면서 현재 위치 포함 총 cnt칸을 흰색으로 칠함
        start = curr - cnt + 1
        end = curr
        for p in range(start, end + 1):
            if p not in tiles:
                tiles[p] = {'w': 0, 'b': 0, 'last': None}
            tiles[p]['w'] += 1
            tiles[p]['last'] = 'W'
        curr = start  # 마지막으로 칠한 타일 위치로 이동
        
    elif d == 'R':
        # 오른쪽으로 이동하면서 현재 위치 포함 총 cnt칸을 검은색으로 칠함
        start = curr
        end = curr + cnt - 1
        for p in range(start, end + 1):
            if p not in tiles:
                tiles[p] = {'w': 0, 'b': 0, 'last': None}
            tiles[p]['b'] += 1
            tiles[p]['last'] = 'B'
        curr = end  # 마지막으로 칠한 타일 위치로 이동

# 최종 타일 색상 카운트
white_count = 0
black_count = 0
gray_count = 0

for p, info in tiles.items():
    # 흰색과 검은색으로 각각 두 번 이상 칠해진 경우 회색
    if info['w'] >= 2 and info['b'] >= 2:
        gray_count += 1
    elif info['last'] == 'W':
        white_count += 1
    elif info['last'] == 'B':
        black_count += 1
        
print(f"{white_count} {black_count} {gray_count}")