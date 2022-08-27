# 참외밭_BOJ2477

# input.txt 열기
import sys
sys.stdin = open('input.txt')

# input 받기
K = int(input()) # 1m^2에서 자라는 참외의 개수
node = [list(map(int, input().split())) for n in range(6)] # 0번인덱스 : 꼭지점의 방향(동:1, 서:2, 남:3, 북:4) / 1번인덱스 : 길이

# 참외밭 구하기
east = []
west = []
south = []
north = []

print(node)
idx = 0
for n in node:
    if n[0] == 1:
        east.append(idx)
        east.append(n[1])
        idx += 1
    elif n[0] == 2:
        west.append(idx)
        west.append(n[1])
        idx += 1
    elif n[0] == 3:
        south.append(idx)
        south.append(n[1])
        idx += 1
    elif n[0] == 4:
        north.append(idx)
        north.append(n[1])
        idx += 1

# 큰 사각형의 넓이
if len(south) < len(north):
    if len(east) < len(west):
        big_earth = south[1] * east[1]
    elif len(east) > len(west):
        big_earth = south[1] * west[1]
elif len(south) > len(north):
    if len(east) < len(west):
        big_earth = north[1] * east[1]
    elif len(east) > len(west):
        big_earth = north[1] * west[1]

print(big_earth)

# 작은 사각형 구하기
if len(east) == 4 and len(south) == 4:
    print(east, south)

elif len(east) == 4 and len(north) == 4:
    print(east, north)

elif len(west) == 4 and len(north) == 4:
    print(west, north)

elif len(west) == 4 and len(south) == 4:
    print(west, south)
